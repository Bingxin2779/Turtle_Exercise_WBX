#科赫雪花
import turtle as t
def koch(lenth,n):
    if n == 0:
        t.fd(lenth)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(lenth/3,n-1)       

def main():
    t.setup(1200,800,0,0)
    #t.penup()
    #t.fd(300)
    #t.pendown()
    t.pensize(3)
    level=3
    size=300
    koch(size,level)
    t.right(120)
    koch(size,level)
    t.right(120)
    koch(size,level)
    t.hideturtle()

main()
