#Name:Manishkumar Singh

import platform
import psutil
import speedtest
from screeninfo import get_monitors
import socket
import tkinter

def installed_software():
 softwares=[program.name for program in psutil.process_iter(['pid', 'name'])]
 return softwares
def internet_speed():
 speed= speedtest.Speedtest()
 download_speed = speed.download() / 1_000_000  # in Mbps
 upload_speed = speed.upload() / 1_000_000  # in Mbps
 return download_speed, upload_speed
def screen_resolution():
 app=tkinter.Tk()
 screen_width=app.winfo_screenwidth()
 screen_height=app.winfo_screenheight()
 return screen_width,screen_height
def cpu_info():
 info=platform.processor()
 return info
def cpu_cores():
 cpu_cores = psutil.cpu_count(logical=False)
 return cpu_cores
def cpu_threads():
 cpu_threads = psutil.cpu_count(logical=True)
 return cpu_threads
def ram_size():
 ram = psutil.virtual_memory().total / (1024 ** 3) # in GB
 return ram
def public_ip():
 public_ip = socket.gethostbyname(socket.gethostname())
 return public_ip
 # Example usage
installed_software = installed_software()
internet_speed = internet_speed()
screen_resolution = screen_resolution()
info= cpu_info()
cpu_cores=cpu_cores()
cpu_threads=cpu_threads()
ram = ram_size()
public_ip = public_ip()

print("1.All Installed Software's List:", installed_software)
print("2.Internet Speed ", internet_speed)
print("3.Screen Resolution:", screen_resolution)
print("4.CPU Model:", cpu_info)
print("5.CPU Cores:", cpu_cores)
print("6.CPU Threads:", cpu_threads)
print("7.RAM Size:", ram, "GB")
print("8.Public IP Address:", public_ip)

