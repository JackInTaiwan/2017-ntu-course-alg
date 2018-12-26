import random



c, e = 1000, 80000

print (str(c) + " " + str(e))

count = 0
record = []
while count < e :
    c1, c2 = random.randint(1, c), random.randint(1, c)
    if (c1, c2) not in record and (c2, c1) not in record and c1 != c2 :
        count += 1
        record.append((c1, c2))
        print (str(c1) + " " + str(c2))
