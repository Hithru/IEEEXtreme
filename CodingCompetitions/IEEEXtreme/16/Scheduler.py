# import math
#
# n,m = map(int,input().strip().split(" "))
# jobs = [2**int(i) for i in input().split()]
#
# while len(jobs) >m:
#     jobs = [jobs[0]+jobs[1]]+jobs[2:]
#     jobs.sort()
# print(jobs[-1]%1000000007)


def insort_right(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    a.insert(lo, x)


n, m = map(int, input().strip().split(" "))
jobs = [2 ** int(i) for i in input().split()]
jobs.sort()
while len(jobs) > m:
    new_element = jobs[0] + jobs[1]
    jobs = jobs[2:]
    if len(jobs) > 1 and new_element < jobs[0]:
        jobs = [new_element] + jobs
    else:
        insort_right(jobs, new_element)
print(jobs[-1] % 1000000007)