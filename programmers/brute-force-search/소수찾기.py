'''
* 🙆‍♂️ Created by wwlee94 on 2019.01.31
~~ TODO: 설명 추가 할 것
'''
import itertools
import math

def is_decimal(number):
    leng = int(math.sqrt(number))
    if number < 2: return False
    for i in range(2, leng+1):
        if number % i == 0: return False
    return True

def solution(numbers):
    answer = 0
    temp = []
    for i in range(len(numbers)):
        permutation = list(map(''.join, itertools.permutations([num for num in numbers], i+1)))
        temp += list(map(int, permutation))

    temp = list(set(temp))
    
    for val in temp:
        if is_decimal(val):
            answer += 1
    return answer