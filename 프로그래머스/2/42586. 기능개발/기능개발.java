import java.util.*;
class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Deque<Deque<Integer>> deq = new LinkedList<>();
        for (int idx = 0 ; idx < progresses.length; idx++){
            Deque<Integer> preSpeed = new LinkedList<>(); // 과정 + speed를 묶어서 저장
            preSpeed.add(progresses[idx]);
            preSpeed.add(speeds[idx]);
            deq.add(preSpeed);
        }
        // 한바퀴씩 돌면서 speeds 만큼 더해줌
        // 더한 뒤에 100 넘는 친구는 빼주기
        while (!deq.isEmpty()){
            for (Deque<Integer> now : deq) {
                // speed 만큼 더하기
                int progress = now.peekFirst() + now.peekLast();
                now.removeFirst();
                now.addFirst(progress);
            }
            
            Boolean check = (deq.peekFirst().peekFirst() >= 100) ? true : false;
            // System.out.println(deq.toString());
            // System.out.println(check);
            if (check) {
                int deploy = 0;
                while (!deq.isEmpty() && deq.peekFirst().peekFirst() >= 100){
                    deq.removeFirst();
                    deploy++;
                }
                answer.add(deploy);
            }
        }
        return answer;
    }
}