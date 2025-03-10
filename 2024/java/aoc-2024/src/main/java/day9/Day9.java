package day9;


import java.io.IOException;

public class Day9 {
    public static void main(String[] args) throws IOException {
        // String filepath = "src/main/resources/day9/example.txt";
        String filepath = "src/main/resources/day9/input.txt";
        Day9 day9 = new Day9();
        day9.partOne(filepath, false); // expected: 6395800119709
        day9.partTwo(filepath, false); // expected: 6418529470362
    }

    private void partOne(String filepath, boolean debug) {
        long checksum = DiskBuilder.computeChecksumOfCompacted(filepath, debug);
        System.out.println("Final checksum is " + checksum);
    }

    private void partTwo(String filepath, boolean debug) {
        long checksum = DiskBuilder.computeChecksumOfIntegrated(filepath, debug);
        System.out.println("Final checksum is " + checksum);
    }

}
