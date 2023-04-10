import os
from pynput import keyboard
import pyautogui as pya
import pyperclip
import time
import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Read the content from ai_prompt.txt and store it in AI_PROMPT
with open("ai_prompt.txt", "r") as f:
    AI_PROMPT = f.read().strip()

def capture_selected_text():
    pya.hotkey('cmd', 'c')
    time.sleep(.01)  # cmd-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def fetch_answer_from_openai(prompt, model="gpt-4", messages=None, temperature=0.5, max_tokens=2000):
    print(f"Sending prompt to OpenAI: {prompt}")

    if messages is None:
        messages = [
            {"role": "system", "content": AI_PROMPT},
            {"role": "user", "content": prompt},
        ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    result = response['choices'][0]['message']['content'].strip()
    print(f"OpenAI response: {result}")
    return result

def on_process_hotkey():
    selected_text = capture_selected_text()
    print(f'Selected text: {selected_text}')
    answer = fetch_answer_from_openai(selected_text)
    pyperclip.copy(answer)
    print("Answer copied to clipboard. Press ctrl+v to paste.")

with keyboard.GlobalHotKeys({'<ctrl>+<alt>+c': on_process_hotkey}) as hotkeys_listener:
    print('Application running.')
    print('Press ctrl+alt+c to process the selected text and get an answer.')

    # Keep the script running and waiting for hotkeys
    while True:
        time.sleep(1)