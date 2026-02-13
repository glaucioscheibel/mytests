public class Main extends Thread {
    private Conta conta1;
    private Conta conta2;

    public Main(Conta conta1, Conta conta2) {
        this.conta1 = conta1;
        this.conta2 = conta2;
    }

    public void run() {
        for (int i = 0; i < 100; i++) {
            conta1.sacar(10);
            conta2.depositar(10);
        }
    }

    public static void main(String[] args) throws Exception {
        Main[] agencias = new Main[1000];
        Conta c1 = new Conta(1000);
        Conta c2 = new Conta(1000);
        System.out.println(c1);
        System.out.println(c2);
        for (int i = 0; i < agencias.length; i++) {
            if (i % 2 == 0) {
                agencias[i] = new Main(c1, c2);
            } else {
                agencias[i] = new Main(c2, c1);
            }
        }
        for (int i = 0; i < agencias.length; i++) {
            agencias[i].start();
        }
        for (int i = 0; i < agencias.length; i++) {
            agencias[i].join();
        }
        System.out.println(c1);
        System.out.println(c2);
    }
}
