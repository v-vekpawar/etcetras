public class BasicOperations {
    public static void main(String[] args) {
        System.out.println(Operations.isPallindromeNumber(344));
        System.out.println(Operations.isArmstrong(153));
        System.out.println(Operations.isPallindromeString("viiiv"));
    }    
}

class Operations{
    
    static boolean isPallindromeNumber(int num){
        int temp=num;
        int result=0;
        int digit;
        while (temp>0){
            digit=temp%10;
            result=result*10 + digit;
            temp=temp/10;
        }
        if (result==num){
            return true;
        }
        return false;
    }

    static boolean isArmstrong(int num){
        int temp=num;
        int result=0;
        int digit;
        while (temp>0){
            digit=temp%10;
            result+=digit*digit*digit;
            temp=temp/10;
        }
        if (result==num){
            return true;
        }
        return false;
    }

    static boolean isPallindromeString(String str){
        String result="";
        for (int i=(str.length()-1);i>=0;i--){
            result+=str.charAt(i);
        }
        if (result.equals(str)){
            return true;
        }
        return false;
    }
}
