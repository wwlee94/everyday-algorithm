'''
* Created by wwlee94 on 2019.01.09
문제의 설명 순서에 따라 코드를 짜면 풀 수 있는 문제
1. 종료 조건 찾기 -> 도착한 트럭의 개수가 첫 시작 트럭의 개수와 일치할 때
2. 다리를 건너는 트럭 리스트 추가 조건 -> 견디는 무게 >= 현재 다리를 건너는 트럭의 무게 + 다음 첫번째 대기 트럭의 무게 
3. 현재 다리를 건너는 트럭들의 이동 거리 조정해 준 후 도착한 트럭 찾기 
'''
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    # truck_times = [bridge_length] * len(truck_weights)
    truck_count = len(truck_weights)
    truck_times = []
    truck_crossing = []
    truck_arrived = []
    
    while True:
        time += 1
        if len(truck_arrived) == truck_count: break
        if len(truck_weights) != 0:
            if weight >= sum(truck_crossing) + truck_weights[0]:
                truck_crossing.append(truck_weights.pop(0))
                truck_times.append(bridge_length)
                
        truck_times = list(map(lambda x: x-1, truck_times))
        if truck_times[0] == 0:
            truck_times.pop(0)
            truck_arrived.append(truck_crossing.pop(0))        
    return time