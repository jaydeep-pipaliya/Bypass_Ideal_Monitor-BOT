import pyautogui
import time
from pynput import mouse, keyboard
from datetime import datetime
import json

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

last_activity_time = time.time()
LOG_FILE = "/tmp/idle_monitor_log.json"

def on_activity(*args):
    global last_activity_time
    last_activity_time = time.time()

def perform_action():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width // 2, 0, duration=0.5)
    pyautogui.moveRel(0, 5, duration=0.1)
    pyautogui.moveRel(0, -5, duration=0.1)
    pyautogui.press('shift')
    pyautogui.click(button='left')
    log_action("Awake function called")

def log_action(message):
    now = datetime.now()
    log_entry = {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%I:%M:%S %p"),
        "message": message
    }
    try:
        with open(LOG_FILE, "r") as f:
            log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        log = []
    log.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(log, f)

def main():
    global last_activity_time
    idle_threshold = 2 * 60  # 2 minutes in seconds
    action_interval = 2  # 2 seconds
    mouse_listener = mouse.Listener(on_move=on_activity, on_click=on_activity, on_scroll=on_activity)
    keyboard_listener = keyboard.Listener(on_press=on_activity, on_release=on_activity)
    mouse_listener.start()
    keyboard_listener.start()

    try:
        while True:
            idle_time = time.time() - last_activity_time
            if idle_time >= idle_threshold:
                while time.time() - last_activity_time >= idle_threshold:
                    perform_action()
                    time.sleep(action_interval)
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped by user.")
    finally:
        mouse_listener.stop()
        keyboard_listener.stop()

if __name__ == "__main__":
    main()