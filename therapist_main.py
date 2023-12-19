import openai
import os
import re

total_tokens_used = 0


def estimate_token_count(text):
    return len(text) // 4


def update_total_tokens(estimated_tokens):
    global total_tokens_used
    total_tokens_used += estimated_tokens


def is_korean(text):
    return bool(re.search("[가-힣]", text))


def translate_text(text, target_language, model="gpt-3.5-turbo-1106"):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    translation_prompt = f"Translate the following text to {target_language}:\n\n{text}"
    response = openai.Completion.create(
        model=model,
        prompt=translation_prompt,
        max_tokens=60
    )

    translated_text = response.choices[0].text.strip()
    estimated_tokens = estimate_token_count(translation_prompt + translated_text)
    update_total_tokens(estimated_tokens)

    return translated_text


def chat_with_gpt(messages, model="gpt-4", stop_sequences=None):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    request_data = {
        "model": model,
        "messages": messages,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 1,
        "stop": stop_sequences
    }

    response = openai.ChatCompletion.create(**request_data)
    response_text = response.choices[0].message["content"]

    messages.append({"role": "assistant", "content": response_text})
    estimated_tokens = estimate_token_count(response_text)
    update_total_tokens(estimated_tokens)

    return response_text, messages


messages = [{"role": "system", "content": "You are a compassionate and knowledgeable therapist.Listen carefully and provide thoughtful, empathetic responses."}]
user_input = ""
print("Hello! How are you feeling today?")

while True:
    user_input = input("You: ")

    original_language = "Korean" if is_korean(user_input) else "English"
    if original_language == "Korean":
        user_input = translate_text(user_input, "English")

    messages.append({"role": "user", "content": user_input})

    english_response, messages = chat_with_gpt(messages, stop_sequences=["Thank you", "End"])

    if original_language == "Korean":
        response = translate_text(english_response, "Korean")
    else:
        response = english_response

    print("Assistant:", response)

    if "Thank you" in user_input or "End" in user_input:
        break

print(f"Total estimated tokens used so far: {total_tokens_used}")