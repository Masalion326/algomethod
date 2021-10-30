# 1
n = int(input())
a = list(map(int,input().split()))

prime_num = list(range(2,max(a)+1))
ans = []

for i in range(2,max(a)+1):
    if i in prime_num:
        ans.append(i)
        for j in prime_num:
            if j % i == 0:
                prime_num.remove(j)

count = 0
for i in a:
    if i in ans:
        count += 1
print(count)


# 2
n,k = map(int,input().split())

ans = 0
for i in range(1,n+1):

    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    
    if count == k:
        ans += 1

print(ans)


# 3
l,r = map(int,input().split())

count = 0
for i in range(l,r+1):
	if str(i) == str(i)[::-1]:
		count += 1
print(count)

# 4
import collections

s = input()

c = collections.Counter(list(s))

print(len(c.keys()))

# 5
n = int(input())

count = 0
for i in range(n):
	s = input()

	if s == s[::-1]:
		count += 1
print(count)


