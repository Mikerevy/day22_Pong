from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super(Paddle, self).__init__()
        self.create_a_paddle()
        self.goto(x_position, y_position)

    def create_a_paddle(self):
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor()
        new_y += 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()
        new_y -= 40
        self.goto(self.xcor(), new_y)





# class Paddle:
#     def __init__(self, x_position, y_position):
#         self.create_a_paddle()
#         self.paddle.goto(x_position, y_position)
# 
#     def create_a_paddle(self):
#         self.paddle = Turtle("square")
#         self.paddle.color("green")
#         self.paddle.penup()
#         self.paddle.shapesize(stretch_wid=5, stretch_len=1)
# 
# 
#     def up(self):
#         new_y = self.paddle.ycor()
#         new_y += 40
#         self.paddle.goto(self.paddle.xcor(), new_y)
# 
#     def down(self):
#         new_y = self.paddle.ycor()
#         new_y -= 40
#         self.paddle.goto(self.paddle.xcor(), new_y)
# 



# # Create a paddle
# paddle = Turtle("square")
# paddle.color("green")
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(350, 0)
#
#
# def up():
#     new_y = paddle.ycor()
#     new_y += 40
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def down():
#     new_y = paddle.ycor()
#     new_y -= 40
#     paddle.goto(paddle.xcor(), new_y)

