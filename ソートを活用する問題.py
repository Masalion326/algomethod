# 1
n = int(input())
a = list(map(int,input().split()))

a.sort()

if n % 2:
	print(a[int((n-1)/2)])
else:
	print((a[int(n/2-1)]+a[int(n/2)])/2)

# 2
n,m = map(int,input().split())
a = list(map(int,input().split()))
x = list(map(int,input().split()))

a.sort()

for i in x:
	print(a[i])

# 3
n,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse=True)

print(sum(a[:k]))

# 4
n,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

for i in range(n-k+1):
	if i == 0:
		ans  = a[i+k-1] - a[i] 
	else:
		if ans > (a[i+k-1] - a[i]):
			ans = a[i+k-1] - a[i]

print(ans)

# 5
# TLE
n = int(input())
a = list(map(int,input().split()))


a_set_list = list(set(a))
a_set_list.sort(reverse=True)

for i in a:
	print(a_set_list.index(i))

# AC
n = int(input())
a = list(map(int,input().split()))


a_set_list = list(set(a))
a_set_list.sort(reverse=True)


sort_dict = {}
for i in range(len(a_set_list)):
	sort_dict[a_set_list[i]] = i


for i in a:
	print(sort_dict[i])
