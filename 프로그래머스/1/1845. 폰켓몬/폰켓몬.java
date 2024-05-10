// N/2 마리의 폰켓몬 선택시 최대
import java.util.HashSet;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        for (int num : nums) {
            set.add(num);
        }
        // N/2 보다 크면 N/2, 작으면 set 크기
        answer = (set.size() > nums.length / 2) ? nums.length / 2 : set.size();
        return answer;
    }
}