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

def possible(i):
	

with open('Problem 23 Abundent Numbers.txt') as f:
    content = f.read().splitlines()

for i in range(1, 28123):
	if possible(i) == false:
		sum += i

print (sum)