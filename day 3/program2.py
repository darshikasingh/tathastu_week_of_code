def permutation(List, String)
    Set=set(List)
    stringList=[]
    if len(Set) == 1:
       String += "",join(List)
       return List([String])
    for x in Set:
       List1=list(List)
       S=String+x
       List.remove(x)
       stringList.extend(permutation(List, S))
    return stringList
    
string=input(ENTER A STRING: ")
List= permutation(list(string))
print("PERMUTATION IS: "+",".join(List))

        
