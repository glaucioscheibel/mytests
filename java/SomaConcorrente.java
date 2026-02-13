
import java.util.Random;

public class Main extends Thread {
    private long soma;
    private int[] nums;
    private int ini;
    private int fim;

    public Main(int[] nums, int ini, int fim) {
        this.nums = nums;
        this.ini = ini;
        this.fim = fim;
    }

    public void run() {
        for (int i = ini; i<=fim; i++) {
            soma += nums[i];
            if (i % 100 == 0) {
                try {
                    sleep(1);
                } catch (InterruptedException e) {
                }
            }
        }
    }

    public long getSoma() {
        return soma;
    }

    public static void main(String[] args) throws Exception {
        int[] nums = new int[500_000];
        Random r = new Random();
        for (int i = 0; i < nums.length; i++) {
            nums[i] = r.nextInt(1000);
        }

        System.out.println("Iniciando a soma...");
        int n = 10;
        int slice = nums.length / n;
        Main[] ts = new Main[n];
        for (int i = 0; i < n; i++) {
            ts[i] = new Main(nums, i * slice, (i + 1) * slice - 1);
        }
        long ini = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
            ts[i].start();
        }
        long soma = 0;
        for (int i = 0; i < n; i++) {
            ts[i].join();
        }
        for (int i = 0; i < n; i++) {
            soma += ts[i].getSoma();
        }
        System.out.println("Total: " + soma);
        System.out.println("Tempo: " + (System.currentTimeMillis() - ini));
    }
}
