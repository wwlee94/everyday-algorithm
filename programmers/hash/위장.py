'''
* 🤷‍♂️ Created by wwlee94 on 2020.02.20
- 문제 풀이 방식 -
Counter 모듈로 각 의상 종류별 개수를 구하고
(의상 종류 + 1) * ... 하면 모든 경우의 수를 구할 수 있음

* 마지막 -1을 하는 이유
의상을 3개일 때 고르는 경우는 안입는것, 첫번째, 두번째, 세번째 총 4개의 선택이 가능하고 부위별로 가능한 선택 수를 곱하면 모든 조합이 나오는데 최소 하나는 입어야 해서 1을 뺀 경우 !

'''
from collections import Counter
def solution(clothes):
    answer = 1
    cnt = Counter([kind for name, kind in clothes])
    
    for key in cnt:
        answer *= (cnt[key]+1) # (의상 종류 + 1)

    return answer-1 # 하나도 안 입은 경우 제외