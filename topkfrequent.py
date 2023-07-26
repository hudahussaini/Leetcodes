def topKFrequent(nums, k):
    dict_of_nums = {}
    my_list = []
    for num in nums:
        if num not in dict_of_nums:
            dict_of_nums[num] = 0
        else:
            dict_of_nums[num] += 1
    for i in range(k):
        max_key = max(dict_of_nums, key=dict_of_nums.get)
        my_list.append(max_key)
        del dict_of_nums[max_key]
    return my_list

    
