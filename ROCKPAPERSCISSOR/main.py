from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Initialize global variables for score tracking
user_score = 0
computer_score = 0
WIN_POINTS = 3
LOSE_POINTS = 0
DRAW_POINTS = 1

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Game logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

@app.route("/", methods=["GET", "POST"])
def index():
    global user_score, computer_score

    result = None
    user_choice = None
    computer_choice = None

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)
        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += WIN_POINTS
            result = "You Win!"
        elif winner == "computer":
            computer_score += WIN_POINTS
            result = "You Lose!"
        else:
            # Tie case: Points are shared
            user_score += DRAW_POINTS
            computer_score += DRAW_POINTS
            result = "It's a Tie!"

    return render_template(
        "index.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        user_score=user_score,
        computer_score=computer_score
    )

@app.route("/reset")
def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
