def y_matrix(n):
    y=[[0]for i in range(n)]
    input_second=input()
    second=input_second.split()
    for j in range(0,n):
        y[j][0]=int(second[j])
    return y

def new_matrix(n,m):
    matrix = [ [ 0 for i in range(m+1) ] for j in range(n) ]
    for i in range(0,n):
        for j in range(0,m+1):
            matrix[i][j]=(i+1)**j
    #print(matrix)
    return matrix

def t_matrix(matrix):
    rows,cols=len(matrix),len(matrix[0])
    t_matrix = [ [0 for i in range(rows) ] for j in range(cols) ]
    for i in range (0,rows):
        for j in range (0,cols):
            t_matrix[j][i]=matrix[i][j]
    return t_matrix


def multiply(m1,m2):
    m1rows,m1cols=len(m1),len(m1[0])
    m2rows,m2cols=len(m2),len(m2[0])
    if m1cols == m2rows :
        mu_matrix = [ [0 for i in range(m2cols) ] for j in range(m1rows) ]
        for i in range(0,m1rows):
            for j in range(0,m2cols):
                for k in range(0,m1cols):
                    mu_matrix[i][j] += m1[i][k] * m2[k][j]
    
    return mu_matrix




def det(matrix):
    n=len(matrix)
    if n > 2:
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m == t):
                        u=0
                    else:
                        d[t1].append(matrix[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(matrix[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])

def minor_matrix(x,y,matrix):
    rows,cols=len(matrix),len(matrix[0])
    mi_matrix=[ [0 for i in range(cols-1) ] for j in range(rows-1) ]
    mi=0
    for i in range(0,rows):
        mj=0
        for j in range(0,cols):
            if i!=x and  j!=y :
                mi_matrix[mi][mj]=matrix[i][j]
                mj+=1
        if i!=x :
            mi+=1
    return mi_matrix

def inverse_matrix(matrix):
    rows,cols,d=len(matrix),len(matrix[0]),det(matrix)
    i_matrix=[ [0 for i in range(rows) ] for j in range(cols) ]
    k=1
    if len(matrix) > 2:
        for i in range(0,rows):
            l=1
            for j in range(0,cols):
                i_matrix[i][j]=det(minor_matrix(i,j,matrix)) * k * l / d
                l *= -1
            k *= -1
        i_matrix = t_matrix(i_matrix)

    else:
        i_matrix[0][0] = matrix[1][1] / d
        i_matrix[1][0] = -matrix[1][0] / d
        i_matrix[0][1] = -matrix[0][1] / d
        i_matrix[1][1] = matrix[0][0] / d
    return i_matrix

def min_error(m,n,C,y):
    matrix=new_matrix(n,m)
    step1 = multiply( t_matrix(matrix) , matrix ) 
    step2 = multiply( inverse_matrix(step1) , t_matrix(matrix) )
    final_matrix = multiply( step2 , y )
    #print(final_matrix)
    
    E=0
    for i in range(0,n):
        p_i=0
        for j in range(0,m+1):
            p_i+=final_matrix[j][0]*(i+1)**j
        E+=(p_i-y[i][0])**2
    
    return(E)

def least_square_error(m,n,C,y):
    cost=[ [ 0 for i in range(n+1) ] for j in range(n+1) ]
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            piecewise=[ [0] for x in range(l) ]
            for s in range(l):
                piecewise[s][0]=y[s+i][0]
            if m > l-1 :
                cost[i][j]=0
            else:
                cost[i][j]=min_error(m,l,C,piecewise)
            for k in range(i,j):
                q=cost[i][k]+cost[k+1][j]+C
                if q<cost[i][j]:
                    cost[i][j]=q
    #print(cost)
    return cost[0][n-1]

        
            

    
    

input_first=input()
first=input_first.split()
n,m,C=int(first[0]),int(first[1]),int(first[2])
y=y_matrix(n)
output=least_square_error(m,n,C,y)
print(round(output))







