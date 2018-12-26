


#adj_dict = {1:[2,3,4,5,6], 2:[1,3,4,5], 3:[1,2,4], 4:[1,2,3], 5:[1,2,6], 6:[1,5]}



def convert_to_complementary (adj_dict, total) :
    total_set = set(range(1,total+1))
    for item in adj_dict :
        comp = total_set - set(adj_dict[item]) - set([item])
        adj_dict[item] = list(comp)
    return adj_dict


def find_clique_of_3 (adj_dict) :
    output = []
    l = len(adj_dict)
    for i in range(1, l+1-2) :
        for j in range(i+1, l+1-1) :
            for k in range(j+1, l+1) :
                if j in adj_dict[i] and k in adj_dict[i] and j in adj_dict[k] :
                    """
                    adj_dict[i].remove(k)
                    adj_dict[i].remove(j)
                    adj_dict[j].remove(i)
                    adj_dict[j].remove(k)
                    adj_dict[k].remove(i)
                    adj_dict[k].remove(j)
                    """
                    output.append([i,j,k])
    return output

def iterative_find_larger_cliques(cliques_3, adj_dict) :
    output = []
    temp = cliques_3
    while len(temp) > 0 :
        new_temp = []
        for clique in temp :
            node_first = clique[0]
            find = False
            for adj in adj_dict[node_first] :
                for node in clique :
                    if adj not in adj_dict[node] : break
                else :
                    find = True
                    break
            if find == True :
                new_node = adj
                for node in clique :
                    pass
                    #adj_dict[node].remove(new_node)
                    #adj_dict[new_node].remove(node)
                clique.append(new_node)
                new_temp.append(clique)
            else :
                output.append(clique)
        temp = new_temp
    return output

def total_size(cliques_list) :
    output = set()
    for item in cliques_list :
        output = output | set(item)
    return output

def answer(total_size) :
    total_size = sorted(list(total_size))
    return len(total_size), total_size

c, e = input().split()
c, e = int(c), int(e)
adj_dict = {}
for i in range(1, c+1) :
    adj_dict[i] = []
for _ in range(e) :
    c1, c2 = input().split()
    c1, c2 = int(c1), int(c2)
    adj_dict[c1].append(c2)
    adj_dict[c2].append(c1)

city_0 = []
city = {}
for item in adj_dict :
    if len(adj_dict[item]) > 0 :
        city[item] = adj_dict[item]
    else :
        city_0.append(item)
#print (len(city_0))
adj_dict_com = convert_to_complementary(adj_dict, c)
#print (adj_dict_com)
cliques_3 = find_clique_of_3(adj_dict_com)
#print (cliques_3)
if len(cliques_3) > 0 :
    cliques = iterative_find_larger_cliques(cliques_3, adj_dict_com)
    #print (cliques)
    total_size = total_size(cliques)
    #print (total_size)
    print (cliques[-1])
    print (set(range(1,c+1)) - set(cliques[-1]))
