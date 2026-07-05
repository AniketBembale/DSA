n = [1,3,4,5,6,2,3,4,4,5,7,9,9,10]
m = [1,3,4,5,6,13,23,44,43,10,61,71,11,22]


# # Approach -  1 Brute Force


# for i in m:
#     count = 0
#     for x in n:
#         if x == i:
#             count+=1
#     print(f"{i}:{count}")


# Approach - 2 Hash List

# hash_list = [0] * 11

# for i in n:
#     hash_list[i]+=1

# for i in m:
#     if i<1 or i>10:
#         print(0)
#     else:
#         print(f"{i}:{hash_list[i]}")


# freq_dict = {}
# for i in n:
#     if i in freq_dict:
#         freq_dict[i] +=1
#     else:
#         freq_dict[i] = 1

# for i in m:
#     if i<1 or i>10:
#         print(0)
#     else:
#         print((f"{i}:{freq_dict[i]}"))





word = "ssaavvbewwwwwwwwe"
# for lower char asci number between 97 - 122
char_list = ['a','b','c','s','v','e','w']



# print(ord("a"))

asci_list = [0]*26
for i in word:
    index = ord(i)-97
    asci_list[index]+=1


for i in char_list:
    index = ord(i)-97
    print(f"{i}:{asci_list[index]}")



