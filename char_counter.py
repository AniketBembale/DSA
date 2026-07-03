# def char_count(word):
#   char = {}
#   for ch in word:
#     if ch in char:
#       char[ch] += 1
#     else:
#       char[ch] = 1
#   return char

# char_count("qabbkll")



# def char_count(c):
#   char = {}

#   for ch in c:
#     if ch in char:
#       char[ch]+=1
#     else:
#       char[ch] = 1
#   return char



# print(char_count("abccceedd"))


def char_count(s):
  char={}

  for ch in s:
    if ch in char:
      char[ch]+=1
    
    else:
      char[ch]=1

  return char

print(char_count("abccceedd"))






def char_count(s):
  char = {}

  for ch in s:
    if ch in char:
      char[ch]+=1
    else:
      char[ch] = 1
  return char

print(char_count("aabbcccccddddddddeeeee"))