size1 = int(input("ENTER THE NUMBER OF ELEMENTS OF LIST 1: ")
print("ENTER THE ELEMENT OF LIST 1 ONE BY ONE")
List1 = []
fot i in range(size1):
    List1.append(input())
size2 = int(input("ENTER THE NUMBER OF ELEMENTS OF LIST 2: ")
print("ENTER THE ELEMENTS OF LIST 2 ONE BY ONE")
list2 = []
for i in range(size2):
    List2.append(input())
intersectionList = list(set(list1).intersection(set(list2)))    
print("THE INTERSECTION OF LIST 1 AND LIST 2 IS:", ", ".join(intersectionList))
