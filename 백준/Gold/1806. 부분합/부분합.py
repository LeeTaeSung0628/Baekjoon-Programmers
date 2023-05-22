import sys
input = sys.stdin.readline

# n = 수열의 길이 / m = 합이 m이상인지..
n, m = map(int,input().split())
#수열
numArr = list(map(int,input().split()))

sumArr = [0] * (n + 1)
tree = [0] * (n + 1)
temp = 0
for i in range(1,len(numArr)+1):
    temp+=numArr[i-1]
    sumArr[i] = temp
    tree[i] = sumArr[i] - sumArr[i - (i & -i)]

#----====----

def prefix_sum(n):
    res = 0
    while n > 0:
        res += tree[n]
        n -= (n & -n)
    return res
def bubun_sum(x,y):
    return prefix_sum(y) - prefix_sum(x - 1)

def update(x, y): #x번째 수를 y만큼 더하기
    while x <= len(tree):
        tree[x]+=y
        x += (x & -x) 

sol = []
i = 1
j = 1
sum = bubun_sum(i,j)
cnt = 0
chkOut = False

while True:
    if sum < m:
        j+=1
        if j <= n:
            sum = bubun_sum(i,j)
        else:
            break
    else: #sum이 더 커지면
        sol.append((j-i)+1)
        i+=1
        if i <= j:
            sum = bubun_sum(i,j)
        else:
            break

if len(sol) == 0:
    print(0)
else:
    print(min(sol))

