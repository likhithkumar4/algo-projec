def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
    	if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
    


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:     
        pi = partition(arr, low, high)
        print(arr)
        
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
print("Enter elements: ")
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print("Entered Array is: ",lst)
arr = lst
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted Array is: ", end="", flush=True)
print(arr)
print("\n")
w = int(input("Enter the element to search: "))

for i in range(0,n):
    if arr[i]==w:
        print('Element found at',i+1,'location')
        break
    else:
        i=i+1
        if i==n-1:
            print('Not found!')
        continue
    
