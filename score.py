from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 200)
        self.write(":", align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.left_paddle_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_paddle_score, align="center", font=("Courier", 80, "normal"))


    def add_points_to(self, paddle):
        if paddle == "left":
            self.left_paddle_score += 1
            self.update_score()
        if paddle == "right":
            self.right_paddle_score += 1
            self.update_score()


