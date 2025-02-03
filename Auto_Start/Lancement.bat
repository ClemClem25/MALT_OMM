@echo off
:: Vérifie si le script est déjà exécuté en mode administrateur
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Demande d'elevation des privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs"
    exit
)

:: Chemin vers Python et ton script
set PYTHON_PATH="C:\Program Files (x86)\OpenSesame\pythonw.exe"
set SCRIPT_PATH="C:\Users\Admin\Desktop\Start_OS_XP.py"

:: Exécute le script Python
%PYTHON_PATH% %SCRIPT_PATH%
exit
