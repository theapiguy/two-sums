nums = [6, 4, 7, 9, 3, 12]
t = 9

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            if nums[i] + nums[j] == t:
                print(nums[i], nums[j])
