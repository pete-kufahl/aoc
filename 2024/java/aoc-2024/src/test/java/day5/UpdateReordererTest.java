package day5;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;

class UpdateReordererTest {

    @Test
    void testReorderUpdateBasic() {
        List<int[]> rules = Arrays.asList(
                new int[]{1, 2},
                new int[]{2, 3},
                new int[]{3, 4}
        );
        List<Integer> update = Arrays.asList(1, 2, 3, 4);
        List<Integer> result = UpdateReorderer.reorderUpdate(rules, update);

        assertEquals(Arrays.asList(1, 2, 3, 4), result);
    }

    @Test
    void testReorderUpdateNoDependencies() {
        List<int[]> rules = new ArrayList<>();
        var update = Arrays.asList(3, 1, 2);

        List<Integer> result = UpdateReorderer.reorderUpdate(rules, update);

        assertEquals(Arrays.asList(3, 1, 2), result);
    }

    @Test
    void testReorderUpdateCircularDependency() {
        List<int[]> rules = Arrays.asList(
                new int[]{1, 2},
                new int[]{2, 3},
                new int[]{3, 1}
        );
        var update = Arrays.asList(1, 2, 3);

        List<Integer> result = UpdateReorderer.reorderUpdate(rules, update);
        assertTrue(result.isEmpty(), "Circular dependencies should return an empty list");
    }
}
