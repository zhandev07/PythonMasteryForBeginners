import os
import json
import random
import time
import pygame
from playsound import playsound

# Global settings
HIGH_SCORE_FILE = "high_scores.json"
USER_PROFILE_FILE = "user_profile.json"
CORRECT_SOUND = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/projects_for_beginers/QuizApp/sound/correct.wav"
WRONG_SOUND = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/projects_for_beginers/QuizApp/sound/wrong.wav"
TIME_LIMIT = 30  # Set time limit for each question in seconds

# Functions to load questions from file
def load_questions():
    if os.path.exists("questions.json"):
        with open("questions.json", "r") as file:
            return json.load(file)
    return []

# Functions to save questions to file
def save_questions(questions):
    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)

# Functions to load high scores
def load_high_scores():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return json.load(file)
    return {}

# Functions to save high scores
def save_high_scores(scores):
    with open(HIGH_SCORE_FILE, "w") as file:
        json.dump(scores, file, indent=4)

# Functions to load the user profile
def load_user_profiles():
    if os.path.exists(USER_PROFILE_FILE):
        with open(USER_PROFILE_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save the user profile
def save_user_profiles(profiles):
    with open(USER_PROFILE_FILE, 'w') as file:
        json.dump(profiles, file, indent=4)

# Function to add a new question
def add_questions(questions):
    try:
        category = input("Enter the category of the question (e.g., Math, Science): ").strip()
        question_text = input("Enter the quiz question: ").strip()
        question_type = input("Is this a multiple-choice (M) or true/false (T) question? ").strip().upper()
        difficulty = input("Enter difficulty (easy, medium, hard): ").strip().lower()

        if question_type == 'M':
            choices = []
            for i in range(4):
                choice = input(f"Enter choice{i+1}: ").strip()
                choices.append(choice)
            correct_choice = int(input("Which choice is correct? (Enter the number 1-4) ").strip()) - 1
            question = {
                "category": category,
                "question": question_text,
                "type": "multiple_choice",
                "choices": choices,
                "correct": correct_choice,
                "difficulty": difficulty
            }
        elif question_type == 'T':
            correct_choice = input("Is the statement True or False (T/F)? ").strip().upper()
            if correct_choice not in ['T', 'F']:
                raise ValueError("Invalid input. Enter 'T' for True or 'F' for False statement!")
            question = {
                "category": category,
                "question": question_text,
                "type": "true_false",
                "correct": 'T' if correct_choice == 'T' else 'F',
                "difficulty": difficulty
            }
        else:
            raise ValueError("Invalid question type. Please choose 'M' for Multiple choice or 'T' for True/False!")

        questions.append(question)
        save_questions(questions)
        print("Question added successfully")
    except ValueError as e:
        print(f"Error: {e}")

# Functions to view all questions
def view_questions(questions):
    if not questions:
        print("No questions yet. Please add questions")
    else:
        for idx, q in enumerate(questions):
            print(f"Question {idx + 1}: {q['question']}")
            if q['type'] == "multiple_choice":
                for i, choice in enumerate(q['choices']):
                    print(f"  {i + 1}. {choice}")
            print(f"Category: {q['category']}, Difficulty: {q['difficulty']}")
            print("-" * 40)

# Functions to select difficulty level
def select_difficulty():
    difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid choice, defaulting to easy.")
        return 'easy'
    return difficulty

# Function to select a quiz category
def select_category(questions):
    categories = list(set([q['category'] for q in questions]))
    if not categories:
        print("No categories available.")
        return None
    print("Available categories:", ", ".join(categories))
    selected_category = input("Choose a category or 'all' for all categories: ").strip()
    if selected_category.lower() != 'all' and selected_category not in categories:
        print("Invalid category. Defaulting to all categories.")
        return None
    return selected_category

# Function to take the quiz
def take_quiz(questions, username):
    if not questions:
        print("No questions available for the quiz!")
        return

    category = select_category(questions)
    difficulty = select_difficulty()

    # Filter questions by selected category and difficulty
    filtered_questions = [
        q for q in questions
        if q['difficulty'] == difficulty and (category is None or q['category'] == category)
    ]

    if not filtered_questions:
        print(f"No questions available for {difficulty} difficulty!")
        return

    score = 0
    random.shuffle(filtered_questions)  # Shuffle questions for random order
    start_time = time.time()  # Start time tracking
    total_time_taken = 0

    for idx, q in enumerate(filtered_questions):
        print(f"Question {idx + 1}: {q['question']}")
        question_start_time = time.time()

        if q['type'] == "multiple_choice":
            for i, choice in enumerate(q["choices"]):
                print(f"  {i + 1}. {choice}")
            try:
                answer = int(input("Your answer (Enter the number): ").strip()) - 1
                if answer == q["correct"]:
                    print("✅ Correct!")
                    playsound(CORRECT_SOUND)  # Play sound for correct
                    score += 1
                else:
                    print(f"❌ Wrong answer! The correct answer was {q['choices'][q['correct']]}")
                    playsound(WRONG_SOUND)  # Play sound for wrong answer
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif q['type'] == "true_false":
            answer = input("Your answer (T/F): ").strip().upper()
            if answer == q["correct"]:
                print("✅ Correct!")
                playsound(CORRECT_SOUND)  # Play sound for correct
                score += 1
            else:
                print(f"❌ Wrong answer! The correct answer was {'True' if q['correct'] == 'T' else 'False'}")
                playsound(WRONG_SOUND)  # Play sound for wrong answer

        print("-" * 40)

        # Enforce time limit per question
        question_end_time = time.time()
        time_taken_for_question = question_end_time - question_start_time
        total_time_taken += time_taken_for_question

        if time_taken_for_question > TIME_LIMIT:
            print(f"⏰ Time's up! You took too long to answer this question.")

        print("-" * 40)

    print(f"Quiz finished! Your final score is {score}/{len(filtered_questions)}")
    print(f"Total Time Taken: {total_time_taken:.2f} seconds")

    update_high_scores(username, score, total_time_taken)

 # Option to return to menu or repeat the quiz
    while True:
        choice = input("Do you want to (R)epeat the quiz or (M)ain menu? ").strip().upper()
        if choice == 'R':
            take_quiz(questions, username)  # Repeat the quiz
            break
        elif choice == 'M':
            break
        else:
            print("Invalid choice. Please choose again.")
            
# Function to update high scores
def update_high_scores(username, score, time_taken):
    high_scores = load_high_scores()

    if username not in high_scores:
        high_scores[username] = {"score": score, "time": time_taken}
    else:
        # Update score if better, or if equal score and faster time
        current_high = high_scores[username]
        if score > current_high["score"] or (score == current_high["score"] and time_taken < current_high["time"]):
            high_scores[username] = {"score": score, "time": time_taken}

    save_high_scores(high_scores)

# Function to view high scores leaderboard
def view_high_scores():
    high_scores = load_high_scores()
    if not high_scores:
        print("No high scores available.")
    else:
        sorted_scores = sorted(high_scores.items(), key=lambda x: (-x[1]['score'], x[1]['time']))
        print("\nLeaderboard:")
        for user, data in sorted_scores:
            print(f"{user}: {data['score']} points, {data['time']:.2f} seconds")

# Function to view user profiles
def view_user_profiles():
    profiles = load_user_profiles()
    if not profiles:
        print("No user profiles available.")
    else:
        print("\nUser Profiles:")
        for user, data in profiles.items():
            print(f"Username: {user}, Quizzes Taken: {data['quizzes_taken']}")

# Function to handle user login/signup
def user_login():
    profiles = load_user_profiles()
    username = input("Enter your username: ").strip()
    if username in profiles:
        print(f"Welcome back, {username}!")
    else:
        profiles[username] = {"quizzes_taken": 0}
        print(f"Profile created for {username}!")

    profiles[username]['quizzes_taken'] += 1
    save_user_profiles(profiles)
    return username

# Function to exit the app
def exit_app():
    confirmation = input("Are you sure you want to exit the app? (Y/N): ").strip().upper()
    if confirmation == 'Y':
        print("Exiting the app. Goodbye!")
        exit()
    else:
        print("Returning to the main menu.")

# Main menu function
def main_menu():
    while True:
        print("\n--- Quiz App ---")
        print("1. Take Quiz")
        print("2. Add Questions")
        print("3. View Questions")
        print("4. View High Scores")
        print("5. View User Profiles")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            username = user_login()
            questions = load_questions()
            take_quiz(questions, username)
        elif choice == "2":
            questions = load_questions()
            add_questions(questions)
        elif choice == "3":
            questions = load_questions()
            view_questions(questions)
        elif choice == "4":
            view_high_scores()
        elif choice == "5":
            view_user_profiles()
        elif choice == "6":
            exit_app()
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main_menu()
