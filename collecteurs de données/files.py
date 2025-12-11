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