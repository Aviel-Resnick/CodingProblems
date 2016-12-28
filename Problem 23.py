#abundent_group = open("Problem 23 Abundent Numbers.txt", "w")

def sum_divisors(num):
	sum = 0
	for i in range(1,int(num/2) + 1):
		if num%i == 0:
			sum = sum + i
	return(sum)

#Generate list of abundent numbers
'''for x in range(1,28123):
	if sum_divisors(x) > x:
		abundent_group.write(str(x) + "\n")'''

with open('Problem 23 Abundent Numbers.txt') as f:
    content = f.read().splitlines()

copy = content

for x in range(1, len(content)-1):
	current_num = content[x-1]
	for y in range(1, len(content)-1):
		num = current_num + content[y]
		print(y, "=", content[y])
		if num not in copy:
			pass
		else:
			copy.remove(num)

print(copy)