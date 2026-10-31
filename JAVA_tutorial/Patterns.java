public class Patterns {
    public static void main(String[] args) {
        System.out.println("\t\t 1. PYRAMID");
        PatternFunctions.pyramid(7,"*");
        System.out.println();
        
        System.out.println("\t\t 2. LEFT INDENTED PYRAMID");
        PatternFunctions.leftPyramid(7,"$");
        System.out.println();
        
        System.out.println("\t\t 3. RIGHT INDENTED PYRAMID");
        PatternFunctions.rightPyramid(7,"@");
        System.out.println();
        
        System.out.println("\t\t 4. REVERSE PYRAMID");
        PatternFunctions.reversePyramid(7,"~");
        System.out.println();
        
        System.out.println("\t\t 5. REVERSE LEFT INDENTED PYRAMID");
        PatternFunctions.reverseLeftPyramid(7,"-");
        System.out.println();
        
        System.out.println("\t\t 6. REVERSE RIGHT INDENTED PYRAMID");
        PatternFunctions.reverseRightPyramid(7,"=");
        System.out.println();
        
        System.out.println("\t\t 7. HOLLOW PYRAMID");
        PatternFunctions.hollowPyramid(7,"!");
        System.out.println();
        
        System.out.println("\t\t 8. DIAMOND");
        PatternFunctions.diamond(7,"+");
        System.out.println();
        
        System.out.println("\t\t 9. HOLLOW DIAMOND");
        PatternFunctions.hollowDiamond(7,"^");
        System.out.println();
        
        System.out.println("\t\t 10. LEFT INDENTED RHOMBUS");
        PatternFunctions.leftRhombus(7,"#");
        System.out.println();
        
        System.out.println("\t\t 11. RIGHT INDENTED RHOMBUS");
        PatternFunctions.rightRhombus(7,"&");
        System.out.println();
        
        System.out.println("\t\t 12. HOURGLASS");
        PatternFunctions.hourGlass(7,"%");
        System.out.println();
        
        System.out.println("\t\t 13. LHOLLOW SQUARE");
        PatternFunctions.hollowSquare(7,".");
        System.out.println();
        
        System.out.println("\t\t 14. FLOYD's TRIANGLE");
        PatternFunctions.floydsTriangle(5);
        System.out.println();
        
        System.out.println("\t\t 15. PASCAL's TRIANGLE");
        PatternFunctions.pascalsTriangle(7);
        System.out.println();
    }
}
class PatternFunctions{
    
