# Step 1: pip install --upgrade openai

from openai import OpenAI

# Step 2: Initialize the OpenAI client with your API key
client = OpenAI(api_key="your-api-key-here")  # 🔑 Replace this with your real key

def chat_with_gpt():
    print("ChatGPT: Ask me anything (type 'exit' to quit).")
    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("ChatGPT: Bye!")
            break

        messages.append({"role": "user", "content": user_input})

        # Step 3: Use the correct client call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("ChatGPT:", reply)
        messages.append({"role": "assistant", "content": reply})

chat_with_gpt()
