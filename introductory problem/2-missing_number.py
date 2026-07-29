n = int(input())
total_sum = n * (n + 1) // 2
num = map(int, input().split())
given_sum = sum(num)
print(total_sum - given_sum)