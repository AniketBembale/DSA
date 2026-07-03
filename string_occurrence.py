
# def count(first_string, second_string):
#     count_occurrences = 0

#     for i in range(len(first_string) - len(second_string) + 1):
#         if first_string[i:i + len(second_string)] == second_string:
#             count_occurrences += 1

#     return count_occurrences

# print(count('abcdefg', 'def'))



def count_occurence(first_string,second_string):
    occurence = 0

    for i in range(len(first_string)-len(second_string)):
        if first_string[i:i+len(second_string)]==second_string:
            occurence+=1
    return occurence
print(count_occurence('abcdecg', 'def'))








def count_occurence(first_string,second_string):
    occurence = 0
    for i in range(len(first_string)-len(second_string)):
        if first_string[i:i+len(second_string)] == second_string:
            occurence +=1
    return occurence

print(count_occurence('abcdecg', 'dec'))
