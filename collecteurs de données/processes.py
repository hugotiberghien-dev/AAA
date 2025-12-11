def get_top_processes(n=3):
    """Récupère le top N des processus les plus gourmands"""
    processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            proc_info = proc.info
            processes.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Trier par CPU + RAM combinés
    processes.sort(key=lambda x: (x['cpu_percent'] or 0) + (x['memory_percent'] or 0), reverse=True)
    top_procs = processes[:n]
    
    # Générer le HTML
    html = "<ul>"
    for proc in top_procs:
        name = proc['name'] or "Inconnu"
        cpu = round(proc['cpu_percent'] or 0, 1)
        mem = round(proc['memory_percent'] or 0, 1)
        html += f"<li><strong>{name}</strong> - CPU: {cpu}% | RAM: {mem}%</li>"
    html += "</ul>"
    
    return {"top_processes": html}