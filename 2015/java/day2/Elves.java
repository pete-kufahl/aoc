import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class Elves {
    public static void main(String[] args) {
        String fileName = "input.txt";
        int totalPaper = 0;
        int totalRibbon = 0;
        int i = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                i += 1;
                String[] parts = line.trim().split("x");
                if (parts.length == 3) {
                    try {
                        int[] dims = Arrays.stream(parts)
                            .mapToInt(Integer::parseInt)
                            .toArray();
                        int x1 = dims[0], x2 = dims[1], x3 = dims[2];

                        // total paper
                        int[] sides = {x1 * x2, x1 * x3, x2 * x3};
                        int surfaceArea = 2 * (sides[0] + sides[1] + sides[2]);
                        int minimum = Arrays.stream(sides).min().orElseThrow(() -> new IllegalArgumentException("sides array cannot be empty"));
                        totalPaper += surfaceArea + minimum;

                        // total ribbon
                        int[] perimeters = {
                            2 * x1 + 2 * x2,
                            2 * x1 + 2 * x3,
                            2 * x2 + 2 * x3
                        };
                        int smallPerim = Arrays.stream(perimeters).min().orElseThrow(() -> new IllegalArgumentException("perimeters array cannot be empty"));
                        int bow = x1 * x2 * x3;
                        totalRibbon += smallPerim + bow;

                    } catch (NumberFormatException e) {
                        System.out.println("Invalid integers found in line: " + line);
                    }
                } else {
                    System.out.println("Line does not contain exactly 3 numbers separated by 'x': " + line);
                }
            }
            System.out.println("total paper needed for " + i + " gifts: " + totalPaper + " ft^3");
            System.out.println("total ribbon needed: " + totalRibbon + " ft");
        } catch (IOException e) {
            // Handle errors related to file reading
            System.out.println("An error occurred while reading the file: " + e.getMessage());
        }
    }
}
