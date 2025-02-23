import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        HashSet set = new HashSet<>(); // 나머지 중족 없이 저장
        for (int i = 0; i < 10; i++) {
            int num =  Integer.parseInt(br.readLine());
            set.add(num % 42); // 나머지 연산자 %
        }
        System.out.println(set.size());
    }
}
