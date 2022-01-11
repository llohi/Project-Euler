/*
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

public class p9 {
    public static void main(String[] args) {
        int i, j, n, m,
            a, b, c;

        for (i = 1; i < 60; i++) {
            n = i;
            for (j = 1; j < 60; j++) {
                m = j + 1;
                a = (int) (Math.pow(m, 2) - Math.pow(n, 2));
                b = 2 * m * n;
                c = (int) (Math.pow(m, 2) + Math.pow(n, 2));

                if (a + b + c == 1000) {
                    System.out.println(a * b * c);
                    return;
                }
            }
        }
    }
}
