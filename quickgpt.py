from pynput import keyboard
import pyautogui as pya
import pyperclip
import time

# Import the ask_agent function from agent_utils module
from agent_utils import ask_agent

def capture_selected_text():
    # Copy selected text to clipboard using keyboard shortcut
    pya.hotkey('cmd', 'c')
    time.sleep(.01)  # cmd-c is usually very fast but your program may execute faster
    # Return the content of the clipboard
    return pyperclip.paste()

def on_process_hotkey():
    # Capture the selected text
    selected_text = capture_selected_text()
    print(f'Selected text: {selected_text}')

    # Fetch answer using the ask_agent function
    answer = ask_agent(selected_text)

    # Copy the answer to the clipboard
    pyperclip.copy(answer)
    print("Answer copied to clipboard. Press ctrl+v to paste.")

# Set up hotkeys and listener
with keyboard.GlobalHotKeys({'<ctrl>+<alt>+c': on_process_hotkey}) as hotkeys_listener:
    print('Application running.')
    print('Press ctrl+alt+c to process the selected text and get an answer.')

    # Keep the script running and waiting for hotkeys
    while True:
        time.sleep(1)