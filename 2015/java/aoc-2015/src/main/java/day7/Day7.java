package day7;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Day7 {
    public static void main(String[] args) {
        var day7 = new Day7();
        System.out.println("Part 1 (expecting A -> 3176");
        day7.evaluate("src/main/resources/day7/input1.txt");
        System.out.println("Part 2 (expecting A -> 14710)");
        day7.evaluate("src/main/resources/day7/input2.txt");
    }

    private void evaluate(String filepath) {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        try (BufferedReader reader = new BufferedReader(new FileReader(filepath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                evaluator.parseLine(line);
            }

            System.out.println("Value of wire a: " + evaluator.evaluateWire("a"));
            System.out.println("Value of wire b: " + evaluator.evaluateWire("b"));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
