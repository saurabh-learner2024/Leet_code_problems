def get_max_and_min(list_nums):
    max_val = list_nums[0]
    min_val = list_nums[0]

    for ele in list_nums:
        if ele > max_val:
            max_val = ele
        if ele < min_val:
            min_val = ele

    return max_val, min_val


lis = [11, 12, 13, 14, 15, 16]
max_val, min_val = get_max_and_min(lis)
print(max_val, min_val)
