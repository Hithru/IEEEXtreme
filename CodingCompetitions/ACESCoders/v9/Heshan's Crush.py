u,v,l = map(int,input().strip().split())

answer = (l*(3*v+u))/(v**2+3*v*u)

print('{:.4f}'.format(round(answer, 4)))
