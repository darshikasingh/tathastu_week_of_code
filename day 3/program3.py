def duplicate(string):
   duplicateString = ""
   for x in string:
      if x not in duplicateString:
          duplicateString += x
   return duplicateString
   
string = input("ENTER THE STRING")
print("STRING AFTER REMOVING DUPLICATION IS", duplicate(string))
   
   
