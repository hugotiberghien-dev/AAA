# Challenge Triple A - Dashboard de Monitoring

## Description
Outil de monitoring système avec dashboard web affichant en temps réel les statistiques d'une machine virtuelle Linux. Ce projet combine trois compétences : Administration système, Algorithmique Python et Affichage web (HTML/CSS).

## Prérequis
- Ubuntu Desktop 22.04 LTS ou version plus récente
- Python 3
- Bibliothèque psutil
- Navigateur web (Firefox, Chrome)

## Installation
```bash
# Mettre à jour les paquets
sudo apt update

# Installer pip si nécessaire
sudo apt install python3-pip -y

# Installer psutil
pip3 install psutil --break-system-packages
```

## Utilisation
```bash
# Lancer le script de monitoring
python3 monitor.py

# Ouvrir le dashboard dans le navigateur
firefox index.html
```

## Fonctionnalités
- **Informations système** : Nom de la machine, OS, uptime, utilisateurs connectés
- **Monitoring CPU** : Nombre de cœurs, fréquence, pourcentage d'utilisation
- **Monitoring RAM** : RAM utilisée/totale avec barre de progression
- **Monitoring Disque** : Espace utilisé/total avec barre de progression
- **Réseau** : Adresse IP principale
- **Top 3 processus** : Processus les plus gourmands en ressources
- **Analyse de fichiers** : Comptage des fichiers .txt, .py, .pdf, .jpg avec pourcentages

## Captures d'écran
![Dashboard](screenshots/index.png)
![Terminal](screenshots/terminal.png)

## Difficultés rencontrées


## Améliorations possibles
- Ajout du rafraîchissement automatique (meta refresh 30s)
- Gauges graphiques pour l'affichage des pourcentages
- Analyse de fichiers approfondie avec plus d'extensions
- Charge système moyenne (load average)
- Mode sombre / clair

## Auteur
Hugo / Louis / Matis - La Plateforme 2025