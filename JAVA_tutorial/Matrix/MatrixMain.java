package Matrix;
import java.util.Scanner;
import java.util.InputMismatchException;
public class MatrixMain {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("\n\t\tMATRIX CALCULATOR\n");
        float[][] matA=MatrixInputDisplay.matrixInput(sc);
        System.out.println("\n\tmatA");
        MatrixInputDisplay.matrixDisplay(matA);
        Choice.choiceOne(matA);
    }
}

class Choice{
    private static Scanner scan=new Scanner(System.in);
    private static String ans="n";
    private static boolean exitCalculator=false;

    private static float[][] singleMatrixOperation(float[][] matrix,String matname){
        try {
            System.out.println("\n1.Transpose(mat" + matname + ") \n2.Determinant(mat" + matname + 
                             ") \n3.Adjoint(mat" + matname + ") \n4.Inverse(mat" + matname + ")"+"\n");
            System.out.print("enter choice: ");
            int choice = scan.nextInt();
            System.out.println();
            float[][] copymatrix=matrix;
            switch(choice) {
                case 1:
                    matrix = MatrixMethods.transpose(matrix);
                    System.out.println("\tTransposed mat" + matname);
                    MatrixInputDisplay.matrixDisplay(matrix);
                    break;
                case 2:
                    Float det = MatrixMethods.determinant(matrix);
                    if(det != null) {
                        System.out.println("Determinant of mat" + matname + " is: " + det);
                    }else{
                        matrix=singleMatrixOperation(copymatrix, matname);
                    }
                    break;
                case 3:
                    matrix = MatrixMethods.adjoint(matrix);
                    if(matrix != null) {
                        System.out.println("\tAdjoint of mat" + matname);
                        MatrixInputDisplay.matrixDisplay(matrix);
                    }else{
                        matrix=singleMatrixOperation(copymatrix, matname);
                    }
                    break;
                case 4:
                    matrix = MatrixMethods.inverse(matrix);
                    if(matrix != null) {
                        System.out.println("\tInverse of mat" + matname);
                        MatrixInputDisplay.matrixDisplay(matrix);
                    }else{
                        matrix=singleMatrixOperation(copymatrix, matname);
                    }
                    break;
                default:
                    System.out.println("\n...wrong-input...(choose b/w 1 to 4)\n");
                    singleMatrixOperation(matrix, matname);
            }
        } catch (InputMismatchException e) {
            System.out.println("\nInvalid input! Please enter an integer.\n");
            scan.next(); // Clear invalid input
            Choice.singleMatrixOperation(matrix, matname);
        }
        
        return matrix;
    }

    protected static void choiceOne(float[][] matA) {
        if (exitCalculator) return;
        try {
            System.out.println("\n1.INPUT another matrix \n2.Operations on matA\n");
            System.out.print("enter choice: ");
            int ch1 = scan.nextInt();
            System.out.println();
            
            if (ch1 == 1) {
                float[][] matB = MatrixInputDisplay.matrixInput(scan);
                System.out.println("\tmatB");
                MatrixInputDisplay.matrixDisplay(matB);
                choiceTwo(matA, matB);
            } 
            else {
                switch(ch1) {
                    case 2:
                        matA = singleMatrixOperation(matA, "A");
                        askForExit(matA);
                        break;
                    default:
                        System.out.println("\n...wrong-input...(choose 1 or 2)\n");
                        choiceOne(matA);
                }
            }
        } catch (InputMismatchException e) {
            System.out.println("\nInvalid input! Please enter an integer.\n");
            scan.next(); // Clear invalid input
            choiceOne(matA);
        }
    }

    private static void choiceTwo(float[][] matA, float[][] matB) {
        if (exitCalculator) return;
        try {
            System.out.println("\n1.INPUT another matrix \n2.Addition \n3.Subtraction \n4.Multiplication \n5.Operations on matB\n");
            System.out.print("enter choice: ");
            int ch2 = scan.nextInt();
            System.out.println();
            
            if (ch2 == 1) {
                float[][] matC = MatrixInputDisplay.matrixInput(scan);
                System.out.println("\tmatC");
                MatrixInputDisplay.matrixDisplay(matC);
                choiceThree(matA, matB, matC);
            }
            else if (ch2 == 5) {
                matB=singleMatrixOperation(matB, "B");
                choiceTwo(matA, matB);
            }
            else {
                float[][] result = null;
                switch(ch2) {
                    case 2:
                        result = MatrixMethods.addition(matA, matB);
                        break;
                    case 3:
                        result = MatrixMethods.subtraction(matA, matB);
                        break;
                    case 4:
                        result = MatrixMultiplication.multiplyMatrices(matA, matB);
                        break;
                    default:
                        System.out.println("\n...wrong-input...(choose b/w 1 to 5)\n");
                        choiceTwo(matA, matB);
                        return;
                }
                if(result != null) {
                    System.out.println("\tResult=(new) matA");
                    MatrixInputDisplay.matrixDisplay(result);
                    askForExit(result);;
                }else{
                    choiceTwo(matA, matB);
                    return;
                }
            }
        } catch (InputMismatchException e) {
            System.out.println("\nInvalid input! Please enter an integer.\n");
            scan.next(); // Clear invalid input
            choiceTwo(matA, matB);
        }
    }

    private static void choiceThree(float[][] matA, float[][] matB, float[][] matC) {
        if (exitCalculator) return;
        try {
            System.out.println("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Operation on matC\n");
            System.out.print("enter choice: ");
            int ch3 = scan.nextInt();
            System.out.println();
            
            if (ch3 == 4) {
                matC=singleMatrixOperation(matC, "C");
                choiceThree(matA, matB, matC);
            }
            else {
                float[][] result = null;
                switch(ch3) {
                    case 1:
                        result = MatrixMethods.addition(matA, matB, matC);
                        break;
                    case 2:
                        result = MatrixMethods.subtraction(matA, matB, matC);
                        break;
                    case 3:
                        result = MatrixMultiplication.multiplyMatrices(matA, matB, matC);
                        break;
                    default:
                        System.out.println("\n...wrong-input...(choose b/w 1 to 4)\n");
                        choiceThree(matA, matB, matC);
                        return;
                }
                if(result != null) {
                    System.out.println("\tResult=(new) matA");
                    MatrixInputDisplay.matrixDisplay(result);
                    askForExit(result);
                }else{
                    choiceThree(matA, matB, matC);
                    return;
                }
            }
        } catch (InputMismatchException e) {
            System.out.println("\nInvalid input! Please enter an integer.\n");
            scan.next(); // Clear invalid input
            choiceThree(matA, matB, matC);
        }
    }

    private static void askForExit(float[][] matrix) {
        try {
            System.out.print("\nExit MATRIX CALCULATOR? (y/n): ");
            ans = scan.next();
            if (ans.equalsIgnoreCase("n")) {
                choiceOne(matrix);
            } else {
                exitCalculator = true;
                System.out.println("\n...Exiting MATRIX CALCULATOR...\n");
            }
        } catch (InputMismatchException e) {
            System.out.println("\nInvalid input! Please enter a string (y/n).\n");
            scan.next();
            askForExit(matrix);
        }
    }

}