import turtle


# Draw a circle out of a square
def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    # Draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    # Draw a circle
    # angie = turtle.Turtle()
    # angie.color("blue")
    # angie.shape("arrow")
    # angie.circle(100)

    window.exitonclick()


draw_art()
