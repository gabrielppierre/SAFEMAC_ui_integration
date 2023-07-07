import psutil
import time
#import subprocess

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent


#def get_temperature():
    #try:
        #output = subprocess.check_output(['WMIC', 'CPU', 'GET', 'Temperature'])
        #output = output.decode('utf-8').strip().split('\n')
        #temperature = output[1]
        #temperature = int(temperature) / 10.0  # Convert to Celsius
        #return temperature
    #except (subprocess.CalledProcessError, IndexError):
        #return None

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
    #temp = get_temperature() or 0
    fps = get_fps(frame_count, start_time)  


frame_count = 100  
start_time = time.time()
print_system_info(frame_count, start_time)
