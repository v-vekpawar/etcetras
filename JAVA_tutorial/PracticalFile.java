import java.util.Scanner;
import java.util.Random;
public class PracticalFile {
    public static void main(String[] args) {
        
        /*// prac-1
        boolean isPrime = true;
        Random random = new Random();
        int rno = random.nextInt(100);
        System.out.println("Generated random number is: "+rno);
        if (rno<=1){
            isPrime=false;
        }else{
            for (int i=2;i<=Math.sqrt(rno);i++){
                if (rno%i==0){
                    isPrime = false;
                    break;
                }
            }
        }
        if (isPrime){
            System.out.println("Generated random number is a prime number");
        }else{
            System.out.println("Generated random number is not a prime number");
        }*/

        /*//prac-2a
        int a=0,b=1;
        System.out.print(a);
        for (int i=0;i<9;i++){
            int temp=a;
            System.out.print("\t");
            System.out.print(b);
            a=b;
            b=temp+b;
        }
        //prac-2b
        System.out.println(factorial(7));*/

        /*//prac-3
        int sum=0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0;i<n;i++){
            System.out.print("Enter element: ");
            arr[i]=sc.nextInt();
        }
        sc.close();
        System.out.print("\nInputted array is: ");
        for (int j=0;j<n;j++){
            System.out.print(arr[j]+"\t");
            sum+=arr[j];
        }
        System.out.println("\nThe sum of given array is: "+sum);
        System.out.println("The average of given array is: "+(float) sum/n);*/

        /*//prac-4
        Rectangle rect = new Rectangle(23,45);
        System.out.println("The area of rectangle is: "+rect.area());
        System.out.println("The area of rectangle is: "+rect.perimeter());*/

        /*//prac-5
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a  string: ");
        String str = sc.nextLine();
        StringOperation s = new StringOperation(str);
        System.out.print("Enter a  string: ");
        String str2 = sc.nextLine();
        System.out.println();
        s.equals(str2);
        System.out.println();
        System.out.println("Reversed of the given string is: "+s.reverse());
        System.out.println();
        s.changeCase();
        sc.close();*/



    }
    
    /*//prac-2b
    public static int factorial(int num){
        if (num==1){
            return 1;
        }else if (num==2){
            return 2;
        }
        else{
            return num*factorial(num-1);
        }
    }*/
}
/* //prac-4
class Rectangle{
    float l,b;
    public Rectangle(int length,int breadth){
        this.l=length;
        this.b=breadth;
    }
    float area(){
        return l*b;
    }
    float perimeter(){
        return 2*(l+b);
    }
}
*/
/* //prac-5 
class StringOperation{
    String str;
    public StringOperation(String s){
        this.str=s;
    }
    void equals(String str2){
        if (str.equals(str2)){
            System.out.println(str+" is equals to :"+str2);
        }else{
            System.out.println(str+" is not equals to: "+str2);
        }
    }
    String reverse(){
        String rev="";
        for(int i=str.length()-1;i>=0;i--){
            rev+=str.charAt(i);
        }
        return rev;
    }
    void changeCase(){
        System.out.println("Given String in uppercase: "+str.toUpperCase());
        System.out.println("Given String in lowercase: "+str.toLowerCase());
    } 
}*/
