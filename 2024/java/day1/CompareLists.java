import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.String;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class CompareLists {

    private static Long differenceOfLists(List<Integer> arr1, List<Integer> arr2) {
        Long total = (long) 0;
        Collections.sort(arr1);
        Collections.sort(arr2);
        for (int i=0; i < arr1.size(); i++) {
            total += Math.abs(arr1.get(i) - arr2.get(i));
        }
        return total;
    }

    private static Long similarityOfLists(List<Integer> arr1, List<Integer> arr2) {
        Long score = (long) 0;
        Set<Integer> set1 = new HashSet<>();
        for (int a : arr1) {
            set1.add(a);
        }

        // count occurences 
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
            score += a * counts1.get(a) * counts2.getOrDefault(a, 0);
        }
        return score;
    }

    public static void main(String[] args) {
        String fileName = "input.txt";
        int i = 0;
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                i += 1;
                String[] parts = line.trim().split("\\s+"); // handle multiple spaces
                if (parts.length == 2) {
                    int[] nums = Arrays.stream(parts)
                                .mapToInt(Integer::parseInt)
                                .toArray();
                    arr1.add(nums[0]);
                    arr2.add(nums[1]);
                }
            }
            Long ans1 = differenceOfLists(arr1, arr2);
            System.out.println("Difference of lists: " + ans1);

            Long ans2 = similarityOfLists(arr1, arr2);
            System.out.println("Similarity of lists: " + ans2);
                                        
        } catch (RuntimeException e) {
            System.out.println("Error found in line: " + i + " -> " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Problem reading file: " + fileName + "-> " + e.getMessage());
        }
    }               
}