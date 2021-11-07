# 1 TLE
n,x,y = map(int,input().split())

def fibonatti_div_100(n):
    if n == 1:
        return x
    if n == 2:
        return y
    return ((fibonatti_div_100(n-2) + fibonatti_div_100(n-1)) % 100)

print(fibonatti_div_100(n))

# 1 AC
n,x,y = map(int,input().split())
A = [0]*n
A[0] = x
A[1] = y

for i in range(2,n):
    A[i] = (A[i-2] + A[i-1]) % 100

print(A[n-1])

# 2 AC
n = int(input())
A = list(map(int,input().split()))

ans = [0]*n
ans[1] = A[1]

for i in range(2,n):

    ans[i] = min(ans[i-2] + 2*A[i],ans[i-1] + A[i])
    # こちらではWAとなるが何故かはわからない
    # if A[i-1] < A[i]:
    #     ans[i] = ans[i-2] + 2*A[i]
    # else:
    #     ans[i] = ans[i-1] + A[i]

print(ans[n-1])

# 3
n = int(input())

A = [1]*(n+1)

for i in range(2,n+1):
	A[i] = A[i-2] + A[i-1]

print(A[n])

# 4
n = int(input())

ans = [1]*(30+1)
ans[2] = 2
ans[3] = 4

if n > 3:
	for i in range(4,n+1):
		ans[i] = ans[i-1] + ans[i-2] + ans[i-3]

print(ans[n])

# 5 WA
n,m = map(int,input().split())
A = list(map(int,input().split()))

ans = [0]*(n+1)

for i in range(1,n+1):
    take_times = []
    for j in range(1,min(i+1,m+1)):
        take_times.append(ans[i-j]+j*A[i-j-1])
    ans[i] = min(take_times)
print(ans[n])

# 5 WA
n,m = map(int,input().split())
A = list(map(int,input().split()))

ans = [0]*(n+1)

for i in range(1,n+1):
	take_times = []
	print(ans)
	for j in range(1,min(i+1,m+1)):
		print(j)
		print(A[i-j])
		take_times.append(ans[i-j]+j*A[i-j])
	print(take_times)
	ans[i] = min(take_times)
print(ans)


# 6 WA
n,m = map(int,input().split())
D = list(map(int,input().split()))

dp = [[]]*(m+1)
dp[1] = D
for i in range(2,m+1):
    points = []
    for j in dp[i-1]:
        for k in D:
            points.append(j+k)
    dp[i] = list(set(points))

ans = []
for i in range(1,m+1):
    ans.extend(dp[i])
ans = set(ans)

if n in ans:
    print("Yes")
else:
    print("No")