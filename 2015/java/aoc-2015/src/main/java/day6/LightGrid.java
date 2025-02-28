package day6;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public abstract class LightGrid {

    protected final int[][] grid = new int[1000][1000];

    private static final Pattern INSTRUCTION_PATTERN = Pattern.compile(
            "(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)"
    );

    // factory methods
    public static LightGrid createBinaryGrid() {
        return new BinaryLightGrid();
    }

    public static BrightnessGrid createBrightnessGrid() {
        return new BrightnessGrid();
    }

    public void processFile(String fileName) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                processInstruction(line);
            }
        }
    }

    public void processInstruction(String instruction) {
        Matcher matcher = INSTRUCTION_PATTERN.matcher(instruction);
        if (!matcher.matches()) {
            throw new IllegalArgumentException("Invalid instruction: " + instruction);
        }

        String action = matcher.group(1);
        int x0 = Integer.parseInt(matcher.group(2));
        int y0 = Integer.parseInt(matcher.group(3));
        int x1 = Integer.parseInt(matcher.group(4));
        int y1 = Integer.parseInt(matcher.group(5));

        applyAction(action, x0, y0, x1, y1);
    }

    protected abstract void applyAction(String action, int x0, int y0, int x1, int y1);


    protected abstract int quantify();

}
