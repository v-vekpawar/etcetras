package Matrix;
import java.util.Scanner;
public class MatrixInputDisplay{
    
    protected static float[][] matrixInput(Scanner sc){
        System.out.print("Enter number of rows: ");
        int row=sc.nextInt();
        System.out.print("Enter number of column: ");
        int column=sc.nextInt();
        float[][] matrix= new float[(int) row+1][(int) column];
        matrix[0][0]=row;
        matrix[0][1]=column;
        for (int i=1;i<=row;i++){
            for (int j=0;j<column;j++){
                System.out.print("Enter element for row "+i+" column "+(j+1)+": ");
                matrix[i][j]=sc.nextFloat();
            }
        }
        return matrix;
    }

    protected static void matrixDisplay(float[][] matrix){
        System.out.println("\n\t"+(int) matrix[0][0]+"x"+(int) matrix[0][1]);
        for (int i=1;i<=matrix.length-1;i++){
            for (int j=0;j<matrix[i].length;j++){
                System.out.printf("%-5.2f\t",matrix[i][j]);
            }
            System.out.println();
        }
    }

}
