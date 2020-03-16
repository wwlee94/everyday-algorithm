/*
* 🙆‍♂️ Created by wwlee94 on 2020.03.14
https://programmers.co.kr/learn/courses/30/lessons/42627
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