from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self) -> object:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ Create the 'snake' at the starting position"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """ Add a segment to the 'snake' """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """ Reset snake to the starting size and position"""
        # loop through segments to move them off the screen so they disappear
        for seg in self.segments:
            seg.goto(1200, 1200)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """ Add a segment to the 'snake' """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Move the 'snake' forward in it's current heading with 
        non-head segments following the head segment """
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ Move the snake up as long as it's not currently going down """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ Move the snake down as long as it's not currently going up """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ Move the snake left as long as it's not currently going right """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ Move the snake right as long as it's not currently going left """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
