n = [2]
m = [2]
value = [10]
matrix = (n,m,value)
def get_matrix (n, m, value):
    matrix = []
    for i in range (n):
        spisok = []
        for j in range (m):
            spisok.append(value)
        matrix.append (spisok)
    return matrix
    result = get_matrix()
for spisok in result:
    print (spisok)
