#printing all numbers divisibe by 5 and 7 between given range.

print('\nEnter a range of number between which you wanna find all numbers divisible by both 5 and 7.')
a=int(input())
b=int(input())
print('The numbers divisible by 5 and 7 are',end=' ')
for i in range(a,b) :
 if (i%5==0) and (i%7==0):
  print(i,end=' ')

#Finding the sum of the series 2+22+222+......+n for n terms

num=int(input('\n\nEnter the n term for series : '))
sum=0
for i in range(1,num+1) :
  if i==(num) :
   e='='
  else :
   e='+'
  print(i*'2',end=e)
  t=int(i*'2')
  sum+=t
print(sum)

'''Taking integer inputs from user until he/she presses q
( Ask to press q to quit after every integer input)
Print the sum of all numbers.'''

var=a
s=0
while var!='q' :
 s+=int(input('\nEnter an integer : '))
 print('The sum of already entered integers is : ',s)
 var=input('\nEnter q if you want to stop adding more integers.\nOR\nPress enter to continue\n')


#Simple while loop to find the factorial of any number

fact=1
no=int(input('\nEnter the number you want factorial of : '))
n=no
while n!=0 :
 fact=fact*n
 n=n-1
print('The Factorial of {} is {}'.format(no,fact))

#program to display the string as P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e

str='python is a good programming language'
print('\nThe string is {} : '.format(str))
for i in range(len(str)) :
 end_v='-'
 if str[i]==' ' :
  end_v=''
 elif i==len(str)-1 :
  end_v=''
 elif str[i+1]=='' :
  end_v=''
 if i%2==0:
  print(str[i].upper(),end=end_v)
 else :
  print(str[i].lower(),end=end_v)
