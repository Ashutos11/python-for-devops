import psutil

def get_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("C:/").percent

    cpu_threshold = 70
    memory_threshold = 60
    disk_threshold = 80

    cpu_status = "High CPU usage" if cpu_usage > cpu_threshold else "Healthy CPU"
    memory_status = "High memory status" if memory_usage > memory_threshold else "Healthy memory"
    disk_status = "High disk usage" if disk_usage > disk_threshold else "Healthy disk"

    return {
        "cpu_status": cpu_status,
        "memory_status": memory_status,
        "disk_status": disk_status
    }