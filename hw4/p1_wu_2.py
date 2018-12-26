c,r=input().split()
c,r=int(c),int(r)
cities=[]
connect=[]
count=0
print_order=[]
friend=dict()
check=[]
count_zero=0
for i in range(c):
    cities.append(i+1)
    connect.append(0)
    check.append(0)
    friend[i+1]=[]
for i in range(r):
    a,b=input().split()
    a,b=int(a),int(b)
    connect[a-1]+=1
    connect[b-1]+=1
    friend[a].append(b)
    friend[b].append(a)
for i in range(len(connect)):
    if connect[i]==0:
        count_zero+=1
#print(count_zero)
#rint(friend)
#print(cities)
while count_zero != c:
    #print(count_zero)
    #print(connect)
    maxi=max(connect)
    first=cities[connect.index(maxi)]
    check[first-1]=1
    connect[first-1]=0
    count+=1
    count_zero+=1
    for i in range (len(friend[first])):
        if connect[friend[first][i]-1]!=0:
            connect[friend[first][i]-1]-=1
            if connect[friend[first][i]-1]==0:
                count_zero+=1
        #print(friend)
        #print(connect)

    #print(friend)
#print(connect)
print(count)
for i in range(len(check)):
    if check[i]!=0:
        print_order.append(cities[i])
print(" ".join(str(i) for i in print_order))
