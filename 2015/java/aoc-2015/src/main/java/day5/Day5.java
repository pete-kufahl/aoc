package day5;

import java.io.IOException;

public class Day5 {
    private final NiceStringChecker checker = new NiceStringChecker();

    public static void main(String[] args) throws IOException {
        String input_path = "src/main/resources/day5/input.txt";
        var day5 = new Day5();
        day5.countNiceStrings_part1(input_path);
        day5.countNiceStrings_part2(input_path);
    }

    void countNiceStrings_part1(String input_path) throws IOException {
        var ans = checker.countNiceStrings(input_path, NiceStringChecker.Ruleset.SET_ONE);
        System.out.println("expected: 238, actual: " + ans);
    }

    void countNiceStrings_part2(String input_path) throws IOException {
        var ans = checker.countNiceStrings(input_path, NiceStringChecker.Ruleset.SET_TWO);
        System.out.println("expected: 69, actual: " + ans);
    }
}
