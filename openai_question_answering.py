from pynput import keyboard
import pyperclip
import time
import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def capture_selected_text():
    ctrl_c = keyboard.Controller()
    ctrl_c.press(keyboard.Key.ctrl)
    ctrl_c.press('c')
    time.sleep(0.1)
    ctrl_c.release('c')
    ctrl_c.release(keyboard.Key.ctrl)
    return pyperclip.paste()

def fetch_answer_from_openai(prompt, model="gpt-4", messages=None, temperature=0.5, max_tokens=100):
    print(f"Sending prompt to OpenAI: {prompt}")

    if messages is None:
        messages = [
            {"role": "system", "content": "You are an assistant designed to answer questions. If the question is multiple choice you will only answer with the answer. If the answer is free response you will answer with all steps, and if the question is fill in the blanks, you will only answer with the blanks."},
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