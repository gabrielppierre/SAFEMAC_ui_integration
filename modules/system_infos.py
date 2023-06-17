import psutil
import wmi
import time

w = wmi.WMI(namespace="root\OpenHardwareMonitor")

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_temperature():
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType == u'Temperature':
            return sensor.Value
    return 0


def get_fps(frame_count, start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time == 0: 
        return 0
    else:
        return frame_count / elapsed_time

def print_system_info(frame_count, start_time):
    cpu = get_cpu_usage()
    ram = get_ram_usage()
    temp = get_temperature() or 0
    fps = get_fps(frame_count, start_time)  

    print(f"CPU usage: {cpu:.2f}%")  
    print(f"RAM usage: {ram:.2f}%")  
    print(f"Temperature: {temp:.2f} C")  
    print(f"FPS: {fps:.2f}")  


frame_count = 100  
start_time = time.time()
print_system_info(frame_count, start_time)
