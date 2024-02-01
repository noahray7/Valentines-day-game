import time

def love_story_game():
    print("Welcome to Our Love Story Game!")
    time.sleep(1)
    print("Let's take a journey through the beautiful moments we've shared.")

    questions = [
        "1. Where did we have our first date?",
        "2. On which date did we officially start dating?",
        "3. Who usually cooks for the other person?",
        "4. Where did we celebrate our first Christmas together?",
        "5. What do I believe about you?",
        "6. What's one thing I love doing for you?",
        "7. Finish the sentence: 'You are the most ______ girl in the world.'",
        "8. What's the ultimate goal in our relationship?",
    ]

    answers = [
        "movies",
        "december 26",
        "you do",
        "at your grandmas",
        "you are the most beautiful girl in the world",
        "everything",
        "beautiful",
        "get married",
    ]

    score = 0

    for i, question in enumerate(questions, 1):
        user_answer = input(f"{question} ")
        user_answer = user_answer.lower().strip()

        if user_answer == answers[i - 1]:
            print("Correct!")
            score += 1
        else:
            print("Oops, that's not right. Let's move on.")

        time.sleep(1)

    print("\nGame Over! Let's see how well you know our love story.")
    print(f"You got {score} out of {len(questions)} questions right.")

    if score == len(questions):
        print("Congratulations! You know our love story inside out. I love you!")
    else:
        print("Even if you missed a few, every moment with you is special. I love you!")

    print("\nHere are the correct answers:")
    for i, (question, answer) in enumerate(zip(questions, answers), 1):
        print(f"{i}. {question} Answer: {answer}")

if __name__ == "__main__":
    love_story_game()
