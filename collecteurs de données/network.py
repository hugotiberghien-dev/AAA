def get_network_info():
    """Récupère l'adresse IP principale"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        ip_address = "Non disponible"
    
    return {"ip_address": ip_address}