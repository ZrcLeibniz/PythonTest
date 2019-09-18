import turtle

my_colors = ['red', 'yellow', 'green', 'blue', 'pink', 'red', 'yellow', 'green', 'blue', 'pink']
t = turtle.Pen()
t.width(5)
for x in range(10, 101, 10):
    t.penup()
    t.color(my_colors[x // 10 - 1])
    t.goto(0, 5 - x)
    t.pendown()
    t.circle(x)
turtle.done()
