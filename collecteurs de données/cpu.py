def get_cpu_info():
    """Récupère les informations CPU"""
    # Nombre de cœurs
    cpu_cores = psutil.cpu_count(logical=True)
    
    # Fréquence CPU
    cpu_freq_info = psutil.cpu_freq()
    cpu_freq = round(cpu_freq_info.current, 2) if cpu_freq_info else "N/A"
    
    # Pourcentage d'utilisation global
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Classe couleur
    cpu_color = get_color_class(cpu_percent)
    
    return {
        "cpu_cores": cpu_cores,
        "cpu_freq": cpu_freq,
        "cpu_percent": cpu_percent,
        "cpu_color": cpu_color
    }
