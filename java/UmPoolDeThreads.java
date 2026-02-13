import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class Main {
  public static void main(String[] args) throws Exception {
    ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newCachedThreadPool();
    executor.submit(() -> {
      Thread.sleep(1000);
      System.out.println("A");
      return null;
    });
    executor.submit(() -> {
      Thread.sleep(1000);
      System.out.println("B");
      return null;
    });
    executor.submit(() -> {
      Thread.sleep(1000);
      System.out.println("C");
      return null;
    });

    System.out.println(executor.getPoolSize());
    System.out.println(executor.getQueue().size());
    executor.shutdown();
    executor.awaitTermination(60, TimeUnit.SECONDS);
    System.out.println("Acabou");
  }

}
