from random import *

array = [randint(0, 100) for _ in range(10)]


#heap sort
def max_heap(arr, index, size): # 정렬할 배열, 현재 탐색할 노드, 배열 크기 인듯
    # size를 넘겨주는 이유: 힙정렬을 수행하는 동안 길이가 계속 짧아지기 때문
    # arr은 필요없음
    largest = index 
    left_index = 2 * index + 1 # 왼쪽 자식
    right_index = 2 * index + 2 # 오른쪽 자식

    # 교수님의 코드는 둘다 존재하면 둘이 비교하고 하나만 존재하면 미리 하는데, 
    # 여기선 둘다 비교해보고 큰놈을 따로 변수에 넣어서 처리하는 군

    if left_index < size and arr[left_index] > arr[largest]:
        # 왼쪽 자식이 존재하고 검사중인 녀석보다 값이 크다면
        largest = left_index # 왼쪽 자식이 가장 크게 되겠군
    if right_index < size and arr[right_index] > arr[largest]:
        # 오른쪽 자식이 존재하고 
        largest = right_index #오른쪽 자식이 가장 크게 되겠군
    if largest != index: # 만약 바뀌었다면
        arr[largest], arr[index] = arr[index], arr[largest] # swap
        max_heap(arr, largest, size) # 그 녀석의 밑으로 최대힙 ㄱㄱ

def heap_sort(unsorted):
    n = len(unsorted) # 현재 배열의 길이, 10이 나올 것
    for i in range(n // 2 - 1, -1, -1): # 4부터, -1씩, 0번까지 -> 처음 최대 힙 만드는 작업, 
        max_heap(unsorted, i, n)
    for i in range(n - 1, 0, -1): # n-1부터, 1까지, -1씩.
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        max_heap(unsorted, 0, i)
    return unsorted


def merge_sort(arr): # 머지 소트 해 봅시다
    if len(arr) <= 1: # 배열의 크기가 1 이하면 return
        # 교수님은 merge sort를 배열의 첫번째, 마지막 ㅣㄴ덱스로 해서
        return arr

    # 중간을 기준으로 배열을 나누기
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    array = result



print("start: " ,  array)
#heap_sort(array)
merge_sort(array)
print("end: " ,  array)