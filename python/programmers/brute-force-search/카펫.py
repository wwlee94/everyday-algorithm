'''
* 🤷‍♂️ Created by wwlee94 on 2020.03.06
https://programmers.co.kr/learn/courses/30/lessons/42842

- 문제 풀이 접근 -
brown은 테두리이고 red는 안을 꽉 채워둔 카펫 모양임을 꼭 ! 인지해야함
brown, red의 개수로 만들 수 있는 경우의 수를 모두 완전 탐색
조건 1. 가로 * 세로 = brown+red 조건
조건 2. brown >= red
조건 3. 조건1, 조건2를 통해 나온 가로, 세로 값으로 red카펫의 크기를 검사해야함

번외) 아마 조건 3을 만족하는 결과가 테스트 4, 6, 7 인듯함
'''
def solution(brown, red):
    answer = 0
    total = brown + red
    for row in range(1, total+1):
        if total % row == 0: 
            col = total // row
            if row >= col: 
                if (row-2) * (col-2) == red: # brown은 테두리, 안에는 모두 red로 채워져 있으므로
                    return [row, col]