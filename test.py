#2 list into a dictionary

L1 = [1,2,3,4]
L2 = ['a','b','c','d']
print(f'\nThe two list are {L1} and {L2}')
z=dict(zip(L1,L2))
print(f'The dictionary is {z}')

#program to count alphabet and digits

str = input("\nInput a string : ")
a=d=0
for c in str:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        a+=1
    else:
        pass
print("Letters : ",a)
print("Digits : ",d)

#Function to return the longest word

str=input('\nEnter the string : ')
l=max=0
t=str.split(" ")
for i in range(len(t)):
  l=len(t[i])
  if l<max:
    continue
  else:
    max=l
    e=i
print(f'The longest word is {t[e]} it is {max} characters long')

#pattern

q=int(input('\nEnter the number for pattern : '))
for i in range(q):
  for j in range(i+1):
   print(i+1,end="")
  print()

#check for Russian palindrome

vl=input('\nEnter a number : ')
num=int(vl)
flag=0
def prime(num) :
  if num>1:
    for i in range(2,num):
       if num%i==0 :
         break
    else :
      return 1
  else :
    return 1

for i in vl:
  flag=prime(int(vl))
  vl=vl[:-1]

if flag==1:
  print(f"\n{num} is Russian prime number")
else:
  print(f"\n{num} is not Russian prime number")
  
