public class p19 {
    public static void main(String[] args) {

        int year = 1901;
        int month = 1;
        int day = 1;
        int wday = 2;  // 1st jan 1901 = tuesday  -google :)
        int n = 0;

        while (year != 2000 || month != 12 || day != 31) {

            // check date
            if (day == 1 && wday == 7) {
                n++;
            }

            // increment date
            wday = (wday < 7) ? wday + 1 : 1;

            // leap year
            if (isLeap(year)) {
                if (month == 2 && day == 28) {
                    day++;
                    continue;
                }
            }
        }
    }

    public static boolean isLeap(int year) {

        return (year % 4 != 0) ? false :
                    (year % 400 == 0) ? true :
                            (year % 100 == 0) ? false : true;
    }
}
