def merge_sort(arr): 
#base case
    if len(arr)<=1: 
        return arr
    mid=len(arr)//2 
    #split the data into half 
    left_half=merge_sort(arr[:mid]) 
    right_half=merge_sort(arr[mid:]) 
 
     #merge the array 
    return merge(left_half,right_half) 
 
def merge(left,right): 
    sorted_array=[] 
    while left and right: 
        if left[0]<right[0]: 
            sorted_array.append(left.pop(0)) 
           
        else: 
            sorted_array.append(right.pop(0)) 
    sorted_array.extend(left or right) 
    return sorted_array 
 
# test 
array = input("Enter elements of array separated by space: ") 
array = [int(x) for x in array.split()]   
print("Array : ",array) 
sorted_array=merge_sort(array) 
print("Sorted Array : ",sorted_array)


 
#b. Binary Search 
def binary_search(arr,target):
    left,right=0,len(arr)-1 
    while left<=right: 
        mid=(left+right)//2 
        if arr[mid]==target: 
            return mid  #target found at index 
        elif arr[mid]<target: 
            left=mid+1  #ignore left half 
        else: 
            right=mid-1  #ignore right half 
    return -1   #target not found 
 
#test 
sorted_array = input("Enter elements of array separated by space: ") 
sorted_array = [int(x) for x in sorted_array.split()]   
target=int(input("Enter target to search : ")) 
result=binary_search(sorted_array,target) 
 
if result!=-1: 
    print(f"Element {target} found at index {result}") 
else: 
    print(f"Element {target} not found in the array") 
