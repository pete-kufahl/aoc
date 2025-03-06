package day7;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import static day7.TestSequences.testAddMult;
import static day7.TestSequences.testAddMultConcat;

public class Day7 {

    public static void main(String[] args) throws IOException {
        //String filepath = "src/main/resources/day7/example.txt";
        String filepath = "src/main/resources/day7/input.txt";
        var day7 = new Day7();
        long ans1 = day7.sumTestValuesBasic(filepath);  // part 1, expected: 303766880536
        System.out.println("total calibration value for part 1: " + ans1);
        long ans2 = day7.sumTestValuesAdvanced(filepath);   // part 2, expected: 337041851384440
        System.out.println("total calibration value for part 2: " + ans2);
    }

    private long sumTestValuesBasic(String filepath) {
        long totalCalibrationValue = 0L;
        try (BufferedReader reader = new BufferedReader(new FileReader(filepath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim();
                if (line.isEmpty()) {
                    continue;
                }
                try {
                    String[] parts = line.split(":");
                    long testValue = Long.parseLong(parts[0].trim());
                    String[] operandStrings = parts[1].trim().split(" ");
                    int[] operands = new int[operandStrings.length];
                    for (int i = 0; i < operandStrings.length; i++) {
                        operands[i] = Integer.parseInt(operandStrings[i]);
                    }
                    if (testAddMult(testValue, operands)) {
                        totalCalibrationValue += testValue;
                    }
                } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
                    System.err.println("Skipping malformed line: " + line);
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return totalCalibrationValue;
    }

    private long sumTestValuesAdvanced(String filepath) {
        long totalCalibrationValue = 0L;
        try (BufferedReader reader = new BufferedReader(new FileReader(filepath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim();
                if (line.isEmpty()) {
                    continue;
                }
                try {
                    String[] parts = line.split(":");
                    long testValue = Long.parseLong(parts[0].trim());
                    String[] operandStrings = parts[1].trim().split(" ");
                    int[] operands = new int[operandStrings.length];
                    for (int i = 0; i < operandStrings.length; i++) {
                        operands[i] = Integer.parseInt(operandStrings[i]);
                    }
                    if (testAddMultConcat(testValue, operands)) {
                        totalCalibrationValue += testValue;
                    }
                } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
                    System.err.println("Skipping malformed line: " + line);
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return totalCalibrationValue;
    }
}
