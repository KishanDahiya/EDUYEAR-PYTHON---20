#prime number or not
def prime(num) :
  if num>1:
    for i in range(2,num):
       if num%i==0 :
         print(f"{num} is not a prime number")
         print(i,'times',num//i,'is',num)
         break
    else :
      print(f"{num} is a prime number")
  else :
    print(f'{num} is a prime number')

#factorial of a number
def fact(a):
  f=1
  t=a
  while a!=0 :
   f=f*a
   a=a-1
  print(f'The Factorial of {t} is {f}')

prime(int(input('Enter a number : ')))
fact(int(input('\nEnter the number you want factorial of : ')))
  
