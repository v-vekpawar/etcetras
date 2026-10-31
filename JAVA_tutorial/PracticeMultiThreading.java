public class PracticeMultiThreading {
    public static void main(String[] args) {
        Thread t1=new Thread(() -> {
            for(int i=0;i<=5;i++){
                System.out.println("Hello...");
                // try {
                //     Thread.sleep(200);
                // } catch (InterruptedException e) {

                //     e.printStackTrace();
                // }
            }
        });
        Thread t2=new Thread(() -> {
            for(int i=0;i<=5;i++){
                System.out.println("World...");
            }
        });
        t1.start();
        t2.start(); 
        t1.setPriority(3);
        t2.setPriority(8);
        System.out.println(t1.getPriority());
        System.out.println(t2.getPriority());
        System.out.println(Thread.currentThread().getState());
        System.out.println(t1.getState());
        
        
        
        /* Practice Question 1 and 2
        Thread t1 = new Thread(() -> {
            while(true){
                System.out.println("Welcome");
            }
        });
        Thread t2 = new Thread(()->{
            while(true){
                System.out.println("good morning");
            }
        });
        t1.start();
        try {
            Thread.sleep(200);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        t2.start();
        */

        /*
        // Create two threads
        Thread thread1 = new Thread(() -> {
            for(int i = 0; i < 5; i++) {
                System.out.println("Thread 1: Task " + i);
                try {
                    Thread.sleep(1000); // Pause for 1 second
                } catch(InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            for(int i = 0; i < 5; i++) {
                System.out.println("Thread 2: Task " + i);
                try {
                    Thread.sleep(1000); // Pause for 1 second
                } catch(InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        // Start both threads
        thread1.start();
        thread2.start();
        */
    }
}
