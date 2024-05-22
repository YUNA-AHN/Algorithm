import java.util.*;
class Solution {
    public ArrayList<int[]> solution(int[][] data, String ext, int val_ext, String sort_by) {
        // 코드 번호, 제조일, 최대 수량, 현재 수량
        String[] index = {"code", "date", "maximum", "remain"};
        ArrayList<int[]> answer = new ArrayList<>();
        int i = 0;
        // ext 기준으로 필터링
        for (int[] row:data){
            // System.out.println(data[i][Arrays.asList(index).indexOf(ext)]);
            if (data[i][Arrays.asList(index).indexOf(ext)] < val_ext){
                answer.add(row);
            }
            i++;
        }
        // 정렬
        answer.sort(Comparator.comparingInt(r -> r[Arrays.asList(index).indexOf(sort_by)]));
        return answer;
    }
}