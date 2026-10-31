package Matrix;

public class MatrixMultiplication {
    protected static float[][] multiplyMatrices(float[][] ...matrices){
        float[][] result=matrices[0];
        for (int i=1;i<matrices.length;i++){
            result=multiplyTwoMatrices(result,matrices[i]);
        }
    return result;
    }
    private static float[][] multiplyTwoMatrices(float[][] a,float[][] b){
        float r1=a[0][0];
        float c1=a[0][1];
        float r2=b[0][0];
        float c2=b[0][1];
        if (c1==r2){
            float[][] result= new float[(int) r1+1][(int) c2];
            result[0][0]=r1;
            result[0][1]=c2;
            for (int i=1;i<r1+1;i++){
                for (int j=0;j<c2;j++){
                    int sum=0;
                    for (int k=0;k<c1;k++){
                        sum += a[i][k] * b[k+1][j];
                    }
                    result[i][j]=sum;
                }
            }
            return result;
        }else{
            System.out.println("Matrix Multipliclication not possible");
            return null;
        }
    }
}
