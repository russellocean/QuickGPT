# QuickGPT

QuickGPT is a powerful question-answering assistant that captures selected text and fetches answers from OpenAI's GPT-4 model using langchain, a framework for developing applications powered by language models. It connects the language model to other sources of data, such as Google searches and Wolfram Alpha, and allows the model to interact with its environment. The answer is copied to your clipboard, making it easy to paste and use.

## Setup and Installation

### Prerequisites

- Python 3.x
- OpenAI API key
- Google Serp API key
- Wolfram Alpha App ID

### Installation

1. Clone the repository or download the project files:

```
git clone https://github.com/russellocean/QuickGPT.git
```

2. Change into the project directory:
```
cd QuickGPT
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

4. Set your API keys and App ID as environment variables:

```bash
export OPENAI_API_KEY="your_openai_api_key"
export SERPER_API_KEY="your_google_serp_api_key"
export WOLFRAM_ALPHA_APPID="your_wolfram_alpha_app_id"
```
Alternatively, you can replace the corresponding variables in the agent_utils.py script with your actual API keys and App ID:

```python
OPENAI_API_KEY = "your_openai_api_key"
SERPER_API_KEY = "your_google_serp_api_key"
WOLFRAM_ALPHA_APPID = "your_wolfram_alpha_app_id"
```

## Usage

1. Run the script:
   ```python
   python quickgpt.py
   ```
2. The application will print instructions:
   ```
   Application running.
   Press ctrl+alt+c to process the selected text and get an answer.
   ```
3. Select the text you want to process and press ctrl+c to copy the selected text.

4. Press ctrl+alt+c to process the selected text, fetch an answer from OpenAI using langchain's enhanced functionality, and copy the answer to your clipboard.

5. Press ctrl+v to paste the answer wherever you need it.
