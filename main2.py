import turtle

window = turtle.Screen()
window.bgcolor('dark salmon')

t = turtle.Turtle()
t.shape('turtle')
t.color('turquoise')
t.penup()

def change_color():
  t.color('light green')
  
def move_left():
  t.left(10)
  
def move_right():
  t.right(10)
  
def move_forward():
  t.forward(10)
  
def move_back():
  t.back(10)
  
def pen_down():
  t.pendown()
  
window.onkeypress(move_forward, "Up")
window.onkeypress(move_back, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(pen_down, "space")



window.listen()
  
turtle.done()