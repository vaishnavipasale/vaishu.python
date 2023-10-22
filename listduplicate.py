Create a list of unique elements from a list with duplicates.
(lst, duplicate) = ([], []) 
N = int(input('Enter the size of list='))
 

for i in range(N):
    ele = input('Enter the ' + str(i + 1) + ' element= ')
    lst.append(ele)
 

print ('The original list is=', lst)
 

for i in range(N):
    check = lst[i]
 
  
    for j in range(i + 1, N):
        if check == lst[j]:
            duplicate.append(check)
 
print ( duplicate)
