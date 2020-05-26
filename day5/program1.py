def replace(number)
if (number==0)
return 0;
digit=number%10
if (digit==0);
   digit=5
   return replace(int(number/10))*10+digit
   number=int(input("ENTER THE NUMBER:"))
   print("NUMBER AFTER REPLACEMENT:",replace(number))
