package day3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Collections;
import java.util.Comparator;

public class ReadCodes {
    
    public static void main(String[] args) {
        int option = 1;
        if (args.length > 0) {
            try {
                option = Integer.parseInt(args[0]);
                if (option != 1 && option != 2) {
                    System.out.println("Invalid argument. Defaulting to 1.");
                    option = 1;
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Defaulting to 1.");
                option = 1;
            }
        }
        boolean useDosDonts = option != 1; // puzzle 1: false, puzzle 2: true

        String fileName = "src/main/resources/day3/input.txt";
        StringBuilder buffer = new StringBuilder();

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
        // just read everything into a single buffer
            String line;
            // add each line's content to buffer without the newline
            while ((line = reader.readLine()) != null) {
                buffer.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        String mulPattern = "mul\\((\\d+),(\\d+)\\)";
        String doPattern = "do\\(\\)";
        String dontPattern = "don't\\(\\)";

        List<Event> events = new ArrayList<>(); // store all events

        // Compile patterns
        Pattern mulRegex = Pattern.compile(mulPattern);
        Pattern doRegex = Pattern.compile(doPattern);
        Pattern dontRegex = Pattern.compile(dontPattern);

        // Match and extract "mul(X,Y)" patterns
        Matcher mulMatcher = mulRegex.matcher(buffer);
        while (mulMatcher.find()) {
            int x = Integer.parseInt(mulMatcher.group(1));
            int y = Integer.parseInt(mulMatcher.group(2));
            int position = mulMatcher.start();
            events.add(new Event("mul", position, x, y));
        }

        // Match and extract "do()" positions
        Matcher doMatcher = doRegex.matcher(buffer);
        while (doMatcher.find()) {
            int position = doMatcher.start();
            events.add(new Event("do", position));
        }

        // Match and extract "don't()" positions
        Matcher dontMatcher = dontRegex.matcher(buffer);
        while (dontMatcher.find()) {
            int position = dontMatcher.start();
            events.add(new Event("don't", position));
        }

        // Sort events by position
        events.sort(Comparator.comparingInt(e -> e.position));

        boolean enabled = true;  // enabled mode to start with
        long subProducts = 0;

        for (Event event : events) {
            if (enabled && event.type.equals("mul")) {
                subProducts += (long) event.x * event.y;
                // System.out.println("mul(X: " + event.x + ", Y: " + event.y + ") at Position: " + event.position);
            } else if (useDosDonts && event.type.equals("do")) {
                enabled = true;
                // System.out.println(event.type + "() at Position: " + event.position);
            } else if (useDosDonts && event.type.equals("don't")) {
                enabled = false;
                // System.out.println(event.type + "() at Position: " + event.position);
            }
        }
        System.out.println("total for " + (useDosDonts ? "Part 2: " : "Part 1: ") + subProducts);
    }

    static class Event {
        String type;
        int position;
        Integer x; // Nullable for non-mul events
        Integer y; // Nullable for non-mul events

        // Constructor for mul(X,Y)
        Event(String type, int position, int x, int y) {
            this.type = type;
            this.position = position;
            this.x = x;
            this.y = y;
        }

        // Constructor for do() and don't()
        Event(String type, int position) {
            this.type = type;
            this.position = position;
        }
    }
}
