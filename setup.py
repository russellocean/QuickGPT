from setuptools import setup

APP = ['quickgpt.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pynput', 'pyautogui', 'pyperclip', 'openai'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
