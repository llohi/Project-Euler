/*
The sum of the squares of the first ten natural numbers is 385.
The square of the sum of the first ten natural numbers is 3025.
Hence, the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
*/

public class p6 {
    public static void main(String[] args) {

        int a = 0;
        int b = 0;

        for (int i = 0; i < 101; i++) {
            a += i * i;
            b += i;
        }
        b *= b;
        System.out.println(b - a);  // 25164150
    }
}
