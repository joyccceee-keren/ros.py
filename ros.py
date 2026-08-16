import turtle

# Setup screen and turtle
screen = turtle.Screen()
screen.title("Interactive Turtle Spiral Generator")
screen.bgcolor("black")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.hideturtle()

# Define color themes
THEMES = {
    "Neon Pink": ["pink", "hotpink", "deeppink", "palevioletred"],
    "Ocean Blue": ["cyan", "deepskyblue", "dodgerblue", "royalblue"],
    "Forest Green": ["lime", "limegreen", "forestgreen", "springgreen"],
    "Rainbow": ["red", "orange", "yellow", "green", "blue", "purple"]
}
theme_names = list(THEMES.keys())
current_theme_idx = 0

def draw_spiral():
    # Disable tracing temporarily to draw instantly or fast
    screen.tracer(0)
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    
    colors = THEMES[theme_names[current_theme_idx]]
    # Update title with current theme info
    screen.title(f"Turtle Spiral - Theme: {theme_names[current_theme_idx]} (Press SPACE to change theme, Q to quit)")
    
    # Draw the spiral
    for x in range(150):
        t.color(colors[x % len(colors)])
        t.circle(x)
        t.left(30)
    
    # Update the screen with the finished drawing
    screen.update()

def next_theme():
    global current_theme_idx
    current_theme_idx = (current_theme_idx + 1) % len(theme_names)
    draw_spiral()

def quit_app():
    screen.bye()

# Bind controls
screen.listen()
screen.onkey(next_theme, "space")
screen.onkey(quit_app, "q")
screen.onscreenclick(lambda x, y: next_theme())

# Initial draw
draw_spiral()

# Start main loop
turtle.done()