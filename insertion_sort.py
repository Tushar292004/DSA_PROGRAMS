#insertion sort program

def insertion(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1 
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j-=1
            array[j+1] = key

        return array

n = int(input("Enter the size of array : ")) 
array = []
for i in range (0,n):
    element = int(input("Enter the number : "))
    array.append(element)

print(insertion(array))

# OUTPUT1
# Enter the size of array : 4 
# Enter the number : 123
# Enter the number : 4
# Enter the number : 25
# Enter the number : 12