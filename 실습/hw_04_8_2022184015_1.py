words = [
  '2022184015', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody', 
  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',
  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',
  'temporize', 'speedboat', 'agenda', 'delusion', 'class04', 'idolize', 'romance', 'overestimate', 'revive', 'smell', 
  'modem', 'splat', 'snaky', 'drawn', 'smoke', 'darky', 'lotus', 'mufti', 'pithy', 'jewel', 'nexus',
  'fluff', 'piton', 'finis', 'drake', 'caulk', 'pussy', 'bless', 'weeds', 'realm', 'swoon', 'thorn', 
  'plant', 'aorta', 'cupid', 'wafer', 'jewry', 'sinus', 'proud', 'grape', 'cable', 'carer', 'pearl', 
  'piece', 'party', 'sleet', 'palmy', 'oiled', 'synod', 'trove', 'voice', 'chest', 'story', 'range', 
  'scout', 'sewer', 'lowly', 'usher', 'seine', 'gulch', 'fever', 'frith', 'pylon', 'wager', 'banns', 
  'merit', 'cheap', 'booby', 'truss', 'codex', 'sepia', 'totem', 'poult', 'dregs', 'giddy', 'umber', 
  'mooch', 'smarm', 'loath', 'spoil', 'drink', 'wrick', 'awake', 'mural', 'glide', 'pinch', 'thine', 
  'tawny', 'swede', 'shier', 'satan', 'triad', 'splay', 'tacit', 
]

# merge sort #
# 1번 선택 - array를 전달하지 않도록 해요
# 2번 선택 - 마지막 숫자 포함 하기
# 3번 선택 - 왼쪽에 포함 시키기
# 4번 선택 - mid 전달하기!

def merge(start, mid, end):
    merged = [] # 여기에 줄 세울 것
    l, r = start, mid + 1 # mid is in left, end is inclusive
    while l <= mid and r <= end: # A반에 선수있다 and B반에 선수있다
        if words[l] <= words[r]: # A반선수가 지면
            merged.append(words[l]) # A반 선수 줄세우기
            l += 1
        else: # B반선수가 지면
            merged.append(words[r]) # B반 선수 줄세우기
            r += 1

    if l <= mid: # A반에 선수가 남아있다면
        merged += words[l:mid + 1] # append로 하면 배열 자체가 추가됨
        words[start:end + 1] = merged
    else: # B반에 선수가 남아있다면
        words[start:r] = merged

def mergeSort(start, end): # start부터 end까지
    if start >= end: return

    mid = (start + end) // 2 # mid is in left
    mergeSort(start, mid)
    mergeSort(mid + 1, end)
    merge(start, mid, end)

mergeSort(0, len(words) - 1)
print(words)