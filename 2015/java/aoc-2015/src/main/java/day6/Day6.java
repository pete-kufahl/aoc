package day6;

import java.io.IOException;

public class Day6 {
    public static void main(String[] args) {
        String filepath = "src/main/resources/day6/input.txt";
        var day6 = new Day6();
        day6.lightGrid_part1(filepath);
        day6.lightGrid_part2(filepath);
    }

    public void lightGrid_part1(String filepath) {
        try {
            LightGrid grid = LightGrid.createBinaryGrid();
            grid.processFile(filepath);
            System.out.println("expecting 569999, lights on: " + grid.quantify());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void lightGrid_part2(String filepath) {
        try {
            LightGrid grid = LightGrid.createBrightnessGrid();
            grid.processFile(filepath);
            System.out.println("expecting 17836115, brightness: " + grid.quantify());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
