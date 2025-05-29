import turtle
from turtle import Turtle, Screen
import time
import math
import random

last_drag_time = time.time()
dragging_now = False

cumulative_error = 0
num_error = 0

top_scores = []

# Set up the screen
screen = Screen()
screen.bgcolor("#f0f8ff")
screen.title("Draw a Perfect Circle Game")

# Add a turtle for writing the score
score_writer = Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 150)
score_writer.color("#ef1220")

# Add a turtle for motivational messages
message_writer = Turtle()
message_writer.hideturtle()
message_writer.penup()
message_writer.goto(0, 120)
message_writer.color("#32cd94")

# Add a turtle for the guide circle (with glow effect)
guide = Turtle()
guide.hideturtle()
guide.penup()
guide.goto(0, 0)
guide.pencolor("gray")
guide.pensize(8)
guide.setheading(0)
guide.goto(0, -100)
guide.pendown()
guide.speed(0)
for _ in range(36):
    guide.pendown()
    guide.circle(100, 5)
    guide.penup()
    guide.circle(100, 5)
guide.penup()
guide.pensize(2)
guide.pencolor("lightgray")
guide.goto(0, -100)
guide.pendown()
guide.circle(100)
guide.penup()

# Add a turtle for the title
title_writer = Turtle()
title_writer.hideturtle()
title_writer.penup()
title_writer.goto(0, 180)
title_writer.color("#333333")
title_writer.write("Try to draw a perfect circle!", align="center", font=("Arial", 18, "bold"))

# Add this near the top, after your imports:
top_scores = []

# Add this after your other turtles in main_game_setup():
global top_scores_writer
top_scores_writer = Turtle()
top_scores_writer.hideturtle()
top_scores_writer.penup()
top_scores_writer.goto(0, -170)
top_scores_writer.color("#ffff00")  # Bright yellow

def get_motivation(score):
    if score > 95:
        return "Thats deacent 🤷‍♂️"
    elif score > 90:
        return "Get 95 or else 💯"
    elif score > 80:
        return "My grandma can do better than you 👵🏻"
    elif score > 60:
        return "Do better or I will nuke your house 👋"
    else:
        return "You're so fat you cant even reach the keyboard ⬅️➡️ "

def update_score():
    score_writer.clear()
    message_writer.clear()
    if num_error > 0:
        score = cumulative_error / num_error
        score_writer.write(f"Score: {round(score, 1)}", align="center", font=("Arial", 18, "bold"))
        message_writer.write(get_motivation(score), align="center", font=("Arial", 16, "italic"))
    else:
        score_writer.write("Score: 0.0", align="center", font=("Arial", 18, "bold"))

def dragging(x, y):
    global last_drag_time, dragging_now, cumulative_error, num_error
    t.ondrag(None)
    t.goto(x, y)
    t.ondrag(dragging)
    last_drag_time = time.time()
    dragging_now = True

    radius = math.sqrt(x*x + y*y)
    acc = 100 - abs(100 - radius)
    cumulative_error += acc
    num_error += 1

def reset_circle():
    global cumulative_error, num_error, top_scores
    if num_error > 0:
        score = cumulative_error / num_error
        top_scores.append(score)
        top_scores = sorted(top_scores, reverse=True)[:3]  # Keep top 3
    update_score()  # Show the score after the circle is done
    show_top_scores()  # Show top 3 scores

    # Play a beep sound (if available)
    try:
        import winsound
        winsound.Beep(800, 150)
    except:
        pass

    # Clear the score and message after 3 seconds (3000 ms)
    screen.ontimer(clear_score, 3000)

    cumulative_error = 0
    num_error = 0
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.dot(12, "#39ff14")  # Neon green dot
    t.goto(0, 100)
    t.pendown()
    # Change to a random neon color for the next circle
    t.color(random.choice([
        "#ff00cc", "#00ffe7", "#39ff14", "#ffff00", "#ff3131", "#fffb00", "#00ffea"
    ]))

def clear_score():
    score_writer.clear()
    message_writer.clear()

def show_top_scores():
    top_scores_writer.clear()
    if top_scores:
        scores_text = "Top Scores: " + ", ".join(str(round(s, 1)) for s in top_scores)
        top_scores_writer.goto(0, -170)
        top_scores_writer.write(scores_text, align="center", font=("Arial", 16, "bold"))

def check_drag_end():
    global last_drag_time, dragging_now
    current_time = time.time()
    if current_time - last_drag_time > 0.2 and dragging_now:
        dragging_now = False
        reset_circle()
    screen.ontimer(check_drag_end, 100)

# --- Start Screen Setup ---
def show_start_screen():
    screen.clear()
    screen.bgcolor("black")  # Black background for start screen
    start_writer = Turtle()
    start_writer.hideturtle()
    start_writer.penup()
    start_writer.goto(0, 60)
    start_writer.color("#00ffe7")  # Neon cyan
    start_writer.write("Draw a Perfect Circle", align="center", font=("Arial", 32, "bold"))
    start_writer.goto(0, 10)
    start_writer.color("#ffffff")  # White
    start_writer.write("Try to follow the guide and draw a perfect circle\nwith your mouse!", align="center", font=("Arial", 18, "normal"))
    start_writer.goto(0, -60)
    start_writer.color("#39ff14")  # Neon green
    start_writer.write("Click anywhere to start", align="center", font=("Arial", 20, "bold"))
    return start_writer

def start_game(x=None, y=None):
    screen.clear()
    main_game_setup()

def main_game_setup():
    global score_writer, message_writer, guide, title_writer, t
    screen.bgcolor("black")  # Black background for main game

    # Reinitialize turtles and variables
    score_writer = Turtle()
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.goto(0, 150)
    score_writer.color("#00ffe7")  # Neon cyan

    message_writer = Turtle()
    message_writer.hideturtle()
    message_writer.penup()
    message_writer.goto(0, 120)
    message_writer.color("#39ff14")  # Neon green

    guide = Turtle()
    guide.hideturtle()
    guide.penup()
    guide.goto(0, 0)
    guide.pencolor("#4444ff")  # Bright blue for glow
    guide.pensize(8)
    guide.setheading(0)
    guide.goto(0, -100)
    guide.pendown()
    guide.speed(0)
    for _ in range(36):
        guide.pendown()
        guide.circle(100, 5)
        guide.penup()
        guide.circle(100, 5)
    guide.penup()
    guide.pensize(2)
    guide.pencolor("#8888ff")  # Lighter blue for main guide
    guide.goto(0, -100)
    guide.pendown()
    guide.circle(100)
    guide.penup()

    title_writer = Turtle()
    title_writer.hideturtle()
    title_writer.penup()
    title_writer.goto(0, 180)
    title_writer.color("#ffffff")  # White
    title_writer.write("Try to draw a perfect circle!", align="center", font=("Arial", 18, "bold"))

    # Reset game variables
    global cumulative_error, num_error
    cumulative_error = 0
    num_error = 0

    # Drawing turtle
    t = Turtle()
    t.shape("circle")
    t.color("#ff00cc")  # Neon pink
    t.pensize(4)
    t.speed(0)

    reset_circle()
    t.ondrag(dragging)
    check_drag_end()

# Show start screen and wait for click
start_writer = show_start_screen()
screen.onclick(start_game)
screen.mainloop()
