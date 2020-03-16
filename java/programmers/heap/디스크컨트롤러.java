/*
* 🙆‍♂️ Created by wwlee94 on 2020.03.14
https://programmers.co.kr/learn/courses/30/lessons/42627

- PriorityQueue 클래스 사용 -
메소드 
1. 삽입 - offer, add
2. 제거 - poll, remove
3. 읽기 - peek, element
offer, poll, peek -> 큐가 비어있으면 null 반환
add, remove, element -> 큐가 비어있으면 예외 발생

- 번외 -
- Array를 첫번째 또는 두번째 Element로 정렬하기 -
1. 첫번째 또는 두번째 Element로 정렬하기
Arrays.sort(arr, Comparator.comparing(o1 -> o1[0]));
Arrays.sort(arr, Comparator.comparing(o1 -> o1[1]));

2. 두가지 기준으로 정렬
Arrays.sort(arr, (o1, o2) -> {
    if (o1[0] == o2[0]){
        return Integer.compare(o1[1], o2[1]);
    } else{
        return Integer.compare(o1[0], o2[0]);
    }
});
*/
import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int length = jobs.length;
        int pre = -1; // 입력된 시간
        int now = 0; // 종료된 시간
        // 자바는 기본 정렬를 바꾸게하는 Comparator를 제공
        PriorityQueue<int[]> wait = new PriorityQueue<>((o1, o2) -> (o1[1] - o2[1]));
        
        int count = 0; // 종료된 프로세스 개수
        while(count != length){
            for(int i=0;i<length;i++){
                int req = jobs[i][0];
                int time = jobs[i][1];
                // pre == req 인 경우는 우선순위를 따져야함
                if(req > pre && req <= now){
                    int[] arr = {req, time};
                    wait.offer(arr);
                }
            }
            if(wait.size() > 0){
                int[] job = wait.poll();
                pre = now;
                now += job[1];
                answer += now - job[0];
                count += 1;
            }
            else now += 1;
        }
        return (int)(answer / length);
    }
}