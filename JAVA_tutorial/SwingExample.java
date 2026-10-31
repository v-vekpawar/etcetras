import javax.swing.*;  // Import Swing classes

public class SwingExample {
    public static void main(String[] args) {
        // Create a frame
        JFrame f = new JFrame("Swing Example");

        // Create a button
        JButton b = new JButton("Click Me");

        // Set position and size of button
        b.setBounds(100, 100, 100, 40);

        // Add button to the frame
        f.add(b);

        // Set frame size
        f.setSize(300, 300);

        // Set layout to null for absolute positioning
        f.setLayout(null);

        // Close operation
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Make the frame visible
        f.setVisible(true);
    }
}
