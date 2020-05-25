def duplicate(List):
    duplicateList = []
    for x in List:
        if x not in duplicateList:
             duplicateList.append(x)
     return duplicateList
     
size = int(input("ENTER THE NUMBER OF ELEMENTS")
print("ENTER THE ELEMENT IN LIST")
List = []
for i in range(size):
    Liat.append(input())
print("LIST AFTER REMOVING THE DUPLICATE IS:", duplicate(List))    
