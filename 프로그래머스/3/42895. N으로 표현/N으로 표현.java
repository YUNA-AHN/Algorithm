import java.util.*;

class Solution {
    public int solution(int N, int number) {
        if (N == number) return 1; // N과 number가 같으면 바로 반환

        List<Set<Integer>> setList = new ArrayList<>();
        for (int i = 0; i < 9; i++) setList.add(new HashSet<>()); // N 사용 횟수별 집합 초기화

        setList.get(1).add(N); // N을 1번 사용해 만들 수 있는 숫자는 N

        for (int i = 2; i < 9; i++) {
            Set<Integer> currentSet = setList.get(i);
            
            // N을 i번 연속 사용하여 만든 숫자 추가 (예: N=5일 때 55, 555)
            currentSet.add(Integer.parseInt(String.valueOf(N).repeat(i)));
            
            // j와 i-j로 쪼개어 가능한 조합 계산
            for (int j = 1; j < i; j++) {
                Set<Integer> set1 = setList.get(j);
                Set<Integer> set2 = setList.get(i - j);

                for (int n1 : set1) {
                    for (int n2 : set2) {
                        currentSet.add(n1 + n2);
                        currentSet.add(n1 - n2);
                        currentSet.add(n1 * n2);
                        if (n2 != 0) currentSet.add(n1 / n2); // 0인 경우 제외
                    }
                }
            }

            // 원하는 숫자 생성 확인
            if (currentSet.contains(number)) return i;
        }
        return -1; // 8번을 넘지 않고 number를 만들 수 없는 경우
    }
}
