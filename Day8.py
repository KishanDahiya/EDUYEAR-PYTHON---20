all_course= ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang', 'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']
user_list = {} #empty dictionary for a single user
data = input('\nEnter name & email seperated by "-" : ') #taking values with : to split later 
user_list['name'],user_list['email']= data.split('-') #unpacking values at ':' and assigning to respective keys in dictionary
user_list['courses']=[] #empty values ,no courses enrolled
t=[] #temperory list to append new enrolled courses

while True :
 print('\n1.All courses\n2.My courses\n3.Show profile\n0.Exit')
 choice=int(input('Enter your choice : '))
 if choice==0 :
  exit(1)
 elif choice==1 :
  #print('\nThe Courses are as below\n','\n'.join(all_course))#displaying all list elements in new lines with 'sep'.join(list_name)
  for i in range(len(all_course)) :
   print(f'{i+1}.{all_course[i]}')
  c_choice=int(input('\nSelect a course(number) : '))
  if all_course[c_choice-1] in t :
    print('\nAlready enrolled for this course')
    continue
  else:
    t.append(all_course[c_choice-1])
  #t.append((input('\nSelect a course : ')))#appending a temperory list with new courses
  user_list['courses']=t #assigning the list of course to key,where its storing mutiple values than overwrting (because we used list and assigned)
 elif choice==2 :
  if user_list['courses']==[] :
   print('\nNo courses enrolled yet!!!')
  else :
   print('\nYour enrolled courses are as below')
   for i in range(len(user_list['courses'])):               
    print(f"{i+1}.{user_list['courses'][i]}")#display all courses enrolled
 elif choice==3 :
  for k,v in user_list.items(): #Displaying the dictionary  
    if k=='courses':
     continue
    else :
     print(k,':',v)
	
