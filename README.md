# 💻 algorithm-python
매일 Python으로 푸는 알고리즘 문제 풀이 !

## 💁‍♂️ 나만의 Rule 정하기 !
* 하루에 최소 1개의 알고리즘 문제 풀기 
* 못 푸는 문제라도 최대한 고민해보기
* 누구나 보아도 이해 할 수 있는 코드와 풀이를 작성하려고 노력하기

## 👨‍💻 문제 풀이 및 코드

### 프로그래머스
1. 스택 / 큐
    * [탑](https://github.com/wwlee94/algorithm-python/blob/master/programmers/stack-queue/탑.py)
    * [다리를 지나는 트럭](https://github.com/wwlee94/algorithm-python/blob/master/programmers/stack-queue/다리를지나는트럭.py)
2. 해쉬
  * [전화번호 목록](https://github.com/wwlee94/algorithm-python/blob/master/programmers/hash/전화번호목록.py)
  * [베스트 앨범](https://github.com/wwlee94/algorithm-python/blob/master/programmers/hash/베스트앨범.py)
    
## 알고리즘 사이트
* [프로그래머스](https://programmers.co.kr)

## Python 자료형 별 주요 연산자 시간 복잡도

알고리즘 문제를 풀다 보면 시간복잡도를 생각해야 하는 경우가 종종 생긴다.  
시간복잡도 기준이 있어서, 기준을 넘기지 못하면 문제를 풀어도 틀리는 경우가 생긴다.

## list

| Operation | Example | Big-O | Notes |
| --- | --- | --- | --- |
| Index | l[i] | O(1) |   |
| Store | l[i] = 0 | O(1) |   |
| Length | len(l) | O(1) |   |
| Append | l.append(5) | O(1) |   |
| Pop | l.pop() | O(1) | l.pop(-1) 과 동일 |
| Clear | l.clear() | O(1) | l = [] 과 유사 |
| Slice | l[a:b] | O(b-a) | l[:] : O(len(l)-0) = O(N) |
| Extend | l.extend(…) | O(len(…)) | 확장 길이에 따라 |
| Construction | list(…) | O(len(…)) | 요소 길이에 따라 |
| check ==, != | l1 == l2 | O(N) | 비교 |
| Insert | ㅣ.insert(i, v) | O(N) | i 위치에 v를 추가 |
| Delete | del l[i] | O(N) |   |
| Remove | l.remove(…) | O(N) |   |
| Containment | x in/not in l | O(N) | 검색 |
| Copy | l.copy() | O(N) | l[:] 과 동일 - O(N) |
| Pop | l.pop(i) | O(N) | l.pop(0):O(N) |
| Extreme value | min(l)/max(l) | O(N) | 검색 |
| Reverse | l.reverse() | O(N) | 그대로 반대로 |
| Iteration | for v in l: | O(N) |   |
| Sort | l.sort() | O(N Log N) |   |
| Multiply | k*l | O(k N) | [1,2,3] * 3 » O(N**2) |

## Dict

| Operation | Example | Big-O | Notes |
| --- | --- | --- | --- |
| Index | d[k] | O(1) |   |
| Store | d[k] = v | O(1) |   |
| Length | len(d) | O(1) |   |
| Delete | del d[k] | O(1) |   |
| get/setdefault | d.method | O(1) |   |
| Pop | d.pop(k) | O(1) |   |
| Pop item | d.popitem() | O(1) |   |
| Clear | d.clear() | O(1) | s = {} or = dict() 유사 |
| View | d.keys() | O(1) | d.values() 동일 |
| Construction | dict(…) | O(len(…)) |   |
| Iteration | for k in d: | O(N) |   |

### References (참고 사이트)
<ul>
  <li><a href="https://wiki.python.org/moin/TimeComplexity">Python wiki’s Time Complexity</a></li>
  <li><a href="https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt">Complexity of Python Operations</a></li>
</ul>
