import time
import random



a = [1,2,3,4]
print ([2,4] in a)
print (17.9//3)
a = a[2:] + a[0:2]
print (a)
x = [random.choice([2,3,4,5,6,7,8,9,10]) for _ in range(10*100)]
print (x)

print ("Whether to go to class : %s " % random.choice([True, False]))
for i in range(0) :
    print (";;")