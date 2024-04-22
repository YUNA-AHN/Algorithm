import java.util.ArrayList;
class Solution {
    public ArrayList<Long> solution(int x, int n) {
        ArrayList<Long> answer = new ArrayList<Long>() ;
        // n개까지
        for (long i = 0; i < n; i ++) {
            answer.add(x + x*i);
        }
        return answer;
    }
}