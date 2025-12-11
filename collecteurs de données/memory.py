def get_memory_info():
    """Récupère les informations mémoire"""
    memory = psutil.virtual_memory()
    
    ram_total = get_size_gb(memory.total)
    ram_used = get_size_gb(memory.used)
    ram_percent = memory.percent
    ram_color = get_color_class(ram_percent)
    
    return {
        "ram_total": ram_total,
        "ram_used": ram_used,
        "ram_percent": ram_percent,
        "ram_color": ram_color
    }