/*
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20x20 grid?
*/
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class p11 {
    public static void main(String[] args) {

        int[][] grid = new int[20][20];
        int i, j, k, horz, vert, diaga, diagb;

        // read data from file
        try {
            File file = new File("11.txt");
            Scanner scanner = new Scanner(file);
            i = 0;
            while (scanner.hasNextLine()) {
                String[] line = scanner.nextLine().split(" ");
                for (j = 0; j < 20; j++) {
                    grid[i][j] = Integer.parseInt(line[j]);
                }
                i++;
            }

        } catch (FileNotFoundException e) {
            System.out.println("Error.");
            e.printStackTrace();
        }

        // calculate max
        int max = 0;

        // horizontal/vertical
        for (i = 0; i < 20; i++) {
            for (j = 0; j < 17; j++) {
                horz = grid[i][j];
                vert = grid[j][i];

                for (k = 1; k < 4; k++) {
                    horz *= grid[i][j+k];
                    vert *= grid[j+k][i];
                }

                // update max
                max = Math.max(horz, max);
                max = Math.max(vert, max);
            }
        }

        // diagonal
        for (i = 0; i < 17; i++) {
            for (j = 0; j < 17; j++) {
                diaga = grid[i][j];
                diagb = grid[i+3][j];

                for (k = 1; k < 4; k++) {
                    diaga *= grid[i+k][j+k];
                    diagb *= grid[i+3-k][j+k];
                }

                max = Math.max(diaga, max);
                max = Math.max(diagb, max);
            }
        }

        System.out.println(max);
    }
}
