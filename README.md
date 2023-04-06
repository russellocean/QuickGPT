# OpenAI Question Answering Assistant

This project is a simple question-answering assistant that captures selected text and fetches an answer from OpenAI's GPT-4 model. The answer is copied to your clipboard, making it easy to paste and use.

## Setup and Installation

### Prerequisites

- Python 3.x
- OpenAI API key

### Installation

1. Clone the repository or download the project files:

```
git clone https://github.com/russellocean/QuickAI.git
```

2. Change into the project directory:
```
cd your_repository
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

1. Set your OpenAI API key as an environment variable or directly in the script:

```
export OPENAI_API_KEY="your_api_key"
```

Alternatively, you can replace `OPENAI_API_KEY` in the script with your actual API key:

```python
OPENAI_API_KEY = "your_api_key"
```
## Usage
1. Run the script:
   ```python
   python openai_question_answering.py
   ```
2. The application will print instructions:
    ```
    Application running.
    Press ctrl+alt+c to process the selected text and get an answer.
    ```
3. Select the text you want to process and press ctrl+c to copy the selected text.
4. Press ctrl+alt+c to process the selected text, fetch an answer from OpenAI, and copy the answer to your clipboard.
5. Press ctrl+v to paste the answer wherever you need it.
## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
