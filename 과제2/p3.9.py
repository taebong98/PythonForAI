import math


speed = float(input("평균 시속을 입력하세요: "))
hour = float(input("이동시간을 입력하세요: "))

a = int(hour)
b = int((hour-a)*60)
c = int(((hour-a)*60 - b)*60)
print(c)
print("평균시속 : ", speed,"km/h")
print("이동시간 : ", a,"시간", b,"분",c, "초")
print("이동거리 : ", speed * hour, "km")
