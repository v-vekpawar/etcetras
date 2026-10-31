import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        GuessNumber gn = new GuessNumber();
        while (true){
            gn.takeUserInput();
            gn.setNGuess();
            System.out.println("number of guesses: "+gn.getNGuess());
            if (gn.isCorrectNumber()){
                System.out.println("you guessed correct number");
                break;
            }
            System.out.println("you guessed wrong number...");
            gn.hintNumber();
            System.out.println();
        }
        System.out.println("Your Score is: "+ gn.getNGuess());
    }
}
class GuessNumber{
    private int nguess;
    private int rno;
    int unum;
    Random random = new Random();
    Scanner sc = new Scanner(System.in);


    public GuessNumber(){
        rno=random.nextInt(100);
    }

    int takeUserInput(){
        System.out.print("Guess the Number: ");
        unum = sc.nextInt();
        return unum;
    }

    boolean isCorrectNumber(){
        if (unum==rno){
            return true;
        }
        return false;
    }

    void setNGuess(){
        nguess+=1;
    }
    int getNGuess(){
        return nguess;
    }

    void hintNumber(){
        if (nguess==1){
            if (rno>75){
                System.out.println("Hint 1: Number is between " + (rno-25) + " to " + (100));
                return;
            }else if (rno>25 && rno<75) {
                System.out.println("Hint 1: Number is between " + (rno-25) + " to " + (rno+25));
                return;
            }else{
                System.out.println("Hint 1: Number is between " + (0) + " to " + (rno+25));
                return;
            }
        }
        if (unum<rno){
            if (unum<(rno-25)) {
                System.out.println("Hint: Guessed number is very much lesser than winning number");
            }else if (unum<(rno-5) && unum>(rno-10)){
                System.out.println("Hint: You are very close your number is slightly lesser.");
            }else if (unum<(rno-10)){
                System.out.println("Hint: Winning Number is a little greater than " + (unum));
            }else {
                System.out.println("Hint: You're extremely close! Just a tiny bit higher!");
            }
        }else if (unum>rno){
            if (unum>(rno+25)) {
                System.out.println("Hint: Guessed number is very much greater than winning number");
            }else if (unum>(rno+5) && unum<(rno+10)){
                System.out.println("Hint: You are very close your number is slightly greater.");
            }else if (unum>(rno+10)){
                System.out.println("Hint: Winning Number is a little smaller than " + (unum));
            }else {
                System.out.println("Hint: You're extremely close! Just a tiny bit lower");
            }
        }
    }
}