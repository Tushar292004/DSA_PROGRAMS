
def quick(array):
    if len(array) <= 1:
        return array

    #using quick sort here
    pivot = array[0]
    left=[]
    right=[]

    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i]) 
        else:
            right.append(array[i]) 
    return quick(left)+ [pivot] + quick(right)              

n = int(input("Enter the size of array : ")) 
array = []
for i in range (0,n):
    element = int(input("Enter the number : "))
    array.append(element)

print(quick(array))

# OUTPUT1
# Enter the size of array : 4 
# Enter the number : 123
# Enter the number : 4
# Enter the number : 25
# Enter the number : 12