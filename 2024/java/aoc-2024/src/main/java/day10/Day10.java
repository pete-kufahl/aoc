package day10;

import common.GridReader;

import java.io.IOException;
import java.util.List;

import static day10.PathFinder.findPaths;

public class Day10 {
    public static void main(String[] args) throws IOException {
        // String filepath = "src/main/resources/day10/example.txt";
        String filepath = "src/main/resources/day10/input.txt";

        try {
            List<List<Integer>> grid = GridReader.readIntegerGridFromFile(filepath);
            findPaths(grid, false); // expected: 652, 1432
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
