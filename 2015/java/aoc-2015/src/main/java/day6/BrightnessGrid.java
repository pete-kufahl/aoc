package day6;

public class BrightnessGrid extends LightGrid {

    @Override
    protected void applyAction(String action, int x0, int y0, int x1, int y1) {
        for (int i = x0; i <= x1; i++) {
            for (int j = y0; j <= y1; j++) {
                switch (action) {
                    case "turn on":
                        grid[i][j] += 1;
                        break;
                    case "turn off":
                        grid[i][j] = Math.max(0, grid[i][j] - 1);
                        break;
                    case "toggle":
                        grid[i][j] += 2;
                        break;
                }
            }
        }
    }

    @Override
    protected int quantify() {
        return totalBrightness();
    }

    private int totalBrightness() {
        int count = 0;
        for (int[] row : grid) {
            for (int light : row) {
                count += light;
            }
        }
        return count;
    }
}
