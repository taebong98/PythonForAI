import random
num1 = random.randint(1,9)
num2 = random.randint(1,9)
num3 = random.randint(1,9)

lotto = []
lotto.append(num1)
lotto.append(num2)
lotto.append(num3)
# print("lotto",lotto)

inputStr = input("세 복권번호를 입력하세요: ").split(" ")
myNum = []
for n in inputStr:
    myNum.append(int(n))

print("mynum: ",myNum)

cnt = 0
for x in myNum:
    if x in lotto:
        cnt +=1

if cnt == 3:
    print("1억원")
elif cnt == 2:
    print("1천만원")
elif cnt == 1:
    print("1만원")
else:
    print("다음 기회에...")