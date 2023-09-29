import java.util.ArrayList;
class Solution {
    public ArrayList solution(int[] arr) {
        ArrayList <Integer> stk = new ArrayList<>();
        int i = 0;
        // arr을 다 순회할 때까지
        while (i < arr.length){
            // stk가 빈 배열이라면
            if (stk.isEmpty()){
                stk.add(arr[i]);
                i += 1;
            // ArrayList 읻덱싱 : .get()
            // ArrayList 크기 : .size()
            } else if (stk.get(stk.size()-1) < arr[i]){
                stk.add(arr[i]);
                i += 1;
            } else {
                stk.remove(stk.size()-1);
            }
        }
        return stk;
    }
}