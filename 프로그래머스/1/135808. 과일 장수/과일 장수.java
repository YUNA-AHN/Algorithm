// 한 상자에 사과를 m개씩 담아 포장, 얻을 수 있는 최대 이익, 상자 단위
// 최댓값으로 정렬 => m개씩 자르고 마지막 원소로 곱하기
import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        // integer 배열로 변환 후 정렬 -> int 배열엔 사용할 수 없음
        Integer[] array = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(array, Collections.reverseOrder());
        for (int i = 1; i <= array.length / m; i++) {
            answer += array[i * m -1] * m;
        }
        return answer;
    }
}