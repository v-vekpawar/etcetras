import java.io.*;

public class FileReadWrite {
    public static void main(String[] args) {
        // Specify the input and output file paths
        String inputFilePath = "textFile.txt";  // Change this to your input file path
        String outputFilePath = "output.txt"; // Change this to your desired output file path

        // Use try-with-resources to ensure proper resource management
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFilePath));
             BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath))) {

            String line;
            // Read from the input file and print to console
            while ((line = reader.readLine()) != null) {
                System.out.println(line); // Print to console
                writer.write(line);        // Write to output file
                writer.newLine();          // Write a new line in the output file
            }

            System.out.println("\n\nContent has been written to " + outputFilePath);

        } catch (IOException e) {
            System.err.println("\n\nAn error occurred while reading or writing files: " + e.getMessage());
        }
    }
}