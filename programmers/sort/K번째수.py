'''
* 🙆‍♂️ Created by wwlee94 on 2020.02.01
- 문제 풀이법 작성할 것
'''
def solution(array, commands):
    answer = []
    for command in commands:
        slice_array = sorted(array[command[0]-1:command[1]])
        answer.append(slice_array[command[2]-1])
    return answer