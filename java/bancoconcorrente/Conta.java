public class Conta {
  private double saldo;

  public Conta(double saldo) {
    this.saldo = saldo;
  }

  public double getSaldo() {
    return saldo;
  }

  public void depositar(double valor) {
    saldo += valor;
  }

  public void sacar(double valor) {
    saldo -= valor;
  }

  @Override
  public String toString() {
    return "Conta [saldo=" + saldo + "]";
  }
}
