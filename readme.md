#  ChatGPT API for Continuous Dialogue Therapist Implementation

This project utilizes the OpenAI ChatGPT API to implement continuous dialogue with users. It automatically translates Korean user inputs into English for processing, and then translates the model's responses back into Korean for presentation.

## Installation

To use this project, Python must be installed on your system. Additionally, you need to install the necessary libraries by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

Before running the project, you must set your OpenAI API key in the environment variable `OPENAI_API_KEY`. After setting up the API key, you can start a conversation by running the script:

```bash
python therapist_main.py
```

## Features

- **Language Detection and Translation**: Automatically translates Korean user inputs to English, and the model's English responses back to Korean.
- **Continuous Dialogue**: Maintains the context of the conversation, allowing for a continuous dialogue experience.
- **Token Usage Tracking**: Tracks the token usage of the API requests for efficient usage of the OpenAI API.

## License

This project is distributed under the MIT License.
