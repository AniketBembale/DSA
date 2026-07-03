list1 = [1, 2, [1, 4, 5, 3, 2], 6, 7]

num = int(input("ENter the number : "))
for i,element in enumerate(list1):
     
     if type(element)==list:
          if num in element:
               print(f"The number found in inner list and the index is{(i,element.index(num))}")
               break
     elif num == element:
          print(f"The number found in outer index {(i)}")
          break

else:
    print("Not FOund")     



