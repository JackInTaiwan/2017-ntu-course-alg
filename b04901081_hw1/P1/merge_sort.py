import time
import sys

########################################
# You can add supporting functions here


########################################

def mergesort(x, count):
    ### TODO ###
    # Implement the merge sort algorithm.
    # x is a list with N elements.
    # You must return a sorted list and a counter of splitting number.
    globalCount = 0
    def split(inputList):
        nonlocal globalCount
        listLength = len(inputList)
        if listLength > 1: globalCount += 1
        redundant, num = listLength % 3, listLength // 3
        if redundant == 0 : splitList = [inputList[0:num], inputList[num:num*2], inputList[num*2:]]
        elif redundant == 1 : splitList = [inputList[0:num+1], inputList[num+1:num*2+1], inputList[num*2+1:]]
        else : splitList = [inputList[0:num+1], inputList[num+1:num*2+2], inputList[num*2+2:]]
        return splitList

    def submerge(subLists):
        outputList = subLists[0]
        del subLists[0]
        for list in subLists:
            criterion = 0
            for element in list:
                for i in range(criterion, len(outputList)):
                    if outputList[i] >= element:
                        outputList.insert(i, element)
                        criterion = i
                        break
                else:
                    outputList += list[list.index(element):]
                    break
        return outputList

    def recursiveSplitAndMerge(list):
        lists = split(list)
        if len(list) > 3: return submerge([recursiveSplitAndMerge(lists[0]), recursiveSplitAndMerge(lists[1]), recursiveSplitAndMerge(lists[2])])
        else: return submerge(lists)

    x, count = recursiveSplitAndMerge(x), globalCount

    return x, count

if __name__ == '__main__':
    case = sys.argv[1]
    test_name = 'test_'+str(case)+'.txt'
    out_name = 'out_'+str(case)+'.txt'
    file_in = open(test_name, 'r')
    file_out = open(out_name, 'w')
    start_time = time.time()
    l = file_in.readline().split()
    l = list(map(int, l))
    count = 0 
    result, count = mergesort(l, count)
    for i in result:
        file_out.write(str(i)+' ')
    file_out.write('\n')
    file_out.write(str(count))
    print('Timer: ', time.time()-start_time)

