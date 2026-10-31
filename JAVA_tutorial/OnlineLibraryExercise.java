/*public class InheritanceOOPs{
    
    public static void main(String[] args) {
        Student student = new Student()
            .setName("John")
            .setAge(20);
    }
} 
    /*public static void main(String[] args) {
        Animal animal2=new Animal();
        Dog doggy=new Dog();
        doggy.name="Saddy";
        System.out.println(animal2.name);
        System.out.println(doggy.name);
        doggy.makeSound(doggy.name);
        animal2.makeSound();
    }
}


class Animal{
    String name;
    int age;
    public void makeSound() {
        System.out.println("Some generic sound");
    }

}
class Dog extends Animal{
    String breed;

    public void makeSound(String name){
        System.out.println(name+" Woof!");
    }
}
class Student {
    private String name;
    private int age;
    
    // Method returns 'this' to allow chaining
    public Student setName(String name) {
        this.name = name;
        return this;
    }
    
    public Student setAge(int age) {
        this.age = age;
        return this;
    }
    
    // Usage:
}
*/
/* 
import java.util.ArrayList;
import java.util.Scanner;

class OnlineLibrary{
    private ArrayList<String> available_books;
    private ArrayList<String>  issued_books;
    private Scanner sc = new Scanner(System.in);

    public OnlineLibrary(String book) {
        available_books = new ArrayList<>();
        issued_books = new ArrayList<>();
        sc = new Scanner(System.in);
        this.addBook(book);
    }

    void showAvailableBooks(){
        this.available_books.toArray(new String[0]); // cpnvert ArrayList to Array
        System.out.println("\nBooks available in library are: ");
        if (available_books.isEmpty()){
            System.out.println("No books avaialable in library...");
            return;
        }
        for (String element:this.available_books){
            System.out.println("* "+element);
        }
    }

    void issueBook(){
        this.showAvailableBooks();
        System.out.print("\nEnter book you want to issue: ");
        String book=sc.nextLine();
        if (available_books.contains(book)){
            available_books.remove(book);
            issued_books.add(book);
            System.out.println(book + " book issued to you....");
        }else{
            System.out.println("Sorry!, No such books available");
        }
        
    }

    void returnBook(){
        if (issued_books.isEmpty()){
            System.out.println("No boolks are issued");
        }
        System.out.println("\nCurrently issued books are:");
        for (String kitab : issued_books) {
            System.out.println("* " + kitab);
        }
        System.out.print("\nEnter book you want to return: ");
        String book=sc.nextLine();
        if (issued_books.contains(book)){
            issued_books.remove(book);
            available_books.add(book);
            System.out.println("Thanlyou for returning "+book+" book");
        }else{
            System.out.println("This book is not by our library...");
        }
    }

    void addBook(String book){
        this.available_books.add(book);
    }
}*/

abstract class Parent{
    Parent(){
        System.out.println("hello");
    }

    abstract void parentMethod1();
}
class Child extends Parent{
    @Override
    void parentMethod1(){
        System.out.println("hello world!!");
    }
}

public class OnlineLibraryExercise{
    public static void main(String[] args) {
        /*OnlineLibrary library = new OnlineLibrary("GRANTH");
        library.addBook("Ved");
        library.addBook("Upanyas");
        library.addBook("Ramayan");
        library.addBook("Mahabharat");
        library.addBook("Ramcharitmanas");
        library.addBook("Rich Dad Poor Dad");
        library.addBook("How to kill a MockingBird");
        library.addBook("R for Everyone");
        library.addBook("Atomic Habits");
        library.issueBook();
        library.issueBook();
        library.showAvailableBooks();
        library.returnBook();
        library.returnBook();
        library.showAvailableBooks();*/

        //Parent p = new Parent(); 
        Child c = new Child();
        c.parentMethod1();
    }
}

