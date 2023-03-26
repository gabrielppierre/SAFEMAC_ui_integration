import torch
import sys
import time

def get_region_boxes(output, num_classes, num_keypoints, only_objectness=1, validation=True):
    
    # Parameters
    anchor_dim = 1 
    if output.dim() == 3:
        output = output.unsqueeze(0)
    batch = output.size(0)
    assert(output.size(1) == (2*num_keypoints+1+num_classes)*anchor_dim)
    h = output.size(2)
    w = output.size(3)

    # Activation
    t0 = time.time()
    max_conf = -sys.maxsize
    output    = output.view(batch*anchor_dim, 2*num_keypoints+1+num_classes, h*w).transpose(0,1).contiguous().view(2*num_keypoints+1+num_classes, batch*anchor_dim*h*w)
    grid_x    = torch.linspace(0, w-1, w).repeat(h,1).repeat(batch*anchor_dim, 1, 1).view(batch*anchor_dim*h*w).cuda()
    grid_y    = torch.linspace(0, h-1, h).repeat(w,1).t().repeat(batch*anchor_dim, 1, 1).view(batch*anchor_dim*h*w).cuda()
    
    xs = list()
    ys = list()
    xs.append(torch.sigmoid(output[0]) + grid_x)
    ys.append(torch.sigmoid(output[1]) + grid_y)
    for j in range(1,num_keypoints):
        xs.append(output[2*j + 0] + grid_x)
        ys.append(output[2*j + 1] + grid_y)
    det_confs = torch.sigmoid(output[2*num_keypoints])
    cls_confs = torch.nn.Softmax()(Variable(output[2*num_keypoints+1:2*num_keypoints+1+num_classes].transpose(0,1))).data
    cls_max_confs, cls_max_ids = torch.max(cls_confs, 1)
    cls_max_confs = cls_max_confs.view(-1)
    cls_max_ids   = cls_max_ids.view(-1)
    t1 = time.time()
    
    # GPU to CPU
    sz_hw = h*w
    sz_hwa = sz_hw*anchor_dim
    det_confs = convert2cpu(det_confs)
    cls_max_confs = convert2cpu(cls_max_confs)
    cls_max_ids = convert2cpu_long(cls_max_ids)
    for j in range(num_keypoints):
        xs[j] = convert2cpu(xs[j])
        ys[j] = convert2cpu(ys[j])
    if validation:
        cls_confs = convert2cpu(cls_confs.view(-1, num_classes))
    t2 = time.time()

    # Boxes filter
    for b in range(batch):
        for cy in range(h):
            for cx in range(w):
                for i in range(anchor_dim):
                    ind = b*sz_hwa + i*sz_hw + cy*w + cx
                    det_conf =  det_confs[ind]
                    if only_objectness:
                        conf = det_confs[ind]
                    else:
                        conf = det_confs[ind] * cls_max_confs[ind]
                    
                    if conf > max_conf:
                        max_conf = conf
                        bcx = list()
                        bcy = list()
                        for j in range(num_keypoints):
                            bcx.append(xs[j][ind])
                            bcy.append(ys[j][ind])
                        cls_max_conf = cls_max_confs[ind]
                        cls_max_id = cls_max_ids[ind]
                        box = list()
                        for j in range(num_keypoints):
                            box.append(bcx[j]/w)
                            box.append(bcy[j]/h)
                        box.append(det_conf)
                        box.append(cls_max_conf)
                        box.append(cls_max_id)                        
    t3 = time.time()
    if False:
        print('---------------------------------')
        print('matrix computation : %f' % (t1-t0))
        print('        gpu to cpu : %f' % (t2-t1))
        print('      boxes filter : %f' % (t3-t2))
        print('---------------------------------')
    return box
