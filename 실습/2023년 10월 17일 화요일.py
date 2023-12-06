#2023년 10월 17일 화요일
import random

random.seed('class_04')
array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)

def partition(arr, beg, end): # end:exclusive
    ri = random.randrange(beg, end)
    arr[beg], arr[ri] = arr[ri], arr[beg]
    pv = arr[beg]

    p, q = beg, end
    while True:
        while True: # p 증가
            p += 1
            if p >= q: break
            if arr[p] > pv: break
        while True: # q 감소
            q -= 1
            if q < p : break
            if arr[q] <= pv: break
        if p >= q: break
        arr[p], arr[q] = arr[q], arr[p]
    
    arr[q], arr[beg] = arr[beg], arr[q]
    return q

def quickSort(arr, beg, end): # end:exclusive
    size = end - beg
    if size <= 1 : return
    pi = partition(arr, beg, end)
    quickSort(arr, beg, pi)
    quickSort(arr, pi + 1, end)

quickSort(array, 0, l_arr)
print(array)


# merge sort #
# # 1번 선택 - array를 전달하지 않도록 해요
# # 2번 선택 - 마지막 숫자 포함 하기
# # 3번 선택 - 왼쪽에 포함 시키기
# # 4번 선택 - mid 전달하기!

# def merge(start, mid, end):
#     #global array
#     merged = [] # 여기에 줄 세울 것
#     l, r = start, mid + 1 # mid is in left, end is inclusive
#     while l <= mid and r <= end: # A반에 선수있다 and B반에 선수있다
#         if array[l] <= array[r]: # A반선수가 지면
#             merged.append(array[l]) # A반 선수 줄세우기
#             l += 1
#         else: # B반선수가 지면
#             merged.append(array[r]) # B반 선수 줄세우기
#             r += 1

#     if l <= mid: # A반에 선수가 남아있다면
#         merged += array[l:mid + 1] # append로 하면 배열 자체가 추가됨
#         array[start:end + 1] = merged
#     else: # B반에 선수가 남아있다면
#         #merged += array[r:end + 1]
#         array[start:r] = merged

#     # while l <= mid: 
#     #     merged.append(array[l]) # A반 선수 줄세우기
#     #     l += 1
#     # while r <= end: 
#     #     merged.append(array[r]) # B반 선수 줄세우기
#     #     r += 1

# def mergeSort(start, end): # start부터 end까지
#     # size = end - start + 1 
#     # if size <= 1: return
#     if start >= end: return

#     mid = (start + end) // 2 # mid is in left
#     mergeSort(start, mid)
#     mergeSort(mid + 1, end)
#     merge(start, mid, end)

# mergeSort(0, l_arr - 1)
# print(array)