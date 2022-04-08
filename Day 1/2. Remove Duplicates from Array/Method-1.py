nums = []
while True:
    try:
        k = input()
        nums.append(int(k))
    except EOFError as e:
        break
new = []
for i in nums:
    if i not in new:
        new.append(i)
for i in new:
    print(i)