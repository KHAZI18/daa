def trans(a,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k]or a[k][j])


def main():
    a = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]
    n = len(a[0])
    print("The adjacent matrix is ")
    print(a)
    print("transitive matrix is ")
    trans(a,n)
    print(a)
main()



