# Given a list of strings, group the anagrams together.
# Anagram: Words that have the same characters in different orders. Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
 
# Output:
# [
#   ["eat", "tea", "ate"],
#   ["tan", "nat"],
#   ["bat"]
# ]
Inputs= ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_list = {}
for i in Inputs:
    word = ''.join(sorted(i))
    if word not in anagram_list:
        anagram_list[word]=[]
    
    anagram_list[word].append(i)
    
print(anagram_list.values())


    
        