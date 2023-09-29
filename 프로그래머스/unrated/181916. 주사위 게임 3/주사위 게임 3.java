import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Comparator;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        HashSet <Integer> hashset = new HashSet<>(Arrays.asList(a,b,c,d));
        ArrayList <Integer> list = new ArrayList<>(Arrays.asList(a,b,c,d));
        list.sort(Comparator.naturalOrder()); // 정렬
        // 원소의 종류 : 중복 제거한 원소의 개수
        int n = hashset.size();
        // 모두 동일한 경우
        if (n == 1) {
            answer += 1111 * a;
        } else if (n == 2) {
            int p = list.get(0);
            int q = list.get(3);
            // 3개 동일한 경우 
            if (list.get(1) == list.get(2)){
                if (list.get(0) == list.get(1)){
                    answer += (int) Math.pow(10 * p + q, 2);
                } else {
                    answer += (int) Math.pow(10 * q + p, 2);   
                }
            } else {
                // 2개 2개 동일한 경우
                answer += (p + q) * Math.abs(p-q);
            }
        } else if(n == 3) {
            // 2개 동일, 나머지 두 개 다른 경우
            if (list.get(0) == list.get(1)){
                answer += list.get(2) * list.get(3);
            } else if (list.get(1) == list.get(2)){
                answer += list.get(0) * list.get(3);
            } else {
                answer += list.get(0) * list.get(1);
            }
        } else {
            // 모두 다른 경우
            answer += list.get(0);
        }
        
        return answer;
    }
}