def binary_search(a,x):
    first_pos = 0
    last_pos = len(a) - 1
    flag = 0    # Flag to check if element is present or not in the list. If it's 1 then element is present otherwise not.

    count = 0

    while(first_pos <= last_pos and flag == 0):
        count+=1
        mid = (first_pos + last_pos)//2
        if x==a[mid]:
            flag = 1
            print("the element present at pos : "+str(mid))
            print("the number of iterations are : "+str(count))
        else:
            if x<a[mid]:
                last_pos = mid-1
            else:
                first_pos = mid+1
        
print("the number is not present")

a = []
for i in range(1,501):
    a.append(i)

binary_search(a,70)