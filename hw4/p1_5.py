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



### Random function
def random(list_, i) :
    #radom_data size = 10 * 100
    random_data = [3, 9, 4, 8, 10, 2, 5, 6, 5, 6, 7, 9, 2, 10, 3, 2, 8, 5, 3, 2, 7, 6, 5, 9, 6, 6, 5, 2, 7, 2, 5, 4, 8, 7, 8, 4, 2, 8, 8, 3, 7, 8, 9, 2, 5, 6, 2, 3, 2, 2, 8, 2, 7, 2, 9, 4, 3, 10, 6, 6, 5, 5, 9, 10, 7, 2, 4, 5, 7, 6, 3, 5, 4, 2, 8, 7, 6, 10, 2, 4, 7, 6, 3, 2, 2, 5, 9, 7, 8, 3, 7, 10, 3, 10, 7, 2, 4, 4, 9, 3, 4, 4, 8, 4, 6, 4, 10, 4, 3, 6, 3, 3, 6, 9, 10, 6, 6, 8, 7, 8, 4, 5, 5, 8, 7, 4, 5, 4, 5, 8, 8, 9, 7, 10, 3, 7, 2, 2, 10, 9, 3, 3, 3, 5, 3, 2, 8, 6, 9, 7, 7, 7, 2, 4, 8, 4, 2, 4, 5, 10, 3, 10, 2, 5, 9, 6, 2, 3, 7, 6, 7, 6, 8, 6, 3, 3, 6, 3, 5, 3, 2, 2, 2, 7, 4, 4, 3, 7, 8, 6, 2, 2, 4, 9, 5, 2, 10, 3, 9, 9, 7, 7, 2, 4, 6, 4, 9, 7, 3, 5, 3, 8, 10, 7, 9, 2, 2, 6, 5, 6, 4, 3, 3, 2, 6, 2, 8, 4, 8, 2, 5, 2, 9, 9, 2, 7, 3, 3, 5, 6, 8, 7, 9, 5, 9, 4, 6, 8, 2, 9, 4, 7, 4, 9, 7, 4, 7, 8, 6, 7, 2, 6, 4, 4, 3, 8, 3, 5, 3, 10, 5, 10, 9, 9, 9, 6, 5, 9, 9, 9, 7, 5, 10, 2, 2, 4, 4, 4, 9, 4, 4, 9, 4, 6, 4, 7, 9, 7, 6, 8, 4, 5, 3, 2, 9, 5, 6, 10, 10, 7, 10, 7, 2, 10, 7, 7, 2, 6, 10, 5, 2, 2, 6, 4, 5, 3, 9, 4, 5, 6, 3, 10, 9, 6, 9, 7, 2, 9, 10, 7, 9, 9, 4, 6, 3, 5, 7, 5, 10, 3, 2, 10, 4, 5, 5, 5, 9, 10, 4, 2, 5, 3, 8, 2, 8, 5, 7, 6, 3, 2, 8, 10, 4, 10, 10, 7, 7, 5, 10, 2, 4, 7, 8, 10, 10, 8, 4, 3, 4, 3, 7, 2, 10, 5, 8, 2, 7, 6, 7, 6, 10, 8, 2, 3, 2, 8, 5, 2, 2, 7, 4, 4, 3, 9, 9, 8, 6, 10, 9, 10, 6, 3, 3, 9, 4, 4, 8, 8, 5, 7, 10, 10, 8, 6, 2, 4, 3, 8, 7, 9, 7, 4, 2, 6, 10, 6, 9, 4, 10, 8, 6, 2, 7, 10, 4, 5, 10, 4, 7, 9, 8, 10, 8, 6, 8, 3, 5, 5, 7, 9, 2, 8, 2, 2, 6, 6, 9, 8, 4, 5, 6, 3, 3, 5, 7, 2, 4, 8, 5, 9, 8, 3, 9, 4, 8, 4, 2, 7, 6, 10, 5, 7, 5, 7, 10, 4, 3, 8, 10, 2, 2, 4, 10, 10, 10, 6, 2, 8, 6, 3, 10, 7, 8, 6, 8, 6, 8, 3, 10, 2, 10, 7, 4, 8, 10, 5, 9, 8, 5, 10, 6, 8, 8, 5, 10, 9, 8, 10, 2, 8, 4, 4, 3, 7, 5, 2, 7, 6, 6, 5, 2, 3, 9, 3, 6, 6, 9, 2, 6, 9, 6, 2, 8, 7, 8, 5, 3, 5, 2, 7, 8, 8, 6, 4, 8, 10, 2, 10, 10, 5, 7, 8, 3, 7, 2, 5, 9, 5, 9, 9, 2, 10, 10, 10, 2, 6, 7, 6, 6, 5, 3, 4, 9, 5, 8, 2, 6, 10, 9, 2, 2, 4, 6, 4, 9, 3, 4, 6, 6, 4, 9, 2, 8, 8, 9, 8, 8, 6, 6, 5, 7, 3, 4, 4, 2, 8, 8, 3, 7, 3, 9, 9, 9, 10, 8, 7, 4, 6, 9, 10, 2, 6, 9, 10, 2, 7, 5, 8, 5, 9, 5, 2, 2, 9, 3, 9, 5, 7, 4, 5, 7, 3, 6, 8, 2, 2, 3, 7, 8, 9, 6, 4, 9, 8, 6, 5, 6, 7, 6, 8, 6, 7, 6, 8, 7, 4, 3, 9, 6, 8, 4, 2, 9, 6, 2, 4, 8, 2, 5, 3, 3, 3, 8, 7, 4, 10, 3, 10, 8, 8, 4, 8, 5, 3, 4, 10, 9, 6, 6, 4, 10, 10, 3, 2, 10, 2, 3, 9, 3, 7, 9, 8, 4, 4, 6, 8, 2, 4, 8, 4, 3, 2, 10, 3, 2, 8, 10, 9, 8, 6, 5, 6, 7, 8, 10, 10, 5, 7, 9, 3, 10, 2, 9, 10, 3, 10, 7, 8, 4, 7, 10, 8, 6, 10, 8, 4, 3, 3, 7, 2, 5, 2, 2, 5, 6, 7, 9, 9, 7, 4, 9, 4, 4, 10, 8, 7, 10, 10, 9, 8, 6, 10, 7, 5, 8, 2, 2, 4, 2, 8, 2, 6, 5, 8, 5, 3, 7, 7, 6, 9, 5, 2, 4, 6, 7, 4, 5, 8, 6, 9, 4, 8, 8, 5, 7, 5, 5, 2, 4, 8, 9, 7, 8, 2, 8, 9, 7, 5, 4, 10, 9, 3, 8, 4, 2, 8, 9, 6, 7, 8, 4, 3, 8, 9, 4, 5, 8, 5, 6, 4, 7, 3, 9, 2, 10, 2, 10, 4, 4, 9, 10, 5, 2, 6, 2, 4, 4, 10, 4, 10, 10, 4, 9, 8, 6, 5, 2, 8, 8, 10, 8, 2, 9, 3, 6, 4, 9, 6, 4, 3, 8, 4, 2, 10, 7, 9, 2, 7, 2, 10, 10, 5, 7, 8, 6, 2, 2, 9, 7, 9, 9, 2, 10, 2, 7, 5, 5, 6, 7, 6, 6, 3, 2, 3, 3, 2, 4, 2, 4, 6, 5, 5, 5, 5, 9, 9, 9, 6, 5, 2, 3, 4, 6, 6, 2, 3, 2, 3, 4, 10, 6, 10, 6, 8, 9, 4, 7, 4, 7, 9]
    l = len(list_)
    if i == 0 or l <= 10:
        return list_
    else :
        for j in range(10) :
            portion = random_data[i * 10 + j]
            #list_ = list(reversed(list_[l//portion:])) + list_[0:l//portion] if i % 2 == 0 else list_[l//portion:] + list_[0:l//portion]
            list_ = list_[l//portion:] + list_[0:l//portion]
        return list_



### Initialize


city_0 = None # size == 0

min_cities = float("inf")
answer = []



### Size = 1, choose its adj
def find_size_1 () :
    candidates_size_1 = [i for i in range(1, c+1) if adj_num_list[i] == 1]
    candidates_size_1 = random(candidates_size_1, run_time)
    for node in candidates_size_1 :
        if all_nodes[node] == False :
            all_nodes[node] = True
            covered_nodes.append(node)
            adj = None
            for item in adj_dict[node] :
                if all_nodes[item] == False :
                    adj = item
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

### Main
total_times = 100
for run_time in range(total_times) :
    ### Init
    adj_num_list = [0 for _ in range(c + 1)]
    for i in range(1, c + 1):
        adj_num_list[i] = len(adj_dict[i])

    all_nodes = {}  # if covered, it carries True
    for i in range(1, c + 1):
        all_nodes[i] = False
    city_0 = city_0 if city_0 != None else len([i for i in range(1, c+1) if adj_num_list[i] == 0])
    chosen_nodes = []
    covered_nodes = []


    ### Iteration
    max_size = max(adj_num_list)
    size = max_size
    while len(covered_nodes) < (c - city_0) :
        if find_size_1() == False :
            candidates = [i for i in range(1,c+1) if adj_num_list[i] == size]
            candidates = random(candidates, run_time)
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
    if len(chosen_nodes) < min_cities :
        min_cities = len(chosen_nodes)
        answer = chosen_nodes



print (len(answer))
ans = ""
for i in sorted(chosen_nodes) :
    ans = ans + str(i) + " "
print (ans[0:-1])