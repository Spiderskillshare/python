
def pri(num):
	lists = []
	while num > 0:
		lists.append(num)
		num -= 1
	return lists
numb = int(input("enter a positive the number: "))
count = 0
if numb > 0:
	
	for word in pri(numb):
		check = numb % word

		if check == 0:
			count += 1

if count == 2:
	print(str(numb) + " is a prime number")
else:
	print(str(numb) + " is not a prime number")
