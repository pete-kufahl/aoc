package day1;

import java.util.*;

public class CompareLists {

    public static long differenceOfLists(List<Integer> arr1, List<Integer> arr2) {
        long total = 0L;
        Collections.sort(arr1);
        Collections.sort(arr2);
        for (int i=0; i < arr1.size(); i++) {
            total += Math.abs(arr1.get(i) - arr2.get(i));
        }
        return total;
    }

    public static long similarityOfLists(List<Integer> arr1, List<Integer> arr2) {
        long score = 0L;
        Set<Integer> set1 = new HashSet<>(arr1);

        // count occurrences
        Map<Integer, Integer> counts1 = new HashMap<>();
        for (int e : arr1) {
            if (set1.contains(e)) {
                counts1.put(e, counts1.getOrDefault(e, 0) + 1);
            }
        }
        Map<Integer, Integer> counts2 = new HashMap<>();
        for (int e : arr2) {
            if (set1.contains(e)) {
                counts2.put(e, counts2.getOrDefault(e, 0) + 1);
            }
        }

        // similarity score formula
        for (int a : set1) {
            score += (long) a * counts1.get(a) * counts2.getOrDefault(a, 0);
        }
        return score;
    }
}