# one based index를 쓸 것
d = [5,9,3,7,2,6,3,9,3]
mc = len(d) - 1

INF = float('inf')
C = [[0 for _ in d] for _ in d] # range(mc+1) 이랑 d랑 같음
P = [[0 for _ in d] for _ in d]

for sps in range(2, mc + 1) : # 문제의 크기를 2부터 늘려나가는 녀석?
  for s in range(1, mc - sps + 2) :
    e = s + sps - 1 # e는 포함
    mult = INF
    for k in range(s, e) :
      t = C[s][k] + C[k + 1][e] + d[s-1] * d[k] * d[e] #s의 행 k의 열
      if mult > t:
        mult = t
        P[s][e] = k
    C[s][e] = mult

def getMultStr(s, e):
  if s == e: return f'A{s}'
  p = P[s][e]
  return f'({getMultStr(s,p)}x{getMultStr(p+1,e)})'

print(f'mul_count = {C[1][mc]} cal = {getMultStr(1, mc)}')