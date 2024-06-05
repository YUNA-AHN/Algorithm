import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int big:tangerine) {
            countMap.putIfAbsent(big, 0);
            countMap.replace(big, countMap.get(big) + 1);
        }
        // 해시맵 정렬
        List<Integer> keys = new ArrayList<>(countMap.keySet());
        Collections.sort(keys, (v1, v2) -> (countMap.get(v2).compareTo(countMap.get(v1))));
        int total = 0;
        for (int idx:keys){
            total += countMap.get(idx);
            answer++;
            if (total >= k) {
                break;
            }
        }
        return answer;
    }
}