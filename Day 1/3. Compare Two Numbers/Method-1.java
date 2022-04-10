import java.util.*;

class Method {
    public static void main(String[] arg) {
        Scanner in = new Scanner(System.in);
        int x = in.nextInt();
        int y = in.nextInt();
        if ((x ^ y) != 0)
            System.out.println("Not Equal");
        else
            System.out.println("Equal");
    }
}