# 1
n,a,b = map(int,input().split())

s = []
for i in range(n):
    s.append(input())

if s[a][b] == "o":
    print("Yes")
else:
    print("No")

# 2
n, m = map(int, input().split())
n_list = []
for i in range(n):
    n_list.append([])

for i in range(m):
    a,b = map(int,input().split())
    n_list[a].append(b)

for i in n_list:
    print(*sorted(i))

# 3
n, m, x = map(int, input().split())
n_list = []
for i in range(n):
    n_list.append([i])

for i in range(m):
	a,b = map(int,input().split())
	n_list[a].append(b)
	n_list[b].append(a)


ans = []
for i in n_list[x]:
	for j in n_list[i]:
		ans.append(j)

ans_set_list = list(set(ans))

print(len(ans_set_list) - len(n_list[x]))

# 4
n, x = map(int, input().split())
a = list(map(int,input().split()))

box_dict = {}

for i in range(len(a)):
	box_dict[i+1] = a[i]

next_box = box_dict[x]
count = 1
for i in range(n):
	if next_box == 0:
		break
	next_box = box_dict[next_box]
	count += 1
print(count)