### Dealing with the algorithm
def recursiveMinPolyError(ys, c, i, j, m, errorMemory, pivotMemory) :
    pivotCost = c if i != 0 else 0
    if j-i <= m :
        return pivotCost
    elif j-i == m + 1 :
        return calculateError(ys, i, j, m) + pivotCost
    else :
        if (i,j) not in errorMemory :
            error = [(recursiveMinPolyError(ys, c, i, k, m, errorMemory, pivotMemory) + recursiveMinPolyError(ys, c, k+1, j, m, errorMemory, pivotMemory), k) for k in range(i, j) ]
            error.append((calculateError(ys, i, j, m) + pivotCost, j))
            pivot = min(error)[1]
            pivotMemory.add(pivot)
            minVal = min(error)[0]
            errorMemory[(i,j)] = minVal
            return minVal
        else :
            return errorMemory[(i,j)]

def calculateError(ys, i, j, m) :
    n = j-i+1
    mMat = [[q**p for p in range(m+1)] for q in range(1,n+1)]
    yMat = [[y] for y in ys[i:j+1][:]]
    aMat = matriceMultiplication(inverseMatrix(matriceMultiplication(list(zip(*mMat)), mMat)), matriceMultiplication(list(zip(*mMat)), yMat))
    error = 0
    yy = ys[i:j+1]
    for x in range(1,j-i+2) :
        term = 0
        for i, a in enumerate(aMat) :
            term += a[0] * (x ** i)
        error += (term - yy[x-1]) ** 2
    return error



### Dealing with calculation of matrices
def matriceSerialMultiplication(matrice) :
    matrice = matrice[:]
    matrix = matrice.pop(0)
    for mat in matrice :
        matrix = matriceMultiplication(matrix, mat)
    return matrix

def matriceMultiplication(mat1, mat2) :
    output = [[sum([pair[0] * pair[1] for pair in zip(mat1Row, mat2Col)]) for mat2Col in zip(*mat2)]for mat1Row in mat1]
    return output

def subMatrix(mat, deletedRow, deletedCol):
    return [row[:deletedCol] + row[deletedCol+1:] for row in (mat[:deletedRow]+mat[deletedRow+1:])]

def deternminant(mat):
    if len(mat) == 2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    res = 0
    for i in range(len(mat)):
        res += (-1) ** i * mat[0][i] * deternminant(subMatrix(mat,0,i))
    return res

def inverseMatrix(mat):
    det = float(deternminant(mat))
    if len(mat) == 2:
        return [[mat[1][1]/det, -1*mat[0][1]/det], [-1*mat[1][0]/det, mat[0][0]/det]]
    cofMat = [[int(((-1) ** (i+j) * deternminant(subMatrix(mat, i, j)) / det) * 10 ** 5)/100000.0 for j in range(len(mat))] for i in range(len(mat))]
    return list(zip(*cofMat))



### Main
if __name__ == '__main__' :
    params = input()
    ys = input()
    params, ys = params.split(' '), ys.split(' ')
    params, ys = [int(param) for param in params], [float(y) for y in ys]
    errorMemory = dict()
    pivotMemory = set()
    m, c, i, j = params[1], params[2], 0, len(ys) - 1
    print (int(round((recursiveMinPolyError(ys, c, i, j, m, errorMemory, pivotMemory)))))