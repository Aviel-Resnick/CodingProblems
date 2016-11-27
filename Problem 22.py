import re

total = 0

file = open('/home/avilor/Desktop/Project Euler/Problem 22 Names.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
names = list(text.split())
names.sort()

for i in range(0,len(names)):
	current_name = names[i]
	value = 0
	for x in range(0,len(current_name)):
		current_letter = ord(current_name[x]) - 96
		value = value + current_letter
	names[i] = value * (i + 1)
	total = total + names[i]

print(total)