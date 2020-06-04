'''
* 🤷‍♂️ Created by wwlee94 on 2020.06.04
https://programmers.co.kr/learn/courses/30/lessons/17684
'''
def solution(msg):
    answer = []
    dic = {}
    
    ch = 65 # 'A'
    num = 1
    while ch != 91:
        dic.update({ chr(ch): num })
        ch = ch + 1
        num += 1

    idx = 0
    maxIdx = 27
    length = 1
    answer = []
    while True:
        length += 1
        _input = msg[idx:idx+length-1]
        _next = msg[idx:idx+length]
        if _next not in dic:
            answer.append(dic[_input])
            dic[_next] = maxIdx
            maxIdx += 1
            idx += length-1
            length = 1
        else:
            if idx+length-1 == len(msg):
                answer.append(dic[_input])
                break
    return answer