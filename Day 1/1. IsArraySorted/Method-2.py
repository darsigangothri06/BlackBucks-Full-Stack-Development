# If input array is not sorted

nums = []
while True:
    try:
        k = input()
        nums.append(k)
    except EOFError as e:
        break
asc = False
des = False
for i in range(len(nums)-1):
    if nums[i] <= nums[i + 1]:
        asc = True
    else:
        des = True
if(asc):
    if des:
        print("Not Ascending and Not Descending")
    else:
        print("Ascending")
else:
    print("Descending")