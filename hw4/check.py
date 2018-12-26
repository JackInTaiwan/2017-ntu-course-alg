c, e = input().split()
c, e = int(c) , int(e)
adj_dict = {}

for i in range(1, c+1) :
    adj_dict[i] = []
for _ in range(e) :
    c1, c2 = input().split()
    c1, c2 = int(c1), int(c2)
    adj_dict[c1].append(c2)
    adj_dict[c2].append(c1)

total = input()
cities = input()
chosen_cities = cities.split()
chosen_cities = [int(item) for item in chosen_cities]

for city in chosen_cities :
    for adj in adj_dict[city] :
        adj_dict[adj].remove(city)

error = False
for city in adj_dict :
    if city not in chosen_cities and len(adj_dict[city]) > 0 :
        error = True
        break
if error == True :
    print ("Error")
else :
    print ("Success!")