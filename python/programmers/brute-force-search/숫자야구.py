'''
* 🙆‍♂️ Created by wwlee94 on 2020.02.26
https://programmers.co.kr/learn/courses/30/lessons/42841?language=python3

- 문제 풀이 접근법 -
*작성할 것
'''
import itertools

def solution(baseball):
    answer = 0
    leng = len(baseball)
    all_case = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
    
    for case in all_case:
        count = 0 # 질문을 만족한 개수
        for item in baseball:
            strike = 0
            # question = [item[0] // 100, item[0] % 100 // 10, item[0] % 10]
            question = [int(i) for i in str(item[0])]

            #첫번째 방법 - strike 개수 우선 구한 후 ball 개수 구함
            for i in range(3):
                if case[i] == question[i]: strike += 1
            if item[1] != strike: break
                
            ball = len(set(case) & set(question)) - strike # 교집합의 크기를 구한 후 strike 개수 빼준 것
            if item[2] != ball: break
                
            count += 1
            
            # 두번째 방법(원래 풀이) - 2중 for문으로 strike, ball 구한 것
            # for i in range(3):
            #     for j in range(3):
            #         if i==j and case[i] == question[j]: strike += 1
            #         elif case[i] == question[j]: ball += 1
            # if item[1] != strike or item[2] != ball: break
            # else: count += 1
                
        if count == leng: answer += 1 # 질문 개수 만큼 돌아야 조건을 모두 만족한 경우이기 때문
    return answer