nterms=int(input("ENTER THE NUMBER OF TERMS"))
n1,n2=0,1
count=0
if nterms<=0:
   print("ENTER A POSITIVE INTEGER")
elif nterms==1:
    print("FIBONACCI SEQUENCE UPTO",nterms,":")
    print(n1)
else:
    print("FIBONACCI SEQUENCE:")
    while count<nterms:
         print(n1)
         nth=n1+n2
         n1=n2
         n2=nth
         cout+=1
