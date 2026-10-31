import java.util.Scanner;
public class ConditionalStatements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        /* // usage of percentage calculator
        System.out.print("enter marks in subject 1: ");
        int m1=sc.nextInt();
        System.out.print("enter marks in subject 2: ");
        int m2=sc.nextInt();
        System.out.print("enter marks in subject 3: ");
        int m3=sc.nextInt();
        sc.close();
        if (ConditionalFunctions.passingCriteria(m1, m2, m3)){
            System.out.println("ypu have passed");
        }
        else{
            System.out.println("you have failed");
        }
        */

        /* // usage of income tax calculator
        System.out.print("Enter your salary: ");
        int sal=sc.nextInt();
        sc.close();
        float tax=ConditionalFunctions.incomeTax(sal);
        if (tax==-1.f){
            System.out.println("you don't need to pay tax");
        }
        else{
            System.out.printf("you have to pay %.3f $ tax",tax);
        }
        */
        
        /* // usage of day by number calculator
        System.out.print("enter day number: ");
        int daynum=sc.nextInt();
        sc.close();  
        ConditionalFunctions.dayOfCalendar(daynum);
        */

        /* // usage of type of website teller
        System.out.print("enter website: ");
        String website=sc.nextLine();
        sc.close();
        ConditionalFunctions.typeOfWebsite(website);
        */
        sc.close();
    }
}
class ConditionalFunctions {

    public static boolean passingCriteria(int marks1, int marks2, int marks3){
        float overall_percentage=(marks1+marks2+marks3)/3.f;
        if (marks1>=33 && marks2>=33 && marks3>=33 && overall_percentage>=40.0){
            return true;
        }
        return false;
    }

    public static float incomeTax(int salary){
        if (salary <= 249999){
            return -1.f;
        }
        else if (salary>=250000 && salary<500000){
            return salary*0.05f;
        }
        else if (salary>=500000 && salary<1000000){
            return salary*0.2f;
        }
        else{
            return salary*0.3f;
        }
    }

    public static void dayOfCalendar(int day){
        switch (day){
            case 0 -> System.out.println("Calendar does not have zero...");
            case 1 -> System.out.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday");
            default -> ConditionalFunctions.dayOfCalendar(day-7);
        }
    }

    public static void typeOfWebsite(String website){
        if (website.endsWith(".com")){
            System.out.println("given website is commercial website");
        }
        else if (website.endsWith(".in")){
            System.out.println("given website is Indian website");
        }
        else if (website.endsWith(".gov")){
            System.out.println("given website is government website");
        }
        else if (website.endsWith(".org")){
            System.out.println("given website is organization website");
        }
        else if (website.endsWith(".info")){
            System.out.println("given website is information website");
        }

    }
}
