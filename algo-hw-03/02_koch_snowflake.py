import turtle


CANVAS_SIZE: int = 1000 # To fit FullHD screens

def koch_curve(t, order, size) -> None:
    """
    Recursive function to draw one side of the snowflake.

    :param t: turtle object
    :param order: current recursion level (depth)
    :param size: length of the line
    """
    if order == 0:
        # Base case: draw a straight line
        t.forward(size)
    else:
        # Recursive step: divide the line into 4 segments
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


def draw_snowflake(t, order, size):
    """Draws the full snowflake using three Koch curves."""
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def main():
    # --- Screen setup ---
    screen = turtle.Screen()
    screen.setup(width=CANVAS_SIZE, height=CANVAS_SIZE)
    screen.bgcolor("#000022")  # Dark blue background (night sky)
    screen.title("Fractal: Koch Snowflake")

    # --- Get user input ---
    # Use the turtle window for input
    try:
        level = int(screen.numinput("Settings",
                                    "Enter recursion level (recommended 0-5):",
                                    default=3, minval=0, maxval=7))
    except TypeError:
        # If the user clicked Cancel
        level = 3

    # --- Pen setup ---
    pen = turtle.Turtle()
    pen.hideturtle()  # Hide the turtle cursor
    pen.speed(0)  # Max animation speed
    pen.width(2)  # Line width

    # Colors: (outline, fill)
    pen.color("#00FFFF", "#003366")

    # --- Positioning ---
    # Move the turtle so the snowflake is centered
    size = CANVAS_SIZE / 2
    pen.penup()
    pen.goto(-size / 2, size / 3)
    pen.pendown()

    # --- Drawing ---
    print(f"Drawing snowflake level {level}...")

    # Turn off animation for instant results (crucial for high levels)
    screen.tracer(0)

    pen.begin_fill()
    draw_snowflake(pen, level, size)
    pen.end_fill()

    # Update the screen after drawing is complete
    screen.update()

    print("Done! Click the window to exit.")
    screen.exitonclick()


if __name__ == "__main__":
    main()