import turtle
t=turtle.Turtle()
t.shape("turtle")



# 거북이를 100만큼 이동시킨다.
t.forward(100) # 첫번째 변


# 정삼각형을 만들기 위해 거북이를 왼쪽으로 (180-60)도 만큼 회전시킨다.
t.left(180-60)
t.forward(100) # 두 번째 변

t.left(180-60)
t.forward(100) # 세 번째 변 


# 두 개의 겹쳐진 정삼각형을 만들기 위해 거북이가 끝난 지점에서 오쪽으로 180-60 만큼 회전시킨다.
t.right(180-60)
t.forward(100)

t.right(180-60)
t.forward(100)
