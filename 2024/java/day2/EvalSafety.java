import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.String;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class EvalSafety {

    private static boolean check_line(List<Integer> levels, int lo, int hi) {
        boolean rule1 = monotonic_levels(levels);
        boolean rule2 = rule1 && safe_differences(levels, lo, hi);
        return rule2;
    }

    private static boolean monotonic_levels(List<Integer> levels) {
        boolean increasing = false;
        for (int i=1; i < levels.size(); i++) {
            if (i == 1) {
                increasing = levels.get(1) > levels.get(0);
            } else {
                if (increasing && levels.get(i) <= levels.get(i-1)) return false;
                if (!increasing && levels.get(i) >= levels.get(i-1)) return false;
            }
        }
        return true;
    }

    private static boolean safe_differences(List<Integer> levels, int lo, int hi) {
        for (int i=1; i < levels.size(); i++) {
            int diff = Math.abs(levels.get(i) - levels.get(i-1));
            if (diff < lo || diff > hi) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        String fileName = "input.txt";
        int i = 0;
        int safeLines = 0;
        int safeLinesIfModified = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                i += 1;
                String[] parts = line.trim().split("\\s+"); // handle multiple spaces
                if (parts.length > 1) {
                    List<Integer> levels = Arrays.stream(parts)
                                .map(Integer::parseInt)
                                .collect(Collectors.toList());
                    boolean ans = check_line(levels, 1, 3);
                    if (!ans) {
                        // create a collection of sublists and check them for safety
                        List<List<Integer>> sublists = IntStream.range(0, levels.size())
                            .mapToObj(x -> {
                                List<Integer> sublist = new ArrayList<>(levels);
                                sublist.remove(x);
                                return sublist;
                            })
                            .collect(Collectors.toList());
                        for (List<Integer> sublist : sublists) {
                            boolean ans1 = check_line(sublist, 1, 3);
                            if (ans1) {
                                safeLinesIfModified += 1;
                                break;
                            }
                        }  
                    } else {
                        safeLines += 1;
                    }
                }
            }
            int totalSafe = safeLines + safeLinesIfModified;
            System.out.println(safeLines + " lines of safe levels (without modification)");
            System.out.println(totalSafe + " lines of safe levels (allowing 1 level to be disregarded)");
                                        
        } catch (RuntimeException e) {
            System.out.println("Error found in line: " + i + " -> " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Problem reading file: " + fileName + "-> " + e.getMessage());
        }
    }  
}
