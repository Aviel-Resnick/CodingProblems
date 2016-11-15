num = 2 ** 1000
str_num = str(num)

length = len(str_num)

total_sum = 0

for i in range(0,length):
    total_sum = total_sum + int(str_num[i])

print(total_sum)
