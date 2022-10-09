num = int(input("세자리 정수를 입력하세요: ") )
print("백의자리: ", num//100)
print("십의자리: ", round((num%100 - num%10)/10 ))
print("일의자리: ", num%10)
