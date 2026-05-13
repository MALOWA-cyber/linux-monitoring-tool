import psutil
import platform
import datetime

def system_report():
    print("===== Linux System Monitoring Tool =====")
    print(f"System: {platform.system()}")
    print(f"Computer Name: {platform.node()}")
    print(f"OS Release: {platform.release()}")
    print(f"Time: {datetime.datetime.now()}")
    print("----------------------------------------")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")

    if cpu > 80:
        print("ALERT: High CPU usage detected!")

    if memory.percent > 80:
        print("ALERT: High memory usage detected!")

    if disk.percent > 80:
        print("ALERT: Low disk space detected!")

    with open("system_report.txt", "a") as file:
        file.write("===== Linux System Monitoring Tool =====\n")
        file.write(f"Time: {datetime.datetime.now()}\n")
        file.write(f"CPU Usage: {cpu}%\n")
        file.write(f"Memory Usage: {memory.percent}%\n")
        file.write(f"Disk Usage: {disk.percent}%\n")
        file.write("----------------------------------------\n")

system_report()
print("Report saved to system_report.txt")
