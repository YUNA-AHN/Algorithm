import java.util.Arrays; // 배열 불러오기

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int[] answer = {};
        for (int i = 0; i < query.length; i++) {
            // 짝수 인덱스 : query[i]번 인덱스 뒷부분 자르기
            if (i % 2 == 0) {
                arr = Arrays.copyOfRange(arr, 0, query[i] + 1);
                // System.out.println(Arrays.toString(arr));
            } 
            // 홀수 인덱스 : quert[i]번 안댁스 앞부분 자르기
            else {
                arr = Arrays.copyOfRange(arr, query[i], arr.length);
                // System.out.println(Arrays.toString(arr));
            }
        }
        return arr;
    }
}