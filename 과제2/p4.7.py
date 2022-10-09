import random

a = random.randint(1,100)
b = random.randint(1,100)

num = int(input("숫자를 입력하세요:" ))

if num == a+b:
    print("정답입니다.")
else:
    print("정답은", a+b,"입니다")

