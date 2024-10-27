import logging
from pynput.keyboard import Listener, Key, KeyCode
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import sys

# File to store the logs
log_file = "key_log.txt"
# Define the exit key combination: Ctrl + Shift + X
exit_combination = {Key.ctrl_l, Key.shift, KeyCode(char='x')}
current_keys = set()
# Function to start the keylogger
def start_keylogger():
    # Set up logging configuration
    logging.basicConfig(filename=log_file,level=logging.DEBUG,format='%(asctime)s: %(message)s')

    # Function to log key presses
    def log_key(key):
        global current_keys
        # Log key presses
        try:
            key_data = str(key.char)  # Handle character keys
        except AttributeError:
            # Handle special keys
            if key == Key.space:
                key_data = " [SPACE] "
            elif key == Key.enter:
                key_data = " [ENTER]\n"
            elif key == Key.backspace:
                key_data = " [BACKSPACE] "
            else:
                key_data = f" [{str(key).replace('Key.', '').upper()}] "

        # Write key data to the log file
        logging.info(key_data)

        # Check if the key is part of the exit combination
        if key in exit_combination:
            current_keys.add(key)
            # If all keys in the exit combination are pressed, stop the keylogger
            if all(k in current_keys for k in exit_combination):
                return False  # Stop the listener

    # Function to track key releases and update `current_keys`
    def release_key(key):
        try:
            current_keys.remove(key)
        except KeyError:
            pass

    # Start a new session log
    with open(log_file, "a") as f:
        f.write(f"\n\n---- New Session Started at {datetime.now()} ----\n\n")

    # Start listening for key presses and releases
    with Listener(on_press=log_key, on_release=release_key) as listener:
        listener.join()
    
    # Exit the program when the listener stops
    sys.exit()

# Function to show a permission pop-up
def request_permission():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show messagebox asking for permission
    user_response = messagebox.askyesno("Permission Request", "Do you agree to use this keylogger for logging your keystrokes?")

    # If the user agrees, start the keylogger
    if user_response:
        start_keylogger()
    else:
        messagebox.showinfo("Goodbye", "Keylogger will not start without permission.")
        root.quit()  # Exit the program if permission is denied

# Request permission to use the keylogger
request_permission()