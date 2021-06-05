#Program to count sum of all even numbers and odd numbers of a list.

list=[1,10,20,31,121,222,545,101]
es,os=0,0
en,on=0,0
print('\nThe list is {}'.format(list))
for i in range(0,len(list)):
 if list[i]%2==0 :
  en+=1
  es+=list[i]
 else :
  on+=1
  os+=list[i] 
print('Sum of all {} even numbers of list is {}\nSum of all {} odd numbers is {}'.format(en,es,on,os))

#maximum and minimum of the list without using function like max() or min()

sl=sorted(list)
mxn,mn=sl[-1],sl[0]
print('\nThe max is : {}\nThe min is : {}\n'.format(mxn,mn))

#Checking if whole list is palindrome or not

l1=[1,2,3,4,3,2,1]
print('\nThe list is {}'.format(l1))
c=l1[::-1]
if c==l1 :
 print('The whole list {} is palindrome'.format(l1))
else :
 print('The list {} is not palindrome'.format(l1))

#check a list and print numbers inside it if they are laindrome or not
 
n=[1112,1211,2345,5665,101,111]
tmp=0
print('\nThe list is {}'.format(n))
for i in range(len(n)) :
 tmp=str(n[i])
 tmp=tmp[::-1]
 tmp=int(tmp)
 if tmp==n[i] :
  print('The element {} is palindrome'.format(n[i]))
