import java.util.*;
class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        // progresses와 speeds를 묶어 당을 deque
        Deque<LinkedList<Integer>> deq = new LinkedList<>();
        
        for (int i=0; i < progresses.length; i++) {
            // 조합을 담을 LinkedList
            LinkedList<Integer> comb = new LinkedList<>();
            comb.add(progresses[i]);
            comb.add(speeds[i]);
            // deq에 추가
            deq.add(comb);
        }
        
        // deq가 빌 때까지
        while (!deq.isEmpty()) {
            for (LinkedList<Integer> now : deq) {
                now.set(0, now.get(0) + now.get(1));
            }
            
            Boolean check = (deq.peekFirst().peekFirst() >= 100) ? true : false;
            if(check) {
                // deque을 순회하면서 완성된 만큼 pop 후 answer에 추가
                int ans = 0;

                while (!deq.isEmpty() && deq.peek().get(0) >= 100) {
                    deq.removeFirst();
                    ans++;
                }

                answer.add(ans);
            }
            
            
        }
        return answer;
    }
}