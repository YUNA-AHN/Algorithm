import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        System.out.println();
        String answer = "";
        // 모든 경우의 수 -> 시간 초과
        // 사전적 정렬을 위해 문자열 리스트로 변환
        String[] strArr = Arrays.stream(numbers) // int 배열을 스트림으로 변환
                                .mapToObj(String::valueOf) // int 값을 String으로 변환
                                .toArray(String[]::new); // String 배열로 반환
        
        // 사용자 정의 정렬
        Arrays.sort(strArr, (a, b) -> (b + a).compareTo(a + b));
        String result = String.join("", strArr);
        answer = result.startsWith("0") ? "0" : result;
        
        return answer;
    }
}