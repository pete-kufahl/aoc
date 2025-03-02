package day5;

import java.io.*;
import java.nio.file.*;
import java.util.*;

public class FileParser {

    public static ParsedData parseFile(String filePath) throws IOException {
        List<int[]> rules = new ArrayList<>();
        List<int[]> updates = new ArrayList<>();

        List<String> lines = Files.readAllLines(Paths.get(filePath));
        int blankLineIndex = lines.indexOf("");
        if (blankLineIndex == -1) {
            blankLineIndex = lines.size();
        }

        List<String> rulesSection = lines.subList(0, blankLineIndex);
        List<String> updatesSection = lines.subList(Math.min(blankLineIndex + 1, lines.size()), lines.size());

        for (String line : rulesSection) {
            line = line.trim();
            if (!line.isEmpty()) {
                String[] parts = line.split("\\|");
                rules.add(new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])});
            }
        }

        for (String line : updatesSection) {
            line = line.trim();
            if (!line.isEmpty()) {
                updates.add(Arrays.stream(line.split(","))
                        .mapToInt(Integer::parseInt)
                        .toArray());
            }
        }

        return new ParsedData(rules, updates);
    }

    public record ParsedData(List<int[]> rules, List<int[]> updates) {}
}
