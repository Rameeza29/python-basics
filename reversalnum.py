# Program to reverse a number entered by the user


n=int(input("Enter a number"))
rev=0
while n>0:
  rev=rev*10+n%10
  n=n//10
print("reversed number",rev)