    public static void leftPyramid(int n,String s){
        for (int i=0;i<n;i++){
            for (int j=0;j<=i;j++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void reverseLeftPyramid(int n,String s){
        for (int i=n;i!=0;i--){
            for (int j=0;j<=i;j++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void rightPyramid(int n,String s){
        for (int i=0;i<n;i++){
            for (int j=n;j>i;j--){
                System.out.print(" ");
            }
            for (int k=0;k<=i;k++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void reverseRightPyramid(int n,String s){
        for (int i=n;i!=0;i--){
            for (int j=n;j>i;j--){
                System.out.print(" ");
            }
            for (int k=1;k<=i;k++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void pyramid(int n,String s){
        for (int i=1;i<=n;i++){
            for (int j=n;j>i;j--){
                System.out.print(" ");
            }
            for (int k=1; k<=2*i-1 ;k++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void reversePyramid(int n,String s){
        for (int i=n;i>0;i--){
            for (int j=n;j>i;j--){
                System.out.print(" ");
            }
            for (int k=1; k<=2*i-1 ;k++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void leftRhombus(int n,String s){
        for (int i=0;i<n;i++){
            for (int j=1; j<=i ;j++){
                System.out.print(" ");
            }
            for (int k=0;k<n;k++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void rightRhombus(int n,String s){
        for (int i=n;i>0;i--){
            for (int j=1; j<=i ;j++){
                System.out.print(" ");
            }
            for (int k=0;k<n;k++){
                System.out.print(s);
            }
            System.out.println();
        }
    }

    public static void diamond(int n,String s){
        if (n%2==0){
            System.out.println("enter odd number of rows for diamond pattern");
        }else{
            //pyramid
            for (int i=1;i<=(n/2)+1;i++){
                for (int j=n;j>i;j--){
                    System.out.print(" ");
                }
                for (int k=1; k<=2*i-1 ;k++){
                    System.out.print(s);
                }
                System.out.println();
            }
            //revrse pyramid
            for (int i=(n/2);i>0;i--){
                for (int j=n;j>i;j--){
                    System.out.print(" ");
                }
                for (int k=1; k<=2*i-1 ;k++){
                    System.out.print(s);
                }
                System.out.println();
            }
        }
    }

    public static void hourGlass(int n,String s){
        if (n%2==0){
            System.out.println("enter odd number of rows for hourglass pattern");
        }else{
            //revrse pyramid
            for (int i=(n/2)+1;i>0;i--){
                for (int j=n;j>i;j--){
                    System.out.print(" ");
                }
                for (int k=1; k<=2*i-1 ;k++){
                    System.out.print(s);
                }
                System.out.println();
            }
            //pyramid
            for (int i=2;i<=(n/2)+1;i++){
                for (int j=n;j>i;j--){
                    System.out.print(" ");
                }
                for (int k=1; k<=2*i-1 ;k++){
                    System.out.print(s);
                }
                System.out.println();
            }
        }
    }

    public static void hollowSquare(int n, String s){
        /*//first row 
        for (int i=0;i<n;i++){
            System.out.print(s);
        }
        System.out.println();
        //hollow part
        for (int j=1;j<n-1;j++){
            System.out.print(s);
            for (int k=1;k<n-1;k++){
                System.out.print(" ");
            }
            System.out.println(s);
        }
        //last row
        for (int i=0;i<n;i++){
            System.out.print(s);
        }
        System.out.println();*/

        // or 

        for (int i=1;i<=n;i++){
            for (int j=1;j<=n;j++){
                if (i==1 || j==1 || i==n || j==n){
                    System.out.print(s);
                }else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    public static void hollowPyramid(int n, String s){
        if (n%2==0){
            System.out.println("enter odd number of rows for hollow pyramid pattern");
        }else{
            for (int i=1;i<=n;i++){
                for (int j=n;j>i;j--){
                    System.out.print(" ");
                }
                for (int k=1; k<=2*i-1 ;k++){
                    if (k==1 || k==2*i-1 || i==n){
                        System.out.print(s);
                    }else{
                        System.out.print(" ");
                    }
                }
                System.out.println();
            } 
        }       
    }

    public static void hollowDiamond(int n, String s){
        if (n%2==0){
            System.out.println("enter odd number of rows for hollow diamond pattern");
        }else{
            //pyramid
            for (int i=1;i<=(n/2)+1;i++){
                for (int j=n;j>i;j--){
                    System.out.print(" ");
                }
                for (int k=1; k<=2*i-1 ;k++){
                    if (k==1 || k==2*i-1 || i==n){
                        System.out.print(s);
                    }else{
                        System.out.print(" ");
                    }
                }
                System.out.println();
            }
            //revrse pyramid
            for (int i=(n/2);i>0;i--){
                for (int j=n;j>i;j--){
                    System.out.print(" ");
                }
                for (int k=1; k<=2*i-1 ;k++){
                    if (k==1 || k==2*i-1 || i==n){
                        System.out.print(s);
                    }else{
                        System.out.print(" ");
                    }
                }
                System.out.println();
            }
        }        
    }

    public static void floydsTriangle(int n){
        int num=1;
        for (int i=1;i<=n;i++){
            for (int j=1;j<=i;j++){
                System.out.print(num++);
            }
            System.out.println();
        }
    }

    public static void pascalsTriangle(int n){
        for (int i = 0; i < n; i++) {
            for (int j = n; j > i + 1; j--) {
                System.out.print(" ");
            }
            int num = 1;
            for (int j = 0; j <= i; j++) {
                System.out.print(num + " ");
                num = num * (i - j) / (j + 1);
            }
            System.out.println();
        }
    }
}
