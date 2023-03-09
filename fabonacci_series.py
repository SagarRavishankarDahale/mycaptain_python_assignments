nterms=int(input("enter the number of terms"))
n1,n2=0,1
count=0
print("fabonacci series",n1,n2)
while(count<=nterms):
   sum = n1 + n2
   print(sum)
   n1=n2
   n2=sum
   count=count+1



