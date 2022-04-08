# If Input is Sorted Array

nums = []
while True:
    try:
        k = input()
        nums.append(k)
    except EOFError as e:
        break
flag = 0
for i in range(len(nums)-1):
    if nums[i] <= nums[i + 1]:
        flag += 1
if(flag == len(nums) - 1):
    print("Ascending")
else:
    print("Descending")