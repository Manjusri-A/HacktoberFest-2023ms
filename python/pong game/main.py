from turtle import Screen, Turtle
from paddle import Paddle, Boundary
from ball import Ball
from scoreboard import Scoreboard
import time

# Initialize the turtle and screen
turtle = Turtle()
screen = Screen()

# Get points from the user and ensure it's an integer
points = screen.textinput(prompt="Kitne Points ka Khelega?", title="Batao bhaiii")
try:
    points = int(points)  # Convert input to an integer
except (ValueError, TypeError):
    print("Invalid input! Using default points: 5.")
    points = 5  # Default value if input is invalid

# Set up the screen
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles, ball, and scoreboard
paddle = Boundary()
paddle.boundary()

ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Listen for key presses
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

# Game loop
while is_game_on:
    time.sleep(0.05)  # Control the speed of the game
    screen.update()
    ball.move()

    # Check if any player has won
    if scoreboard.l_score > points or scoreboard.r_score > points:
        is_game_on = False
        turtle.color("white")
        turtle.hideturtle()
        turtle.write("Game Over", align="center", font=("Courier", 80, "normal"))

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # R_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # L_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Exit the game on click
screen.exitonclick()
