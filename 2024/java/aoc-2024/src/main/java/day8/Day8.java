package day8;

import common.GridReader;

import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

import static day8.Antinodes.findAntinodes;
import static day8.Antinodes.findCollinearPoints;

public class Day8 {

    private char[][] grid;

    public Day8(char[][] grid) {
        this.grid = grid;
    }

    public static void main(String[] args) throws IOException {
        // String filepath = "src/main/resources/day8/example.txt";
        String filepath = "src/main/resources/day8/input.txt";
        var grid = GridReader.readGridFromFile(filepath);
        GridReader.printGrid(grid);
        Day8 day8 = new Day8(grid);
        day8.partOne(grid, false); // expected: 332
        day8.partTwo(grid, false); // expected: 1174
    }

    public void partOne(char[][] grid, boolean debug) {
        int rows = grid.length;
        int cols = grid[0].length;
        System.out.println("Input grid is " + rows + " rows and " + cols + " columns");

        // Map to store frequency (char) -> locations { (x, y) }
        Map<Character, Set<Node>> antennae = new HashMap<>();

        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < cols; x++) {
                char freq = grid[y][x];
                if (freq != '.') {
                    antennae.computeIfAbsent(freq, k -> new HashSet<>()).add(new Node(x, y));
                }
            }
        }

        for (var entry : antennae.entrySet()) {
            System.out.println(entry.getValue().size() + " antennae for the frequency " + entry.getKey());
        }

        // Calculate antinodes (in-bounds) for each antenna set
        List<Set<Node>> antinodesList = new ArrayList<>();
        for (Set<Node> network : antennae.values()) {
            antinodesList.add(findAntinodes(network, grid));
        }

        if (debug) {
            for (Set<Node> group : antinodesList) {
                System.out.println("Antinode set: " + group);
            }
        }

        // Flatten a list of sets into a single set
        Set<Node> uniqueAntinodes = antinodesList.stream()
                .flatMap(Set::stream)
                .collect(Collectors.toSet());

        if (debug) {
            for (int j = 0; j < rows; j++) {
                char[] printRow = new char[cols];
                Arrays.fill(printRow, '.');
                for (int i = 0; i < cols; i++) {
                    if (uniqueAntinodes.contains(new Node(i, j))) {
                        printRow[i] = '#';
                    } else {
                        printRow[i] = grid[j][i];
                    }
                }
                System.out.println(new String(printRow));
            }
        }

        System.out.println();
        System.out.println(uniqueAntinodes.size() + " antinodes amongst all of these antenna pairs");
    }


    public void partTwo(char[][] grid, boolean debug) {
        int rows = grid.length;
        int cols = grid[0].length;
        System.out.println("Input grid is " + rows + " rows and " + cols + " columns");

        // Map to store frequency (char) -> locations { (x, y) }
        Map<Character, Set<Node>> antennae = new HashMap<>();

        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < cols; x++) {
                char freq = grid[y][x];
                if (freq != '.') {
                    antennae.computeIfAbsent(freq, k -> new HashSet<>()).add(new Node(x, y));
                }
            }
        }

        // Calculate antinodes (collinear in-bounds) for each antenna set
        List<Set<Node>> antinodesList = new ArrayList<>();
        for (Set<Node> network : antennae.values()) {
            antinodesList.add(findCollinearPoints(network, grid));
        }

        // Flatten a list of sets into a single set
        Set<Node> uniqueAntinodes = antinodesList.stream()
                .flatMap(Set::stream)
                .collect(Collectors.toSet());

        System.out.println();
        System.out.println(uniqueAntinodes.size() + " collinear-point antinodes amongst all of these antenna pairs");
    }
}
