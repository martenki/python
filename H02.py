import turtle
turtle.pensize(6)
turtle.speed(1)
ekraan = turtle.Screen()
ekraan.title("olümpiarõngad - Marten")
ekraan.setup(500, 400)

turtle.pencolor("blue")
turtle.penup()
turtle.goto(-110,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("black")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("red")
turtle.penup()
turtle.goto(110,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("Yellow")
turtle.penup()
turtle.goto(-55,-55)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("green")
turtle.penup()
turtle.goto(55,-55)
turtle.pendown()
turtle.circle(50)

turtle.done()
    
