list1 = [1,2,2,3,55,55,98,65,65,13,29,29]  
# Declare an empty list that will store unique values  

list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)
        print(i, end=" ")
