import psutil
import time
import platform

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
output = ""
for conn in net_connections:
    if conn.status == "ESTABLISHED" and conn.pid is not None:
        try:
            process_name = psutil.Process(conn.pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            process_name = "-"
        if "chrome" not in process_name.lower() and "firefox" not in process_name.lower():
            local_address = "{}:{}".format(conn.laddr.ip, conn.laddr.port)
            remote_address = "{}:{}".format(conn.raddr.ip, conn.raddr.port)
            os_name = platform.system()
            output += f"Local address: {local_address}\n"
            output += f"Remote address: {remote_address}\n"
            output += f"Process ID: {conn.pid}\n"
            output += f"Process name: {process_name}\n"
            output += f"Operating System: {os_name}\n"
            output += f"Status: {conn.status}\n\n"

output += f"Upload speed: {upload_speed:.2f} MB/s\n"
output += f"Download speed: {download_speed:.2f} MB/s\n"

# Write output to file
with open("network_info.txt", "w") as file:
    file.write(output)

print("Network information saved to network_info.txt")
