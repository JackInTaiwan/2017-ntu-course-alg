import sys
########################################
# You can add supporting functions here





########################################
def match(men, women, mprefer, wprefer):
    ### TODO ###
    # Implement the Gale-Shapley algorithm.
    # You should return a dictionary of pairing result, use woman as key and man as
    # value.

    pairs = []
    for man in range(len(men)):
        outMan = man
        if len(pairs) > 0:
            while outMan != None :
                for wantWoman in mprefer[outMan] :
                    if wantWoman not in [item[1] for item in pairs] :
                        pairs.append([outMan, wantWoman])
                        outMan = None
                        break
                    elif women[wantWoman][outMan] < women[wantWoman][[wantWoman == item[1] for item in pairs].index(True)] :
                        pairs[[wantWoman == item[1] for item in pairs].index(True)][0], outMan = outMan, pairs[[wantWoman == item[1] for item in pairs].index(True)][0]
                        outMan = None
                        break
        else : pairs.append([man, mprefer[man][0]])
    wives = dict([[item[1],item[0]] for item in pairs])     # transform (m,w) -> (w,m)
    return wives


def is_stable(men, women, mprefer, wives):
    if wives is None:
        wives = wives
    for w, m in wives.items():
        i = men[m][w]
        preferred = mprefer[m][:i]
        for p in preferred:
            h = wives[p]
            if women[p][m] < women[p][h]:  
                return False
    return True

if __name__ == '__main__':
    '''
    A reminder of the definitions of variables

    men is a 2D-list which presents men's rankings for women. 
    men[m][w]=i means man 'm' ranks woman 'w' as i.
    Note that every list is zero-based and 0 means the highest preference.
    For example, if there are 10 pairs of men and women, 
    they are denoted as m0, m1, ..., m9 and w0, w1, ..., w9
    men[1][2] = 0 means m1 likes w2 the most among all women.
    Similarly, women[1][2] = 1 means, for w1, m2 is her second choice.
    
    mprefer is a 2D-list which presents men's preference.  
    mprefer[m][i]=w means, for man 'm', his i-th preferable woman is 'w'
    For examples, mprefer[1][0]=2 means m1's first choice is w2.
    '''
    case = str(sys.argv[1])
    men = []
    men_file = 'men_' + case + '.txt'
    women_file = 'women_' + case + '.txt'
    for line in open(men_file, 'r'):
        man = list(map(int, line.split()))
        men.append(man)

    women = []
    for line in open(women_file, 'r'):
        woman = list(map(int, line.split()))
        women.append(woman)

    wives = {}
    pairs = []
    
    mprefer = []
    wprefer = []
    pair_num = len(men[0])
    
    for i in range(pair_num):
        mp = []
        wp = []
        for j in range(pair_num):
            mp.append(men[i][:].index(j))
            wp.append(women[i][:].index(j))
        mprefer.append(mp)
        wprefer.append(wp)
    
    wives = match(men, women, mprefer, wprefer)
    if is_stable(men, women, mprefer, wives):
        print('The matching is stable.')
    else:
        print('The matching is failed.')







