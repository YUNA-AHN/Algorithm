import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] array, int[][] commands) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[] partOf = {};
        
        for (int[] command : commands) {
            System.out.println();
            partOf = array.clone(); // 깊은 복사
            // 정렬 범위 지정 
            Arrays.sort(partOf, command[0] - 1, command[1]);
            System.out.println(Arrays.toString(partOf)); // 배열 출력
            answer.add(partOf[command[0] + command[2] - 2]);
        }
        
        return answer;
    }
}