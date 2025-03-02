package day5;

import java.io.IOException;
import java.util.*;

public class Day5 {

    public static int middleElement(List<Integer> arr) {
        if (arr.size() % 2 == 0) {
            throw new IllegalArgumentException("The list must have an odd number of elements.");
        }
        return arr.get(arr.size() / 2);
    }

    public static void main(String[] args) throws IOException {
        String filepath = "src/main/resources/day5/input.txt";
        //String filepath = "src/main/resources/day5/example.txt";

        FileParser.ParsedData parsedData = FileParser.parseFile(filepath);
        List<Integer> middles = new ArrayList<>();
        List<Integer> correctedMiddles = new ArrayList<>();

        for (int[] updateArr : parsedData.updates()) {
            List<Integer> update = new ArrayList<>();
            for (int val : updateArr) {
                update.add(val);
            }

            boolean allowed = true;
            for (int before = 0; before < update.size(); before++) {
                int element = update.get(before);
                List<int[]> applicableRules = new ArrayList<>();
                for (int[] rule : parsedData.rules()) {
                    if (rule[0] == element) {
                        applicableRules.add(rule);
                    }
                }

                for (int[] appl : applicableRules) {
                    if (update.contains(appl[1]) && update.indexOf(appl[1]) < before) {
                        allowed = false;
                        break;
                    }
                }
            }

            if (allowed) {
                System.out.println("Allowing " + update);
                middles.add(middleElement(update));
            } else {
                List<Integer> reordered = UpdateReorderer.reorderUpdate(parsedData.rules(), update);
                if (!reordered.isEmpty()) {
                    System.out.println("Corrected this: " + update + " into this " + reordered);
                    correctedMiddles.add(middleElement(reordered));
                }
            }
        }

        System.out.println("1) Sum of the middle elements of printable updates: " + middles.stream().mapToInt(Integer::intValue).sum());
        System.out.println("2) Sum of the middle elements of corrected updates: " + correctedMiddles.stream().mapToInt(Integer::intValue).sum());
    }
}
