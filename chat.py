import random


def chatbot():
    print("Hi, I'm a chatbot! What's your name?")
    name = input()

    greetings = ["Hi", "Hello", "Hey", "Nice to meet you"]
    print(f"{random.choice(greetings)}, {name}! How are you feeling today?")

    feelings = ["happy", "sad", "excited", "tired", "angry"]
    user_feeling = input().lower()

    if user_feeling in feelings:
        if user_feeling == "happy":
            print("That's great to hear!")
        elif user_feeling == "sad":
            print("I'm sorry to hear that. Is there anything I can do to help?")
        elif user_feeling == "excited":
            print("That's awesome!")
        elif user_feeling == "tired":
            print("You should get some rest.")
        elif user_feeling == "angry":
            print("Take a deep breath and try to relax.")
    else:
        print("I'm sorry, I don't understand that feeling.")

    print("Do you have any other questions for me?")
    response = input().lower()

    if "yes" in response:
        print("What would you like to know?")
        question = input()
        print("I'm sorry, I don't know the answer to that.")
    else:
        print("It was nice talking to you. Goodbye!")


chatbot()
