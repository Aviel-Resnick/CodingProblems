##l = []
##l.append("75")
##l.append("95 64")
##l.append("17 47 82")
##l.append("18 35 87 10")
##l.append("20 04 82 47 65")
##l.append("19 01 23 75 03 34")
##l.append("88 02 77 73 07 63 67")
##l.append("99 65 04 28 06 16 70 92")
##l.append("41 41 26 56 83 40 80 70 33")
##l.append("41 48 72 33 47 32 37 16 94 29")
##l.append("53 71 44 65 25 43 91 52 97 51 14")
##l.append("70 11 33 28 77 73 17 78 39 68 17 57")
##l.append("91 71 52 38 17 14 91 43 58 50 27 29 48")
##l.append("63 66 04 68 89 53 67 30 73 16 69 87 40 31")
##l.append("04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

l = []
l.append("3")
l.append("7 4")
l.append("2 4 6")
l.append("8 5 9 3")

t = []
test = 0
for i in range(0,4):
    temp = []
    str_group = l[i]
    temp = str_group.split()
    
    for x in range(0, len(temp)):
        num = temp[x]
        t.append(num)
        test = test + 1
        
print(test)

for i in range(-4,-1):
    abs_i = abs(i)
    row1_str = l[abs_i - 2]
    row2_str = l[abs_i - 1]
  
    row1 = row1_str.split()
    row2 = row2_str.split()
    
    for x in range (0, len(row1)):
        current_num_row1 = row1[x]
        current_num_row2_1 = row2[x]
        current_num_row2_2 = row2[x+1]
        if current_num_row2_1 > current_num_row2_2:
            t[abs_i * (x + 1) + 3] = current_num_row1 + current_num_row2_1
        else:
            current_num_row1 = current_num_row1 + current_num_row2_2
