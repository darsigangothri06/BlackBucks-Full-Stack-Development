nums = []
while True:
    try:
        k = input()
        nums.append(int(k))
    except EOFError as e:
        break
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(nums)