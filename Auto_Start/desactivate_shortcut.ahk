#Persistent  ; Cela permet au script de rester en exécution
SetTimer, CheckFullScreen, 500  ; Vérifie toutes les 500ms si la fenêtre est en plein écran

; Définir les raccourcis à l'avance pour simuler l'action du tactile
*~a::
    MsgBox, A pressé !
    return

*~b::
    MsgBox, B pressé !
    return

CheckFullScreen() {
    static shortcutsDisabled := false
    WinGet, activeWindowID, ID, A
    WinGetPos, x, y, width, height, ahk_id %activeWindowID%
    
    ; Vérifie si la fenêtre est en plein écran
    if (width == A_ScreenWidth && height == A_ScreenHeight) {
        if (!shortcutsDisabled) {
            ; Désactive les raccourcis spécifiques pour empêcher le retour en arrière
            Hotkey, *~a, Off
            Hotkey, *~b, Off
            
            ; Bloquer les actions comme ALT+TAB et WIN+TAB pour éviter de quitter l'écran plein
            Hotkey, *^Tab, Off
            Hotkey, *#Tab, Off
            
            ; Empêche les actions tactiles de glissement ou de "swipe"
            BlockInput, MouseMove ; Empêche de déplacer la souris
            BlockInput, MouseClick ; Empêche les clics souris (peut être ajusté si besoin)

            shortcutsDisabled := true
        }
    } else {
        if (shortcutsDisabled) {
            ; Réactive les raccourcis spécifiques
            Hotkey, *~a, On
            Hotkey, *~b, On

            ; Réactive les raccourcis comme ALT+TAB et WIN+TAB
            Hotkey, *^Tab, On
            Hotkey, *#Tab, On

            ; Réactive les mouvements de la souris et les clics
            BlockInput, Off

            shortcutsDisabled := false
        }
    }
}
