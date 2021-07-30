def pow(num, powe):
	answer = 1
	for numb in range(powe):
		answer *= num
	return answer
num = int(input("enter num: "))
powe = int(input("enter power: "))
print(pow(num, powe))
