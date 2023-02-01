MOD = 1000000007
def mul(A,B):
    return [ [ sum(A[r][i]*B[i][c] for i in range(2))%MOD for c in range(2) ] for r in range(2) ]

def exp(A,n):
    if n==0: return [ [1,0], [0,1] ]
    C = exp(A,n//2)
    C = mul(C,C)
    return mul(A,C) if n%2 else C
t = int(input())
for i in range(t):
    n = int( input() )
    print( exp( [ [0,1], [1,1] ], n )[1][1] )