#Simple program to count age

x=2021
y=int(input("Enter the year you were born in.\n"))
check=str(input('Did your birthday pass this year?\nAnswer in yes or no\n'))
print(check)
if check=='yes' :
               print('You are',x-y,'years old.')
elif check=='no' :
               print('You are',(x-y)-1,'years old.')
else :
               print('Enter the correct response')
