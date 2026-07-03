# def freq_Count(n):
#     freq_hash = {}

#     for i in range(0,len(n)):
#         if n[i] in freq_hash:
#             freq_hash[n[i]] += 1
#         else:
#             freq_hash[n[i]]=1
#     return freq_hash
# print(freq_Count([1,1,2,2,4,5,6,7,7]))



def freq_Count(list1):
    freq_hash = {}
    n = len(list1)

    for i in range(0,n):
        freq_hash[list1[i]] = freq_hash.get(list1[i],0)+1
    return freq_hash
print(freq_Count([1,1,2,2,4,5,6,7,7]))
