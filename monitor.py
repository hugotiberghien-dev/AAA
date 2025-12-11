"""
Challenge Triple A
Collecte informations système et génère dashboard HTML
"""

import psutil
import platform
import socket
import os
from datetime import datetime

# FONCTIONS UTILITAIRES

def get_size_gb(bytes_value):
    """Convertit les bytes en GB"""
    return round(bytes_value / (1024 ** 3), 2)


def get_color_class(percent):
    """Retourne la classe CSS selon le pourcentage"""
    if percent <= 50:
        return "green"
    elif percent <= 80:
        return "orange"
    else:
        return "red"


# FONCTIONS DE COLLECTE DE DONNÉES

def get_system_info():
    
    # Nom machine
    hostname = socket.gethostname()
    
    # SE
    os_name = f"{platform.system()} {platform.release()}"
    
    # Uptime
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_delta = datetime.now() - boot_time
    hours, remainder = divmod(int(uptime_delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime = f"{hours}h {minutes}m {seconds}s"
    
    # Utilisateurs co
    user_count = len(psutil.users())
    
    return {
        "hostname": hostname,
        "os_name": os_name,
        "uptime": uptime,
        "user_count": user_count
    }


def get_cpu_info():
    
    # Nb de cœurs
    cpu_cores = psutil.cpu_count(logical=True)
    
    # Fréquence CPU
    cpu_freq_info = psutil.cpu_freq()
    cpu_freq = round(cpu_freq_info.current, 2) if cpu_freq_info else "N/A"
    
    # % utilisation 
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Classe couleur
    cpu_color = get_color_class(cpu_percent)
    
    return {
        "cpu_cores": cpu_cores,
        "cpu_freq": cpu_freq,
        "cpu_percent": cpu_percent,
        "cpu_color": cpu_color
    }


def get_memory_info():
    
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


def get_disk_info():
    
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


def get_network_info():
    """Récup IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        ip_address = "Non disponible"
    
    return {"ip_address": ip_address}


def get_top_processes(n=3):
    """Récupère top processus les plus gourmands"""
    processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            proc_info = proc.info
            processes.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Fonction pour calculer le score de "gourmandise" d'un processus
    def calculer_score(processus):
        cpu = processus['cpu_percent']
        ram = processus['memory_percent']
        
        # Si la valeur est None, on utilise 0 à la place
        if cpu is None:
            cpu = 0
        if ram is None:
            ram = 0
        
        return cpu + ram
    
    # Trier par CPU + RAM combinés (du plus gourmand au moins gourmand)
    processes.sort(key=calculer_score, reverse=True)
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


def analyze_files(directory=None):
    """Analyse les fichiers .txt, .py, .pdf, .jpg d'un répertoire"""
    if directory is None:
        directory = os.path.expanduser("~/Documents")
    
    # Vérifie que le dossier existe
    if not os.path.exists(directory):
        directory = os.path.expanduser("~")
    
    # Extensions demandées par le sujet
    extensions = {'.txt': 0, '.py': 0, '.pdf': 0, '.jpg': 0}
    
    total_files = 0
    
    # Parcours RÉCURSIF du répertoire
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if not file.startswith('.'):
                    total_files += 1
                    _, ext = os.path.splitext(file.lower())
                    if ext in extensions:
                        extensions[ext] += 1
    except PermissionError:
        pass
    
    # Calcul des pourcentages
    html = f"<p>Répertoire analysé : {directory}</p>"
    html += f"<p>Total : {total_files} fichiers</p>"
    html += "<ul>"
    
    for ext, count in extensions.items():
        if total_files > 0:
            percent = round((count / total_files) * 100, 1)
        else:
            percent = 0
        html += f'<li><span class="ext-name">{ext}</span> <span class="ext-count">{count} fichiers ({percent}%)</span></li>'
    
    html += "</ul>"
    
    return {"file_stats": html}

# GÉNÉRATION DU HTML

def generate_html():
    """Génère le fichier index.html"""
    
    print("Challenge Triple A - Monitoring System")
    print("\nCollecte des données système...")
    
    # Collecter toutes les données
    data = {}
    data["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    print("  → Informations système...")
    data.update(get_system_info())
    
    print("  → Informations CPU...")
    data.update(get_cpu_info())
    
    print("  → Informations mémoire...")
    data.update(get_memory_info())
    
    print("  → Informations disque...")
    data.update(get_disk_info())
    
    print("  → Informations réseau...")
    data.update(get_network_info())
    
    print("  → Top processus...")
    data.update(get_top_processes())
    
    print("  → Analyse des fichiers...")
    data.update(analyze_files())
    
    # Lire le template
    try:
        with open("template.html", "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print("\n Erreur : template.html introuvable !")
        return
    
    # Remplacer les variables
    for key, value in data.items():
        template = template.replace("{{ " + key + " }}", str(value))
    
    # Écrire le fichier généré
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(template)
    
    print("\n" + "=" * 50)
    print(f" index.html généré avec succès !")
    print(f" {data['timestamp']}")
    print("=" * 50)
    print("\nOuvrez index.html dans votre navigateur pour voir le dashboard.")

# POINT D'ENTRÉE

if __name__ == "__main__":
    generate_html()