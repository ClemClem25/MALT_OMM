import subprocess
import sys
import os
import pyautogui
import time

# Lien chemin vers le fichier .osexp
experiment_file = r'C:\OMMEntryPoint.osexp'

# Vérification de l'existence du fichier
if not os.path.exists(experiment_file):
    print(f"Le fichier {experiment_file} n'existe pas.")
    sys.exit(1)

# Chemin vers l'exécutable OpenSesame
openSesame_path = r'C:\Program Files (x86)\OpenSesame\Scripts\opensesame.exe'

# Ouvre le fichier .osexp avec OpenSesame
try:
    process = subprocess.Popen([openSesame_path, experiment_file])
    
    # Attendre quelques secondes pour permettre à OpenSesame d'ouvrir le fichier
    time.sleep(10)
    
    # Simuler la pression de CTRL+R pour démarrer l'expérience
    pyautogui.hotkey('ctrl', 'r')
    
    print(f"L'expérience {experiment_file} est maintenant en cours d'exécution.")
    
    # Attendre que l'interface se charge avant d'appuyer sur Entrée
    time.sleep(2)  # Attendre un peu plus longtemps si nécessaire
    
    # Simuler la pression de la touche "Entrée" une première fois
    pyautogui.press('enter')
    
    # Attendre un peu avant de simuler la seconde pression
   
    
    
    # Simuler la pression de la touche "Entrée" une deuxième fois après la flèche gauche
    time.sleep(2)
    pyautogui.press('enter')
    
    time.sleep(3)  # Attendre un peu plus longtemps si nécessaire
     # Simuler la pression de la flèche gauche
    pyautogui.press('left')
    time.sleep(2)
    
    pyautogui.press('enter')

except Exception as e:
    print(f"Erreur lors du lancement de l'expérience : {e}")
    sys.exit(1)
