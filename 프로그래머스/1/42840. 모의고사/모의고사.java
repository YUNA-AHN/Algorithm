import java.util.*;
class Solution {
    public List<Integer> solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int[] fst = {1, 2, 3, 4, 5};
        int[] sec = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] thr = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        List<Integer> arr = new ArrayList<>(Arrays.asList(0,0,0));
        
        System.out.println();
        
        for (int i = 0; i < answers.length; i++){
            if (answers[i] == fst[i%5]) {
                arr.set(0, arr.get(0) + 1);
            }
            if (answers[i] == sec[i%8]) {
                arr.set(1, arr.get(1) + 1);
            }
            if (answers[i] == thr[i%10]) {
                arr.set(2, arr.get(2) + 1);
            }
        }
        
        Integer top = Collections.max(arr);
        
        for (int j = 0; j < 3; j++) {
            if (arr.get(j).equals(top)) {
                answer.add(j+1);
            }
        }
        
        return answer;
    }
}