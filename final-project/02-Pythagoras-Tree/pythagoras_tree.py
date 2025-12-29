import turtle


def draw_tree(t, branch_len, level, max_level):
    """
    Recursive function to draw the fractal tree.

    Args:
        t: The turtle object.
        branch_len: Length of the current branch.
        level: Current recursion depth.
        max_level: Total recursion depth (used for color calculation).
    """
    # Base case: if level is 0, stop drawing
    if level == 0:
        return

    # Set pen width based on the current level (thicker at the bottom)
    t.width(level * 1.5)

    # Color logic: Interpolate from brown to green based on level
    # Calculate a ratio: 1.0 is the trunk, 0.0 is the tip
    ratio = level / max_level

    # Simple color mixing logic (RGB)
    # Brown-ish: (139, 69, 19) -> Green-ish: (50, 205, 50)
    r = int(50 + (139 - 50) * ratio)
    g = int(205 + (69 - 205) * ratio)
    b = int(50 + (19 - 50) * ratio)

    t.pencolor(r, g, b)

    # Draw the branch
    t.forward(branch_len)

    # Right branch
    t.right(30)
    draw_tree(t, branch_len * 0.75, level - 1, max_level)

    # Left branch (rotate 60 to the left to compensate for the previous 30 right)
    t.left(60)
    draw_tree(t, branch_len * 0.75, level - 1, max_level)

    # Restore orientation
    t.right(30)

    # Restore color and width for the backward journey
    # (crucial so the parent branch doesn't get repainted with child attributes)
    t.width(level * 1.5)
    t.pencolor(r, g, b)

    # Return to the starting position of this branch
    t.penup()
    t.backward(branch_len)
    t.pendown()


def main():
    # Screen setup
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    screen.bgcolor("black")  # Dark background makes colors pop
    screen.colormode(255)  # Use RGB 0-255 mode
    # Turn off animation for instant results (crucial for high levels)
    screen.tracer(0)

    # Setup the turtle
    pen = turtle.Turtle()
    pen.speed(0)  # Fastest speed
    pen.hideturtle()

    # Position the turtle at the bottom center
    pen.left(90)
    pen.penup()
    pen.goto(0, -250)
    pen.pendown()

    # Get user input for recursion level via a popup window
    try:
        level = int(screen.numinput("Recursion Level",
                                    "Enter depth (recommended 7-12):",
                                    default=9, minval=1, maxval=15))
    except TypeError:
        # Handle case where user presses Cancel
        level = 9

    # Start drawing
    # Initial branch length is 150 pixels
    draw_tree(pen, 150, level, level)

    # Keep the window open
    screen.mainloop()


if __name__ == "__main__":
    main()