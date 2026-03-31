print("Hello! I am your AI Assistant Bot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you today?")

    elif "course" in user:
        print("Bot: This course covers AI basics, programming, and problem solving.")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence, which enables machines to think and learn.")

    elif "university" in user:
        print("Bot: Our university offers various programs in technology and sciences.")

    elif "help" in user:
        print("Bot: I can answer questions about AI, courses, or university info.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I didn't understand that. Can you rephrase?")
