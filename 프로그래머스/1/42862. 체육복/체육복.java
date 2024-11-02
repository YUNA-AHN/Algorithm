
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Collections;
import java.util.Iterator;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        // int 배열 List로 변환 :  int 스트림 생성 후 Integer로 박싱하여 List로 수집
        List<Integer> lostList = Arrays.stream(lost).boxed().collect(Collectors.toList());
        Collections.sort(lostList);  // lostList 정렬
        
        List<Integer> reserveList = Arrays.stream(reserve).boxed().collect(Collectors.toList());
        Collections.sort(reserveList);  // reserveList 정렬
        
        // 여벌 체육복을 가져온 학생이 도난당한 경우, 양쪽 리스트에서 제거
        Iterator<Integer> iterator = lostList.iterator();
        while (iterator.hasNext()) {
            Integer student = iterator.next();
            if (reserveList.contains(student)) {
                iterator.remove();                  // lostList에서 제거
                reserveList.remove(student);        // reserveList에서 제거
            }
        }

        // 여벌 체육복을 빌려줄 수 있는지 확인
        iterator = lostList.iterator();
        while (iterator.hasNext()) {
            Integer student = iterator.next();
            if (reserveList.contains(student - 1)) {
                reserveList.remove(Integer.valueOf(student - 1));
                iterator.remove();
            } else if (reserveList.contains(student + 1)) {
                reserveList.remove(Integer.valueOf(student + 1));
                iterator.remove();
            }
        }

        // 최종 결과: 수업을 들을 수 있는 학생 수
        return n - lostList.size();
    }
}