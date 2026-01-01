import psutil


def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    cpu_threshold = 50
    status = "healthy" if cpu_percent <= cpu_threshold else "high cpu"

    return {
        "cpu_percentage": cpu_percent,
        "memory_percentage": memory_percent,
        "disk_percentage": disk_percent,
        "cpu_threshold": cpu_threshold,
        "system_status": status,
    }
