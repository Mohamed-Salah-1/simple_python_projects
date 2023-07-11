"""
My Module - Example module utilizing the psutil library.

This module demonstrates the usage of the psutil library to retrieve system
information such as CPU usage, memory usage, and network statistics.
"""
import time
import platform
import psutil


# Get network information
net_io_counters1 = psutil.net_io_counters()
time.sleep(1)
net_io_counters2 = psutil.net_io_counters()

# Calculate upload and download speed
bytes_sent = net_io_counters2.bytes_sent - net_io_counters1.bytes_sent
bytes_recv = net_io_counters2.bytes_recv - net_io_counters1.bytes_recv
upload_speed = bytes_sent / (1024 * 1024)
download_speed = bytes_recv / (1024 * 1024)

# Get information about other connected devices
net_connections = psutil.net_connections()
OUTPUT = ""
for conn in net_connections:
    if conn.status == "ESTABLISHED" and conn.pid is not None:
        try:
            PROCESS_NAME = psutil.Process(conn.pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            PROCESS_NAME = "-"
        if "chrome" not in PROCESS_NAME.lower() and "firefox" not in PROCESS_NAME.lower():
            local_address = f"{conn.laddr.ip}, {conn.laddr.port}"
            remote_address = f"{conn.raddr.ip}, {conn.raddr.port}"
            os_name = platform.system()
            OUTPUT += f"Local address: {local_address}\n"
            OUTPUT += f"Remote address: {remote_address}\n"
            OUTPUT += f"Process ID: {conn.pid}\n"
            OUTPUT += f"Process name: {PROCESS_NAME}\n"
            OUTPUT += f"Operating System: {os_name}\n"
            OUTPUT += f"Status: {conn.status}\n\n"

OUTPUT += f"Upload speed: {upload_speed:.2f} MB/s\n"
OUTPUT += f"Download speed: {download_speed:.2f} MB/s\n"

# Write OUTPUT to file
with open("network_info.txt", "w", encoding='utf-8') as file:
    file.write(OUTPUT)

print("Network information saved to network_info.txt")
