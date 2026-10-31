public class Program1{
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println("This is my first java program....");
        System.out.println("hi");
        int x,y,z;
        x=10;
        y=20;
        z=30;
        SumThreeNumber.sumThree(x,y,z);
            }
}
class SumThreeNumber{
    public static void sumThree(int a, int b,int c){
        int sum=a+b+c;
        System.out.print("The sum is: ");
        System.out.println(sum);
    }
}