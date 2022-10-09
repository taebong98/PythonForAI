import turtle

t = turtle.Turtle()
t.shape("turtle")

s1 = turtle.textinput("", "왼족 하단 모서리 좌표 x,y: ").split(",")
s2 = turtle.textinput("", "오른쪽 상단 모서리 좌표 x,y: ").split(",")

x1, y1 = map(int, s1)
x2, y2 = map(int, s2)

print("x1:",x1)
print("x2:",x2)


t.forward(x2-x1)
t.left(90)
t.forward(y2-y1)
t.left(90)
t.forward(x2-x1)
t.left(90)
t.forward(y2-y1)


s3 = turtle.textinput("", "임의의 점 x,y를 입력하세요: ").split(",")
x3, y3 = map(int, s3)
t.penup()
t.goto(x3, y3)
t.dot(30)

if x3*y3 < (x2-x1)*(y2-y1):
    print("점은 사각형 내부에 있습니다.")
else:
    print("점은 사각형 외부에 있습니다.")
