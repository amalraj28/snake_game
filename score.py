from turtle import Turtle
ALIGN = 'center'
STYLE = ('Arial', 18, 'italic')
COLOR = 'white'


class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(0, 260)
        self.points = 0
        with open('data.txt', 'r') as file:
            self.high = int(file.read())
        self.color(COLOR)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.points}  High Score: {self.high}', font=STYLE, align=ALIGN)

    # def game_over(self):
    #     self.home()
    #     self.write('GAME OVER!', font=STYLE, align=ALIGN)

    def reset(self):
        if self.points > self.high:
            with open('data.txt', 'w') as file:
                self.high = self.points
                file.write(str(self.high))
        self.points = 0
        self.update_score()

    def increment_score(self):

        self.points += 1
        self.update_score()
