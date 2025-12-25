n = int(input("Enter a number: ")
if n%2==0:
        print("Even number")
else:
        print("odd number")
if n<=1:
  print("NOT a prime number")
else:
  c=0
  for i in range(1,n):
    if n%i==0:
      c=c+1
  if c==2:
    print("prime number")
  else:
    print("not a prime number")
