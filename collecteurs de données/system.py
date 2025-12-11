def get_system_info():
    """Récupère les informations système générales"""
    # Nom de la machine
    hostname = socket.gethostname()
    
    # Système d'exploitation
    os_name = f"{platform.system()} {platform.release()}"
    
    # Uptime
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_delta = datetime.now() - boot_time
    hours, remainder = divmod(int(uptime_delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime = f"{hours}h {minutes}m {seconds}s"
    
    # Nombre d'utilisateurs connectés
    user_count = len(psutil.users())
    
    return {
        "hostname": hostname,
        "os_name": os_name,
        "uptime": uptime,
        "user_count": user_count
    }
