def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while (left<=right):
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=list(map(int,input('enter sorted arry').split()))
target=int(input('enter the target'))
result=binary_search(arr,target)
if result!=-1:
    print(f"{result}")  
else:
    print("not found")