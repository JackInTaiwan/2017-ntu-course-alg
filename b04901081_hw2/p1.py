def smallestDigits(num) :
    output = ''
    for i in range(9,1,-1) :
        while num % i == 0 :
            output = str(i) + output
            num /= i
    if len(output) == 0 : return '11'
    elif len(output) == 1 : return '1' + output
    else : return output



if __name__ == '__main__' :
    caseNum = int(input())
    cases = []
    for i in range(caseNum) :
        case = input()
        cases.append(int(case))
    for case in cases :
        print (smallestDigits(case))