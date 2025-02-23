import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine()); // 테스트 케이스

        // num 만큼 순회
        for (int i = 0; i < tc; i++) {
            String quiz = br.readLine();
            int point = 0; // 점수
            int last = 0; // 쌓인 점수

            // 퀴즈 순회
            for (int j = 0; j < quiz.length(); j++) {
                if (quiz.charAt(j) == 'O') {
                    last += 1;
                    point += last;
                } else {
                    last = 0;
                }
            }
            // 점수 출력
            System.out.println(point);
        }
    }
}
