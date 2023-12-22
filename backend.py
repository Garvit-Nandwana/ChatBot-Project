import openai


class ChatBot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input, model="gpt-3.5-turbo", tokens=3000):
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {
                    'role': 'user', 'content': user_input
                }
            ],
            max_tokens=tokens,
            temperature=0.5)

        return response.choices[0].message.content


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response(user_input="Hello")
    print(response)
