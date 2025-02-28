package day6;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LightGridTest {

    private final LightGrid binaryGrid = LightGrid.createBinaryGrid();
    private final BrightnessGrid brightnessGrid = LightGrid.createBrightnessGrid();

    @Test
    void testTurnOn() {
        binaryGrid.processInstruction("turn on 0,0 through 999,999");
        assertEquals(1000000, binaryGrid.quantify());

        brightnessGrid.processInstruction("turn on 0,0 through 999,999");
        assertEquals(1000000, brightnessGrid.quantify());
    }

    @Test
    void testTurnOff() {
        binaryGrid.processInstruction("turn on 0,0 through 999,999");
        binaryGrid.processInstruction("turn off 499,499 through 500,500");
        assertEquals(999996, binaryGrid.quantify());

        brightnessGrid.processInstruction("turn on 0,0 through 999,999");
        brightnessGrid.processInstruction("turn off 499,499 through 500,500");
        assertEquals(999996, brightnessGrid.quantify());
    }

    @Test
    void testToggle() {
        binaryGrid.processInstruction("turn on 0,0 through 999,999");
        binaryGrid.processInstruction("toggle 0,0 through 999,999");
        assertEquals(0, binaryGrid.quantify());

        brightnessGrid.processInstruction("turn on 0,0 through 999,999");
        brightnessGrid.processInstruction("toggle 0,0 through 999,999");
        assertEquals(3000000, brightnessGrid.quantify());
    }

    @Test
    void testMixedOperations() {
        binaryGrid.processInstruction("turn on 0,0 through 4,4");   // 25
        binaryGrid.processInstruction("toggle 2,2 through 3,3");    // -4
        binaryGrid.processInstruction("turn off 1,1 through 2,2");  // -3
        assertEquals(18, binaryGrid.quantify());

        brightnessGrid.processInstruction("turn on 0,0 through 4,4");   // 25
        brightnessGrid.processInstruction("toggle 2,2 through 3,3");    //  8
        brightnessGrid.processInstruction("turn off 1,1 through 2,2");  // -4
        assertEquals(29, brightnessGrid.quantify());
    }
}