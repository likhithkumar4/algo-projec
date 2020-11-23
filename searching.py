def search(nums, target):
    low = 0
    high = len(nums)
    while low<high:
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        if nums[low]<=nums[mid]:
            if target >=nums[low] and target <nums[mid]:
                high = mid
            else:
                low = mid+1
        else:
            if target<=nums[high-1] and target>nums[mid]:
                low = mid+1
            else:
                 high = mid
    return -1
arr =[]
n = int(input("Enter number of elements : "))
print("Enter elements ")
for i in range(0, n): 
    ele = int(input())
    arr.append(ele)

print("Entered Array", arr)
x = search(arr, 5)
if x == -1:
    print("Element not found ")
else:
    print("same element found at",x,"location")

    
