import java.util.Scanner;
public class Game{
    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        game.playGame();
    }
    
}
class TicTacToe{
    private char[][] board;
    private char currentPlayer;
    
    public TicTacToe(){
        this.board = new char[3][3];
        this.initializeBoard();
        currentPlayer='X';
    }

    private void initializeBoard(){
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = ' ';
            }
        }
    }

    public void printBoard() {
        System.out.println("Current Board:");
        for (int i = 0; i < 3; i++) {
            System.out.print(" | ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println();
            System.out.println("---------------");
        }
    }

    private boolean isBoardFull(){
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' '){
                    return false;
                }
            }
        }
        return true;
    }

    private boolean checkWinner(){
        for (int i=0;i<3;i++){
            if ((board[i][0]==currentPlayer) && (board[i][1]==currentPlayer) && (board[i][2]==currentPlayer)){
                return true;
            }else if ((board[0][i]==currentPlayer) && (board[1][i]==currentPlayer) && (board[2][i]==currentPlayer)){
                return true;
            }
        }
        if ((board[0][0]==currentPlayer) && (board[1][1]==currentPlayer) && (board[2][2]==currentPlayer)){
            return  true;
        }else if ((board[0][2]==currentPlayer) && (board[1][1]==currentPlayer) && (board[2][0]==currentPlayer)){
            return true;
        }else{
            return false;
        }
    }

    public void playGame(){
        Scanner sc = new Scanner(System.in);
        while (true){
            printBoard();
            System.out.println("Player " + currentPlayer + ", enter your move (row and column): ");
            try{
                System.out.print("Enter row(1-3): ");
                int row = sc.nextInt()-1;
                System.out.print("Enter col(1-3): ");
                int col = sc.nextInt()-1;
                System.out.println();
                if (row>2 || row<0 || col>2 || col<0){
                    System.out.println("wrong input(-_-) enter between 1 to 3");
                    continue;
                }
                if (board[row][col]!=' '){
                    System.out.println("...This place already taken.... chose wisely(~_~)");
                    continue;
                }
                board[row][col]=currentPlayer;
                if (checkWinner()) {
                    printBoard();
                    System.out.println("Player " + currentPlayer + " wins!");
                    break;
                }
                if (isBoardFull()) {
                    printBoard();
                    System.out.println("It's a draw!");
                    break;
                }
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
            }catch (Exception e){
                System.out.println("Invalid Input (*_*)... enter integern only\n");
                sc.nextLine();
            }
        }
        sc.close();
    }
}