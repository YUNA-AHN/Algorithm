import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (int col: moves){
            // 해당 열을 탐색 : 0이 아니면 stack 입력
            for (int row = 0; row < board.length; row++){
                if (board[row][col-1] != 0) {
                    stack.add(board[row][col-1]);
                    board[row][col-1] = 0;
                    break;
                }
            }
            if (stack.size() >= 2) {
                if (stack.peek() == stack.get(stack.size() - 2)) {
                    stack.pop();
                    stack.pop();
                    answer += 2;
                }
            }
        }
        return answer;
    }
}