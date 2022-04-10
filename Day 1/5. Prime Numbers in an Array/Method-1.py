nums = []
while True:
    try:
        k = input()
        nums.append(int(k))
    except EOFError as e:
        break

def isPrime(num):
    flag = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = 1
            break
    if flag == 1:
        return False
    return True

count = 0
for i in nums:
    if isPrime(i):
        count += 1
print(count)