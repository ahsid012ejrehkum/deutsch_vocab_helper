import csv
import random

def load_vocab(filename="vocab.csv"):
    words = []
    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                german = row.get("german", "").strip()
                english = row.get("english", "").strip()
                if german and english:
                    words.append({"german": german, "english": english})
    except FileNotFoundError:
        print(f"Error: {filename} not found. Make sure it is in the same folder as vocab_quiz.py.")
    return words

def ask_questions(words, num_questions=5):
    if not words:
        print("No vocab loaded. Exiting.")
        return

    score = 0
    asked = 0

    num_questions = min(num_questions, len(words))
    questions = random.sample(words, num_questions)

    print("Willkommen zum Deutsch-Vokabel-Quiz! 🎓")
    print(f"I'll ask you {num_questions} words.\n")

    for entry in questions:
        german_word = entry["german"]
        correct_answer = entry["english"]

        print(f"What is the meaning of: **{german_word}** ?")
        user_answer = input("Your answer (in English): ").strip().lower()

        if user_answer == correct_answer.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Not quite. Correct answer: {correct_answer}\n")

        asked += 1

    print(f"Quiz finished! You scored {score} / {asked}.")

def main():
    words = load_vocab("vocab.csv")
    ask_questions(words, num_questions=5)

if __name__ == "__main__":
    main()
