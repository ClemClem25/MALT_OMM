#Persistent
SetTimer, CheckFullScreen, 500
return

CheckFullScreen:
    WinGet, Style, Style, A
    if (Style & 0x80000000) { ; Vérifie si la fenêtre active est en plein écran
        BlockTouchGestures(true)
    } else {
        BlockTouchGestures(false)
    }
return

BlockTouchGestures(Block) {
    static gestureKeys := ["LWin", "RWin", "LAlt", "Tab", "Escape", "LControl", "RControl"]
    
    Loop, % gestureKeys.MaxIndex()
    {
        key := gestureKeys[A_Index]
        if (Block)
            Hotkey, %key%, DisableKey, On
        else
            Hotkey, %key%, DisableKey, Off
    }
    return
}

DisableKey:
    return
