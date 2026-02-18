public class Main {
    public static void main(String[] args) {
        boolean[] nums = new boolean[100000];
        int max = (int) Math.sqrt(nums.length);
        for (int i = 2; i <= max; i++) {
            if (!nums[i]) {
                for (int j = i * i; j < nums.length; j+=i) {
                    nums[j] = true;
                }
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (!nums[i]) {
                System.out.print(i);
                System.out.print(", ");
            }
        }
    }
}