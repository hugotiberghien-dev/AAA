def get_disk_info():
    """Récupère les informations disque"""
    disk = psutil.disk_usage('/')
    
    disk_total = get_size_gb(disk.total)
    disk_used = get_size_gb(disk.used)
    disk_percent = disk.percent
    disk_color = get_color_class(disk_percent)
    
    return {
        "disk_total": disk_total,
        "disk_used": disk_used,
        "disk_percent": disk_percent,
        "disk_color": disk_color
    }
