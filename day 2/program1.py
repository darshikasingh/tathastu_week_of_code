a=int(input("ENTER ANY NUMBER"))
if(a%2==0):
  print("EVEN")
else:
  print("ODD")


num=int(input("ENTER ANY NUMBER"))
if num>1:
  for i in range(2,num):
    if(num%i)==0:
       print(num,"is not prime number")
       print(i,"times",num//i,"is",num)
       break
    else:
       print(num,"is a prime number")
else:
  print(num,"is not a prime number")
  
  
  n=int(input("ENTER THE NUMBER:"))
  temp=n
  rev=0
  while(n>0):
      dig=n%10
      rev=rev*10+dig
      n=n//10
  if(temp==rev):
     print("PALINDROME")
  else:
     print("NOT PALLINDROME")
     
     
 num=int(input("ENTER THE NUMBER"))
 sum=0
 temp=num
 while(temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp//=10
  if(num==sum)
     print(num,"is an armstrong number")
  else:
     print(num,"is not an armstrong number")
