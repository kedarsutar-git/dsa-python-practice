def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    return arr
arr = [12,332,1,34,21,43,56]
print(bubbleSort(arr))            

'''
Time Complexity: O(n^2)
space Complexity: O(1)
'''
