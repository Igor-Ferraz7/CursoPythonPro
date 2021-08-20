nums = [2, 3, 7, 6]
target = 5
for c in range(len(nums)-1):
    tentativa = nums[c] + nums[c+1]
    if tentativa == target:
        print(f'[{c}, {c+1}]')
        break