import java.util.TreeSet;

class Solution {
    public TreeSet<Integer> solution(int[] numbers) {
        // 정렬하여 더하기 + 중복 없어야 함
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++ ) {
                set.add(numbers[i] + numbers[j]);
            }
        }
        return set;
    }
}