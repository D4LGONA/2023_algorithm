import random
random.seed('class_04')
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
l_arr = len(words)

print('정렬 전: ', words)

# heap sort
def downHeap(root, size): # 정렬할 때 heapsize가 달라져야 해서 그런 거 입니다
    ch = root * 2 + 1 # parent와 비교할 애

    # pyramid of doom vs early return? if문을 여러개 돌리는거랑 리턴 갈기는 거군
    # 만약 그 조건이 맞으면 계속한다 vs 그 조건이 아니면 그만둔다(리턴, break)
    if ch >= size:  return # 자식이 존재하지 않으면 리턴(early return방식으로 합니다)
    if ch + 1 < size and words[ch] < words[ch + 1]: # right child가 존재한다는 의미 -> child끼리 비교 ㄱㄱ
                                                    # right child가 left보다 크다면 ch를 바꿈
        ch = ch + 1 # parent와 비교할 애를 right child로 바꾼다
    if words[root] >= words[ch]: return # 부모가 child보다 크면 return

    words[root], words[ch] = words[ch], words[root]
    downHeap(ch, size) # 재귀 호출 갈김 테일... 리쿼젼? 이 성능이 좋다는데

for i in range(l_arr // 2 - 1, -1, -1): # 14부터 0까지 돌아야 함
    downHeap(i, l_arr) # 아직은 l_arr이 힙사이즈랑 같음

print('최대힙 상태: ', words)

heapSize = l_arr # 이녀석을 줄여 나갈 것 임
for i in range(l_arr - 1, 0, -1): # 29부터 1까지 돌아야 함
    heapSize -= 1
    words[0], words[heapSize] = words[heapSize], words[0]
    downHeap(0, heapSize)

print('정렬 후: ', words)
