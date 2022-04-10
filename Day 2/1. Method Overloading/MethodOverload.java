public class MethodOverload {
    public static void main(String[] arg) {
        MethodOverload obj = new MethodOverload();
        System.out.println(obj.Add("Darsi ", "Gangothri"));
        System.out.println(obj.Add(2.5f, 5.8f));
        System.out.println(obj.Add(4, 9));
    }

    public int Add(int a, int b) {
        return (a + b);
    }

    public float Add(float a, float b) {
        return (a + b);
    }

    public String Add(String a, String b) {
        return (a + b);
    }
}
