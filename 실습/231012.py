# radix sort #
import random
random.seed('class_04')
array = [random.randrange(1000) for _ in range(10)]
l_arr = len(array)
maxv = max(array)
print(array, maxv)

results = array[:] # array와 같은 크기의 배열로 만들어놓기만 해도 됨

div = 1 # 자릿수를 정의하는 친구
while div <= maxv: # 100일때, 1000일때 생각해서 등호를 붙여야 함
    counts = [0 for _ in range(10)] # 각 자리수는 0~9 10종류 뿐
    for v in array:
        digit = v // div % 10
        counts[digit] += 1

    for i in range(len(counts) - 1): # 9번 돌려야 함, count를 index로
        counts[i+1] += counts[i]

    for i in range(l_arr - 1, -1, -1): # 99부터 0까지 돌아야 하는군
        v = array[i]
        digit = v // div % 10
        counts[digit] -= 1
        ri = counts[digit]
        results[ri] = v # result를 array랑 같이 쓸 수 없음(새 배열 필요)
    array = results[:] # 원래 array로 복사 갈겨야 함 복사 안하고 그냥 대입해도 위에서 복사해서 ㄱㅊ다네요ㅋㅋㅋ
    print(results, div)

    div *= 10 # 1, 10, 100, 1000 ... 

# count sort #
# import random
# random.seed('class_04')
# array = [random.randrange(15) for _ in range(10)]
# l_arr = len(array)
# maxv = max(array)
# print(array, maxv)
# counts = [0 for _ in range(maxv+1)]
# print(counts, len(counts))

# for v in array:
#     counts[v] += 1
# print(counts, len(counts))

# for i in range(len(counts) - 1): # 14번 돌려야 함
#     counts[i+1] += counts[i]
# print(counts, len(counts))

# # results = [None for _ in range(l_arr)]
# # results = [None] * l_arr
# results = array[:]
# for i in range(l_arr - 1, -1, -1): # 99부터 0까지 돌아야 하는군
#     v = array[i]
#     counts[v] -= 1
#     ri = counts[v]
#     results[ri] = v # result를 array랑 같이 쓸 수 없음(새 배열 필요)
#     print(results)


# heap sort #
# import random
# random.seed('class_04')
# array = [random.randrange(100) for _ in range(30)]
# l_arr = len(array)
# print(array)

# array = list(map(lambda e: -e, array)) # 모든 원소를 음수로 바꿈, 원래값 유지: (-e, e) 로 적으면 됨, heapify가 첫번째 원소로 하기 때문에 정렬 됨 !!
# print (array)
# import heapq
# heapq.heapify(array) # min heap만 만들 수 있음
# print(array)

# # heap sort
# def downHeap(root, size): # 정렬할 때 heapsize가 달라져야 해서 그런 거 입니다
#     ch = root * 2 + 1 # parent와 비교할 애

#     # pyramid of doom vs early return? if문을 여러개 돌리는거랑 리턴 갈기는 거군
#     # 만약 그 조건이 맞으면 계속한다 vs 그 조건이 아니면 그만둔다(리턴, break)
#     if ch >= size:  return # 자식이 존재하지 않으면 리턴(early return방식으로 합니다)
#     if ch + 1 < size and array[ch] < array[ch + 1]: # right child가 존재한다는 의미 -> child끼리 비교 ㄱㄱ
#                                                     # right child가 left보다 크다면 ch를 바꿈
#         ch = ch + 1 # parent와 비교할 애를 right child로 바꾼다
#     if array[root] >= array[ch]: return # 부모가 child보다 크면 return

#     array[root], array[ch] = array[ch], array[root]
#     downHeap(ch, size) # 재귀 호출 갈김 테일... 리쿼젼? 이 성능이 좋다는데

# for i in range(l_arr // 2 - 1, -1, -1): # 14부터 0까지 돌아야 함
#     downHeap(i, l_arr) # 아직은 l_arr이 힙사이즈랑 같음

# print(array)

# heapSize = l_arr # 이녀석을 줄여 나갈 것 임
# for i in range(l_arr - 1, 0, -1): # 29부터 1까지 돌아야 함
#     heapSize -= 1
#     array[0], array[heapSize] = array[heapSize], array[0]
#     downHeap(0, heapSize)

# print(array)
