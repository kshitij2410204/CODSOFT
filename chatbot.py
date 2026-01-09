print("Welcome to CodSoft Chatbot")
print("Type 'bye' to exit")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine. Hope you are doing well!")

    elif user_input == "your name":
        print("Bot: I am a Rule-Based Chatbot created for CodSoft Internship.")

    elif user_input == "help":
        print("Bot: You can say hi, ask my name, or type bye to exit.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
