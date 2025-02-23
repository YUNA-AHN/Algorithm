import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        int mul = Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine());
        
        // 0부터 9까지 포함개수
        for (int i = 0; i < 10; i++) {
            System.out.println(countChar(mul, i));
        }
    }

    public static long countChar(int mul, int i) {
        String str = Integer.toString(mul);
        char ch = (char) (i + '0'); // 숫자를 문자로 형 변환 시 0을 더해준다!
        return str.chars()
                .filter(c -> c== ch)
                .count();
    }
}
