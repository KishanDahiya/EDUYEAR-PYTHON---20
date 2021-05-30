#program to give index values of all vowels present in a string

st='hello everyone'
vvl=['a','e','i','o','u']
l=[]
for i in range(len(st)) :
 if st[i] in vvl :
  l.append(i)
print('\nThe string is : {}.\nThe vowels are at index {}\n'.format(st,l))

#reverse the words of a string

s=('hello','world','happy','birthday')
ls=list(s)
print(type(s))
print('The string is :',s)
ls.reverse()
print(type(ls))
print(ls)

#program to print without duplicate elements

a=[1,2,3,2,1,1,1,1,1,1,4,5,6,2,100]
b=[]
for i in range(len(a)) :
 if a[i] in b :
  continue
 else :
  b.append(a[i])
print('\nThe list without repeated characters is :',b)


#Different method
q=[1,2,3,2,1,1,1,1,1,1,4,5,6,2,100]
w=[]
for i in q :
 if i in w :
  continue
 else :
  w.append(i)
print('\nThe list without repeated characters is :',b)

#Different method
a=[1,2,3,2,1,1,1,1,1,1,4,5,6,2,100]
b=[]
for i in a :
 if i not in b :
  b.append(i)
print('\nThe list without repeated characters is :',b)
