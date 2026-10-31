import java.util.Scanner;
public class PercentageCalculator {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        try{
            System.out.print("Enter number of subjects: ");
            int num = sc.nextInt();
            float marks[] = new float[num];
            for (int i=0; i<num ; i++){
                System.out.printf("Enter marks of subject %d: ", (i+1));
                float markSub=sc.nextFloat();
                marks[i]=markSub;
            }
            float result= PercentageCalc.percentage(marks, num);
            System.out.printf("the percentage of student is: %.2f",result);
        }
        finally{
            sc.close();
        }
    }
}

class PercentageCalc{
    public static float percentage(float[] marks,int n){
        float sum=0;
        float total_sum= n * 100;
        for (int i=0; i<n; i++){
            // sum = sum + marks[i]
            // sum += marks[i]
            sum  = ++ marks[i]; 
        }
        float percent=( sum / total_sum ) * 100;
        return percent;
    }
}