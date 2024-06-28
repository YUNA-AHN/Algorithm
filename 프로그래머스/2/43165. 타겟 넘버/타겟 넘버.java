// numbers를 더하고 빼며 que에 값을 입력
// que : (합, 인덱스 겸 카운팅)
import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Deque<ArrayList<Integer>> deq = new LinkedList<>();
        ArrayList<Integer> first = new ArrayList<>(List.of(0,0));
        deq.add(first); // 초기값 설정
        
        while (!deq.isEmpty()){
            Integer sum_v = deq.getFirst().get(0);
            Integer count = deq.getFirst().get(1);
            deq.removeFirst();
            // 한바퀴 다 돌았다면
            if (count == numbers.length) {
                if (sum_v == target) {
                    answer++;
                }
            } // 아직 덜 돌았다면
            else {
                // 값 더해주기
                ArrayList<Integer> plus = new ArrayList<>(List.of(sum_v + numbers[count], count + 1));
                // 값 지우기
                ArrayList<Integer> minus = new ArrayList<>(List.of(sum_v - numbers[count], count + 1));
                deq.add(plus);
                deq.add(minus);
            }
        }
        
        return answer;
    }
}