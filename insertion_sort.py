#compare first element with next element 
#if next element is less than first then swap both and start from the first position
#if not less then go for next element till length of array
#after complete iteration start from next element till the length of an array and continue
arr = [8,4,10,20,6,2,1]
        
# arr = [10,20,8,6,4,2,1]
for i in range(1,len(arr)):
    for j in range(i):
        if arr[j] > arr[i]:
            arr[i],arr[j] = arr[j],arr[i]    
    print(f"array after {j}th iteration {arr}")
print("final result of sorting",arr)

#time complexity O(n^2)

# arr = [10,20,8,6,4,2,1]
# arr = [8,4,10,20,6,2,1]
'''
array start of sorting :[8, 4, 10, 20, 6, 2, 1]
array after 1th iteration [4, 8, 10, 20, 6, 2, 1]
array after 2th iteration [4, 8, 10, 20, 6, 2, 1]
array after 3th iteration [4, 8, 10, 20, 6, 2, 1]
array after 4th iteration [4, 6, 8, 10, 20, 2, 1]
array after 5th iteration [2, 4, 6, 8, 10, 20, 1]
array after 6th iteration [1, 2, 4, 6, 8, 10, 20]
array end of sorting :[1, 2, 4, 6, 8, 10, 20]
'''

# print(f"array start of sorting :{arr}") 
# for i in range(1,len(arr)):
#     for j in range(i):
#         if arr[j] > arr[i]:
#             arr[i],arr[j] = arr[j],arr[i]
#     print(f"array after {i}th iteration {arr}") 
# print(f"array end of sorting :{arr}") 

# # Traverse through 1 to len(arr)
# for i in range(1, len(arr)):

#     key = arr[i]

#     # Move elements of arr[0..i-1], that are
#     # greater than key, to one position ahead
#     # of their current position
#     j = i-1
#     while j >= 0 and key < arr[j] :
#             arr[j + 1] = arr[j]
#             j -= 1
#     arr[j + 1] = key
#     print(f"array after {i}th iteration {arr}") 
    