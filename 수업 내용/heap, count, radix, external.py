array = [
       46,      82,      21,      58,      22
]

def heapSort(arr):
    for i in range(len(arr) // 2, -1, -1):
        downHeap(arr, i, len(arr))
    print(arr)

    length = len(arr) - 1
    while length > 0:
        arr[0], arr[length] = arr[length], arr[0]
        length -= 1
        downHeap(arr, 0, length)

    print(arr)

# 젠장 !

def downHeap(arr, i, length):
    if i * 2 + 1 >= length: return
    if arr[i * 2 + 1] <= arr[i * 2 + 2]: # 오른쪽이 더 클때
        if arr[i] < arr[i * 2 + 2]:
            arr[i], arr[i * 2 + 2] = arr[i * 2 + 2], arr[i]
            downHeap(arr, i * 2 + 2, length)
    else: # 왼쪽이 더 클때
        if arr[i] < arr[i * 2 + 1]:
            arr[i], arr[i * 2 + 1] = arr[i * 2 + 1], arr[i]
            downHeap(arr, i * 2 + 1, length)

heapSort(array[:])  