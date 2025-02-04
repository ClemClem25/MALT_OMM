#Persistent
SetTimer(CheckFullScreen, 500)

CheckFullScreen() {
    static shortcutsDisabled := false
    WinGetStyle, style, "A"
    
    if (style & 0x80000000) { ; Vérifie si la fenêtre active est en plein écran
        if (!shortcutsDisabled) {
            Hotkey "*~", "Off"
            shortcutsDisabled := true
        }
    } else {
        if (shortcutsDisabled) {
            Hotkey "*~", "On"
            shortcutsDisabled := false
        }
    }
}
