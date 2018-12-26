a = input()
a_1 = a.split()
c = int(a_1[0])
r = int(a_1[1])
neigh = [[] for i in range(c)]
# neigh_num=[0 for i in range(c)]
neigh_num = {}
for i in range(c):
    neigh_num[i] = 0
list = {}
vertex_num = c
vertex_choose = []
# print(r)

for i in range(r):
    c1 = input()
    c_1 = c1.split()
    neigh[int(c_1[0]) - 1].append(int(c_1[1]) - 1)
    neigh[int(c_1[1]) - 1].append(int(c_1[0]) - 1)
    neigh_num[int(c_1[0]) - 1] += 1
    neigh_num[int(c_1[1]) - 1] += 1
max_nei = max(neigh_num, key=lambda x: neigh_num.get(x))
max_value = neigh_num[max_nei]
# print(neigh,neigh_num)
# list=[1, 5,2,2,1]
# maxIndex, maxValue = max(enumerate(list), key=lambda v: v[1])
# print(max(neigh_num.keys(), key=(lambda k: neigh_num[k])))
# print(neigh_num,max_nei)

while max_value > 0:
    '''
    for i in range(len(vertex)-1,-1,-1):
        if neigh_num[vertex[i]]==1 and neigh_num[neigh[vertex[i]][0]]==2:
            vertex_choose.append(neigh[vertex[i]])
            neigh_num[neigh[vertex[i]][0]]-=1
            del vertex[i]
        print(vertex,neigh_num)
    '''
    del_list = []
    for key, value in neigh_num.items():
        # print(neigh_num,neigh,key)
        if value == 1:
            if neigh_num[neigh[key][0]] == 2 or neigh_num[neigh[key][0]] == 1:
                i1 = key
                i2 = neigh[key][0]
                while True:
                    # print(neigh_num,neigh,i2,i1)
                    neigh[i2].remove(i1)
                    neigh_num[i1] = 0
                    neigh_num[i2] = 0
                    del_list.append(i1)
                    del_list.append(i2)
                    vertex_choose.append(i2 + 1)
                    if len(neigh[i2]) > 0:
                        nei_i2 = neigh[i2][0]
                        neigh[nei_i2].remove(i2)
                        neigh_num[nei_i2] -= 1


                    else:
                        break
                    # del neigh_num[i1]
                    # del neigh_num[i2]

                    i1 = nei_i2
                    if neigh_num[i1] == 1 and (neigh_num[i2] == 2 or neigh_num[i2] == 1):
                        i2 = neigh[i1][0]
                        # print(i1,i2)
                    else:
                        break
    # print(del_list)
    for i in del_list:
        del neigh_num[i]

    if len(neigh_num) != 0:
        max_nei = max(neigh_num, key=lambda x: neigh_num.get(x))

        # max_nei, _ = max(neigh_num.iteritems(), key=lambda x:x[1])
        # print(max_nei,maxValue)
        if neigh_num[max_nei] > 0:
            del neigh_num[max_nei]
            for i in neigh[max_nei]:
                neigh_num[i] -= 1
                neigh[i].remove(max_nei)
            # neigh_num[max_nei]=0
            vertex_choose.append(max_nei + 1)
        max_nei = max(neigh_num, key=lambda x: neigh_num.get(x))
        max_value = neigh_num[max_nei]
    else:
        max_value = 0

        # print(neigh_num,neigh)
        # max_value=max(neigh_num.keys(), key=(lambda k: neigh_num[k]))
        # print(max_value)

print(len(vertex_choose))
x = sorted(vertex_choose)

print(*x)
# print(neigh,neigh_num)
