from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COLUMNS = 11
X_START = -450
X_GAP = 90
Y_START = 220
Y_GAP = 25

BRICK_HALF_W = 40   # stretch_len=4 -> 80px wide
BRICK_HALF_H = 10   # stretch_wid=0.5 -> 10px tall (+ gap for hit box)


class Box(Turtle):
    """A single brick."""

    def __init__(self, x, y, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=4, stretch_wid=0.5)
        self.goto(x, y)

    def destroy(self):
        self.hideturtle()
        self.goto(2000, 2000)


class BrickWall:
    """The full grid of bricks."""

    def __init__(self):
        self.bricks = []
        self.build()

    def build(self):
        for row, color in enumerate(COLORS):
            y = Y_START - row * Y_GAP
            for col in range(COLUMNS):
                self.bricks.append(Box(X_START + col * X_GAP, y, color))

    def remaining(self):
        return len(self.bricks)

    def check_hit(self, ball):
        """Return the brick the ball hit (and remove it), or None.
        Also bounces the ball."""
        for brick in self.bricks:
            dx = ball.xcor() - brick.xcor()
            dy = ball.ycor() - brick.ycor()
            if abs(dx) < BRICK_HALF_W + 10 and abs(dy) < BRICK_HALF_H + 10:
                if abs(dx) > BRICK_HALF_W:   # hit the side of the brick
                    ball.reflect_x()
                else:                        # hit top or bottom
                    ball.reflect_y()
                brick.destroy()
                self.bricks.remove(brick)
                return brick
        return None
