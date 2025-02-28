package day6;

public class BinaryLightGrid extends LightGrid {

    protected void applyAction(String action, int x0, int y0, int x1, int y1) {
        for (int i = x0; i <= x1; i++) {
            for (int j = y0; j <= y1; j++) {
                switch (action) {
                    case "turn on":
                        grid[i][j] = 1;
                        break;
                    case "turn off":
                        grid[i][j] = 0;
                        break;
                    case "toggle":
                        grid[i][j] = grid[i][j] == 0 ? 1 : 0;
                        break;
                }
            }
        }
    }

    public int quantify() {
        return countLightsOn();
    }

    private int countLightsOn() {
        int count = 0;
        for (int[] row : grid) {
            for (int light : row) {
                count += light;
            }
        }
        return count;
    }
}
