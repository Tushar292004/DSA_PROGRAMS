def merge_list(array):
    if len(array) <= 1:
        return(array)
    mid = len(array)//2

    left = array[:mid]
    right = array[mid:] 

    left_half = merge_list(left)
    right_half = merge_list(right)  

    return merge(left_half , right_half) 

def merge(left_half, right_half):
    result = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i]< right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1    
    
    result+= left_half[i:]
    result+= right_half[j:]
    return result


n = int(input("Enter the size of array : ")) 
array = []
for i in range (0,n):
    element = int(input("Enter the number : "))
    array.append(element)

print(merge_list(array))    

# OUTPUT1
# Enter the size of array : 4 
# Enter the number : 123
# Enter the number : 4
# Enter the number : 25
# Enter the number : 12
# [4, 12, 25, 123]