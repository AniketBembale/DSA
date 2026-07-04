def freq_count(nums):
    freq_map = {}

    for i in nums:
        if i in freq_map:
            freq_map[i]+=1
        else:
            freq_map[i]=1
    return freq_map

print(freq_count([1,1,2,4,5,5,6,6,6,6,7]))



def freq_count(nums):
    freq_map = {}
    for i in range(0,len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] += 1
        else:
            freq_map[nums[i]] = 1
    return freq_map
        

print(freq_count([1,1,2,4,5,5,6,6,6,6,7]))




def freq_count(nums):
    freq_map = {}
    for i in nums:
        freq_map[i] = freq_map.get(i,0)+1
    return freq_map


  
        

print(freq_count([1,1,2,4,5,5,6,6,6,6,7]))





