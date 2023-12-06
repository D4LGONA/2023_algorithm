array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,      35, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,      68, 
]

def bubble_sort(arr):
  print('-' * 60)
  print('Bubble Sort')
  print(f'before: {arr}')
  count = len(arr)
  for a in range(count - 1): 
    for b in range(count - 1 - a): 
      if arr[b] > arr[b + 1]: 
        arr[b], arr[b + 1] = arr[b + 1], arr[b] 
  print(f'after : {arr}')

def select_sort(arr):
  print('-' * 60)
  print('Selection Sort')
  print(f'before: {arr}')
  count = len(arr)
  for i in range(count - 1):
    min = i
    for j in range(i + 1, count, 1):
      if(arr[j] < arr[min]):
        min = j
    arr[i], arr[min] = arr[min], arr[i]
  print(f'after : {arr}')

def insert_sort(arr):
  print('-' * 60)
  print('Insertion Sort')
  print(f'before: {arr}')
  count = len(arr)
  for i in range(1, count):
    tmp = arr[i]
    for j in range(i, 0, -1):
      if tmp < arr[j - 1]:
        arr[j] = arr[j - 1]
      else:
        arr[j] = tmp
        break
  print(f'after : {arr}')

def shell_sort(arr):
  print('-' * 60)
  print('Shell Sort')
  print(f'before: {arr}')
  count = len(arr)
  gap = count // 3
  while gap > 0:
    if gap < 3 and gap != 1:
      gap = 1
    for i in range(gap, count, 1):
      tmp = arr[i]
      for j in range(i, 0, -gap):
        if tmp < arr[j - gap]:
          arr[j], arr[j - gap] = arr[j - gap], arr[j]
        else:
          break
    gap //= 3
  print(f'after : {arr}')

def main():
  bubble_sort(array[:])
  select_sort(array[:])
  insert_sort(array[:])
  shell_sort(array[:])

if __name__ == '__main__':
  main()

