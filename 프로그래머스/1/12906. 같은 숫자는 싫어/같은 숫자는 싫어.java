import java.util.*;

public class Solution {
    public Stack<Integer> solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        stack.push(arr[0]); // 첫 번째는 무조건 추가
        for(int i = 1; i < arr.length; i++){
            if (stack.peek() != arr[i]){ // 최상단과 다른 경우에만 추가
                stack.push(arr[i]);
            }
        }
        return stack;
    }
}