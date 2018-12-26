### Input load
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



### Initialize
adj_num_list = [0 for _ in range(c+1)]
for i in range(1,c+1) :
    adj_num_list[i] = len(adj_dict[i])

all_nodes = {}  #if covered, it carries True
for i in range(1, c+1) :
    all_nodes[i] = False

chosen_nodes = []
covered_nodes = []



### Size = 0
"""
candidates = [i for i in range(1, c+1) if adj_num_list[i] == 0]
for node in candidates :
    all_nodes[node] = True
    chosen_nodes.append(node)
    covered_nodes.append(node)
"""
city_0 = len([i for i in range(1, c+1) if adj_num_list[i] == 0])



### Size = 1, choose its adj
def find_size_1 () :
    candidates_size_1 = [i for i in range(1, c+1) if adj_num_list[i] == 1]
    for node in candidates_size_1 :
        if all_nodes[node] == False :
            #print(all_nodes[node])
            all_nodes[node] = True
            covered_nodes.append(node)
            adj = None
            for item in adj_dict[node] :
                if all_nodes[item] == False :
                    adj = item
            if adj == None : print ("none", node)
            if all_nodes[adj] == False :
                all_nodes[adj] = True
                covered_nodes.append(adj)
                chosen_nodes.append(adj)
                for adj_adj in adj_dict[adj] :
                    if all_nodes[adj_adj] == False :
                        if adj_num_list[adj_adj] == 1 :
                           all_nodes[adj_adj] = True
                           covered_nodes.append(adj_adj)
                        else :
                           adj_num_list[adj_adj] -= 1
                if len(covered_nodes) == (c - city_0) :
                    return True
    return False



### Iteration
max_size = max(adj_num_list)
size = max_size
while len(covered_nodes) < (c - city_0) :
    if find_size_1() == False :
        candidates = [i for i in range(1,c+1) if adj_num_list[i] == size]
        for node in candidates :
            if adj_num_list[node] == size and all_nodes[node] == False :
                all_nodes[node] = True
                chosen_nodes.append(node)
                covered_nodes.append(node)
                for adj in adj_dict[node] :
                    if all_nodes[adj] == False :
                        if adj_num_list[adj] != 1 :
                            adj_num_list[adj] -= 1
                        else :
                            all_nodes[adj] = True
                            covered_nodes.append(adj)

                if len(covered_nodes) == (c - city_0) :
                    break
    size -= 1

print (len(chosen_nodes))
ans = ""
for i in sorted(chosen_nodes) :
    ans = ans + str(i) + " "
print (ans[0:-1])