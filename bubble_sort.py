#compare first element with next if less then swap and take next element for compariosion
#do the same till the length of array
#start next iteration again from first element and repeat


def bubble_sort(arr):
    for i in range(1,len(arr)):
        for j in (range(len(arr)-i)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"array after {i}th iteration {arr}") 
    return arr


# arr = [1,2,3,4,5,6,7,8]
arr = [6,11,5,2,9,8,1,11,0]
# result =bubble_sort(arr)
# print(f"final result {result}")


'''
array after 0th iteration [6, 5, 2, 9, 8, 1, 11, 0, 11]
array after 1th iteration [5, 2, 6, 8, 1, 9, 0, 11, 11]
array after 2th iteration [2, 5, 6, 1, 8, 0, 9, 11, 11]
array after 3th iteration [2, 5, 1, 6, 0, 8, 9, 11, 11]
array after 4th iteration [2, 1, 5, 0, 6, 8, 9, 11, 11]
array after 5th iteration [1, 2, 0, 5, 6, 8, 9, 11, 11]
array after 6th iteration [1, 0, 2, 5, 6, 8, 9, 11, 11]
array after 7th iteration [0, 1, 2, 5, 6, 8, 9, 11, 11]
'''
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1-i):
#         if arr[j+1] < arr[j]:
#             arr[j+1],arr[j] = arr[j],arr[j+1]

#     print(f"array after {i}th iteration {arr}")

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
    print(f"arr value after {i}th iteration {arr}")