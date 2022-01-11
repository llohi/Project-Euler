import java.util.ArrayList;

public class p23 {
    public static void main(String[] args) {

        int s = 0;
        for (int i = 1; i < 28123 + 1; i++) {
            if (i % 2 != 0) {
                s += i;
            }
        }
        System.out.println(s + 26 + 28);
    }

    public static int d(int n) {

        int s = 1;
        for (int i = 2; i < (int) Math.sqrt(n) + 1; i++) {
            if (n % i == 0) {
                s += i;
                s += n / i;
            }
        }
        return s;
    }
}
