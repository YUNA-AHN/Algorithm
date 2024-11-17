import java.util.Arrays;
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        
        // 이분 탐색을 위한 정렬
        Arrays.sort(times);
        
        // left: 최소 시간  right: 최대 시간
        long left = times[0];
        long right = times[times.length - 1] * (long)n;
        
        // left가 right보다 커지면 종료
        while (left <= right) {
            long mid = (left + right) / 2;
            // mid 시간 동안 심사할 수 있는 인원 체크
            long total = 0;
            for (int time : times) {
                total += mid/time;
            }
            
            // 검사 가능 인원이 n보다 크거나 같은 경우 -> 현재 값보다 더 최솟값 존재할 수 있음
            if (total >= n) {
                right = mid - 1;
                answer = mid;
            } // 검사 가능 인원이 n보다 작은 경우
            else {
                left = mid + 1;
            }
        }
        return answer;
    }
}