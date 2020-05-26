def last(n)
   return n[-1]
def sort(tuples):
   return sorted(tuples, key=last)
a= input("ENTER A LIST OF TUPLE:")   
print("SORTED:")
print(sort(a))
