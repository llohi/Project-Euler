public class p3 {
    public static void main(String[] args) {
        long n = 600851475143L;
        int f = 1;
        int i = 1;

        while (n != 1) {
            if (n % (6 * i - 1) == 0) {
                f = 6 * i - 1;
                n /= f;
            }
            if (n % (6 * i + 1) == 0) {
                f = 6 * i + 1;
                n /= f;
            }
            i++;
        }
        System.out.format("The biggest factor is %d", f);  // 6857
    }
}
