import java.util.Random;
import java.util.Scanner;
public class RockPaperScissor {
    public static void main(String[] args) {
        System.out.println("\nRock (0) | Paper (1) | Scissor (2)");
        int i=1;
        int[] score={0,0};
        while (score[0]<5 && score[1]<5){
            System.out.printf("\nROUND %d\n",i++);
            int user_choice=Functions.userChoice();
            int comp_choice=Functions.CompChoice();
            Functions.result(user_choice, comp_choice,score);
            System.out.printf("Score: %d | %d\n ",score[0],score[1]);
        }
        if (score[0]<score[1]){
            System.out.printf("\n \tFINAL SCORE: %d | %d\n",score[0],score[1]);
            System.out.println("\t\t<<<<YOU LOSE>>>>");
        }
        else{
            System.out.printf("\n \tFINAL SCORE: %d | %d\n",score[0],score[1]);
            System.out.println("\t\t<<<<YOU WIN>>>>");
        }
    }
}
class Functions{
    public static int userChoice(){
        @SuppressWarnings("resource")
        Scanner sc = new Scanner(System.in);
        System.out.print("enter your choice: ");
        int u= sc.nextInt();
        if (u==0){
            System.out.println("you chose Rock");
            return 0;
        }
        else if (u==1){
            System.out.println("you chose Paper");
            return 1;
        }
        else if (u==2){
            System.out.println("you chose Scissor");
            return 2;
        }
        else{
            System.out.println("\n....wrong input.....\n");
            return Functions.userChoice();
        }
    }

    public static int CompChoice(){
        Random random = new Random();
        int c=random.nextInt(3); // generate random integer between 0, 1 and 2 (3 is exclusive)
        switch (c){
            case 0 -> System.out.println("computer chose Rock");
            case 1 -> System.out.println("computer chose Paper");
            case 2 -> System.out.println("computer chose Scissor");
        }
        return c;
    }

    public static void result(int u,int c,int[] s){
        int[][] result_matrix={{0,-1,1},{1,0,-1},{-1,1,0}};
        int result = result_matrix[u][c];
        if (result==0){
            System.out.println("this round is a TIE");
        }
        else if (result ==1){
            System.out.println("You WIN this round");
            s[0]+=1;
        }
        else{
            System.out.println("You LOSE this round");
            s[1]+=1;
        }
        //here i don't have to return s because in java if we pass an object like array to a function and change element of array it will change the array passed to function. (does not make a copy, use origina;)
        //but in case of any variable it will not change the value globally to do that we have to return the new value and assign to same variable (make a copy of original)
    }

}