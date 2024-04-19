import time
import threading
import ctypes
import keyboard
import os
import sys

class AutoClicker:
    def __init__(self, delay=None):
        self.delay = delay
        self.running = False
        self.hotkey = None

    def click(self):
        while self.running:
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
            if self.delay:
                time.sleep(self.delay)

    def start_clicking(self):
        self.running = True
        clicking_thread = threading.Thread(target=self.click)
        clicking_thread.daemon = True
        clicking_thread.start()

    def stop_clicking(self):
        self.running = False

    def set_hotkey(self, hotkey):
        self.hotkey = hotkey

    def toggle_autoclicker(self):
        if self.running:
            self.stop_clicking()
        else:
            self.start_clicking()

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def listen_for_hotkey(self):
        if self.hotkey:
            keyboard.add_hotkey(self.hotkey, self.toggle_autoclicker)
            keyboard.add_hotkey('esc', self.restart_program)
            keyboard.wait('esc')

delay_input = input("Enter delay in seconds (0 for none): ")
delay = float(delay_input) if delay_input != '0' else None

hotkey = input("Enter hotkey to start/stop autoclicker: ")

if __name__ == "__main__":
    autoclicker = AutoClicker(delay=delay)
    autoclicker.set_hotkey(hotkey)
    autoclicker.listen_for_hotkey()
