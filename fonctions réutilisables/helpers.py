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
