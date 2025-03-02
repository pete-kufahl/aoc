package day4;

import java.util.List;

import static day4.XMasWord.*;

public class Day4 {
    public static void main(String[] args) {

        char[][] grid = getGrid("src/main/resources/day4/input.txt");

        // part 1
        List<int[]> part1 = findWord(grid, "XMAS");
        System.out.println("Found XMAS " + part1.size() + " times");

        // part 2
        int part2 = findCrosses(grid);
        System.out.println("Found X-MAS cross patterns " + part2 + " times");
    }
}
