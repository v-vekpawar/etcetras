import java.util.Scanner;
public class StringMethods {
    public static void main(String[] args) {
        String name = "Shri Krishna";
        
        System.out.println(name); 
        System.out.printf("my name is %s \n",name); //method of formatted string print in same line
        System.out.format("i am lord %s \n",name);  //another method of formatted string print in same line

        System.out.println();

        // taking string input
        Scanner sc = new Scanner(System.in);
        System.out.println("enter string: ");
        String str1=sc.next();     //takes only the first word
        System.out.format("you entered: %s \n",str1);
        sc.nextLine(); //it is added because without this the next input will be considered as leftover of sc.next()
        System.out.println("enter string: ");
        String str2=sc.nextLine();   //takes the whole line
        System.out.format("you entered: %s \n",str2);
        
        // string methods

        // 1. length() 
        int a=name.length(); //give length of the string
        System.out.printf("the string length is:%4d\n",a);  //%4d means 4 spaces were added in left side of a

        // 2. toUpperCase()
        System.out.println(name.toUpperCase()); //returns a new string in all letters uppercase

        // 3. toLowerCase()
        System.out.println(name.toLowerCase()); //returns a new string in all letters Lowercase

        // 4. trim()
        String name2= "      ved      ";
        System.out.println(name2.trim()); //returns a new string by removing all leading and trailing spaces

        // 5. substring(int start, int end)
        System.out.println(name.substring(3)); //returns a new substring from index 3 to end
        System.out.println(name.substring(2,8)); //returns a new substring from index 2 to 7 as end is excluded
        
        // 6. replace('char1',char2) || replace("substr1","substr2")
            // it will replace all occurence of char1 or substr1 with char2 or substr2 respectively...
        System.out.println(name.replace('i','e')); //returns a new string after replacing i with e 
        System.out.println(name.replace("Shri","Shree")); //returns a new string after replacing shri with shree

        // 7. startsWith('char') || startsWith("string")
        System.out.println(name.startsWith("shri")); //returns True if name starts with shri (case sensitive)

        // 8. endssWith('char') || endsWith("string")
        System.out.println(name.endsWith("shna")); //returns True if name ends with shna (case sensitive)

        // 9. charAt(int index)
        System.out.println(name.charAt(5)); //returns character at index 5

        // 10. indexOf('char') || indexOf('char',start)    ('char' || "substr")
        System.out.println(name.indexOf('S')); //returns index of first occurence of s
        System.out.println(name.indexOf('s',5)); //returns index of first occurence of s starting from index 7
        System.out.println(name.indexOf("Ram"));  //return -1 as substring not present in the name

        // 11. lastIndexOf('char') || lastIndexOf('char',start)   ('char' || "substr")
        System.out.println(name.lastIndexOf('s')); //returns index of last occurence of s or first occurence in reverse traverse
        System.out.println(name.lastIndexOf('s',4)); //returns index of first occurence of s in reverse traversing starting from index 4
        System.out.println(name.lastIndexOf("Ram"));  //return -1 as substring not present in the name
        // 12. equals("substr") || equalsIgnorecase("substr")     ('char' || "substr")
        System.out.println(name.equals("Ram")); //returns False if name not equals to Ram
        System.out.println(name.equalsIgnoreCase("shri krishna")); //return True as it is case insensitive

        // 13. Escape characters or Escape Sequence Character
            // to escape character we have to use backslash(\)
        System.out.println("\\i am lord \"Krishna\"/");  //print: \i am lord "Krishna"/
        System.out.println("\\i am godess \"Radha\"/");  //print: \ i am godess "Radha"/

        sc.close();
    }
}
