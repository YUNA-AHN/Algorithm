import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()); // 반복 획수
            String word = st.nextToken(); // 단어
            String ans = "";
            // 단어 순회
            for (int j = 0; j < word.length(); j++) {
                for (int k = 0; k < n; k++) {
                    ans += word.charAt(j);
                }
            }
            System.out.println(ans);
        }
    }
}
