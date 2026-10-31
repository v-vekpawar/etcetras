package Matrix;
public class MatrixMethods{
    
    protected static float[][] addition(float[][] ...matrices){
        float[][] result=matrices[0];
        for (int i=1;i<matrices.length;i++){
            if (result[0][0]==matrices[i][0][0] && result[0][1]==matrices[i][0][1]){
                for(int j=1;j<matrices[i].length;j++){
                    for (int k=0;k<matrices[i][j].length;k++){
                        result[j][k]+=matrices[i][j][k];
                    }
                }
            }else{
                System.out.println("matrix addition not possible");
                return null;
            }
        }
        return result;
    }

    protected static float[][] subtraction(float[][] ...matrices){
        float[][] result=matrices[0];
        for (int i=1;i<matrices.length;i++){
            if (result[0][0]==matrices[i][0][0] && result[0][1]==matrices[i][0][1]){
                for(int j=1;j<matrices[i].length;j++){
                    for (int k=0;k<matrices[i][j].length;k++){
                        result[j][k]-=matrices[i][j][k];
                    }
                }
            }else{
                System.out.println("matrix subtraction not possible");
                return null;
            }
        }
        return result;
    }

    protected static Float determinant(float[][] mat){
        float row=mat[0][0];
        float col=mat[0][1];
        if (row!=col){
            System.out.println("matrix is not a square matrix \ndeterminant not possible");
            return null;
        }
        if (row==2){
            return (mat[1][0]*mat[2][1])-(mat[1][1]*mat[2][0]);
        }
        else{
            float determinant=0;
            float[][] submatrix=new float[(int) row][(int) col-1];
            submatrix[0][0]=row-1;
            submatrix[0][1]=col-1;
            for (int k=0;k<col;k++){
                for (int i=2;i<=row;i++){
                    int y=0;
                    for (int j=0;j<col;j++){
                        if (j==k) continue;
                        submatrix[i-1][y++]=mat[i][j];
                    }
                }
                if ((1+k)%2==0){
                    determinant+=(-1)*(mat[1][k]*(determinant(submatrix)));
                }else{
                    determinant+=(mat[1][k])*(determinant(submatrix));
                }
            }
            return determinant;
        }
    }

    protected static float[][] transpose(float[][] mat){
        float row=mat[0][0];
        float col=mat[0][1];
        float[][] result = new float[(int) col+1][(int) row];
        result[0][0]=col;
        result[0][1]=row;
        for (int i=1;i<=row;i++){
            for (int j=0;j<col;j++){
                result[j+1][i-1]=mat[i][j];
            }
        }
        return result;
    }

    protected static float[][] adjoint(float[][] mat){
        float row=mat[0][0];
        float col=mat[0][1];
        if (row!=col){
            System.out.println("matrix is not a square matrix \nadjoint does not exist");
            return null;
        }

        if (row==2){
            float[][] result = new float[(int) row+1][(int) col];
            result [0][0]=row;
            result[0][1]=col;
            result[1][0]=mat[2][1];
            result[2][1]=mat[1][0];
            result[1][1]=-mat[1][1];
            result[2][0]=-mat[2][0];
            return result;
        }

        float[][] result = new float[(int) row+1][(int) col];
        result [0][0]=row;
        result[0][1]=col;
        float[][] submatrix=new float[(int) row][(int) col-1];
        submatrix[0][0]=row-1;
        submatrix[0][1]=col-1;
        for (int r=1;r<=row;r++){
            for (int c=0;c<col;c++){
                int x=1;
                for (int i=1;i<=row;i++){
                    if (i==r) continue;
                    int y=0;
                    for (int j=0;j<col;j++){
                        if (j==c) continue;
                        submatrix[x][y++]=mat[i][j];
                    }
                    x++;
                }
                if ((r+c)%2==0){
                    result[r][c]=(-1)*(determinant(submatrix));
                }else{
                    result[r][c]=determinant(submatrix);
                }
            }
        }
        return transpose(result);
    }

    protected static float[][] inverse(float[][] mat){
        Float d=determinant(mat);
        if (d != null){
            if (d==0){
                System.out.println("determinant is zero \ninverse does not exist");
                return null;
            }  
            float rows = mat[0][0];
            float col = mat[0][1];
            float[][] result = adjoint(mat);
            for (int i=1;i<=rows;i++){
                for (int j=0;j<col;j++){
                    result[i][j]=(result[i][j])/d;
                }
            }
            return result;
        }else{
            System.out.println("...inverse not possible...\n");
            return null;
        }
    }
}