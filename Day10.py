'''printing a particular pattern of numbers without using loop,use reccursion functions'''

def f1(t):
  print(t)
  if t<0 :
    return
  f1(t-5)
  print(t)

def f2(v):
  print(v)
  if v==0 :
    return 
  f2(v-5)
  print(v)
  
f1(16)
print('\n')
f2(10)

