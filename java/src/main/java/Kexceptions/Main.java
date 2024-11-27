package Kexceptions;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {
public static void main(String[] args) {
        // Try-with-resources to handle file operations
        try {
            level1(); // Calling the first level
        } catch (ArithmeticException e) {
            System.out.println("Caught in main: " + e.getMessage());
        }
    }

    public static void level1() {
        level2(); // Calls the next level
    }

    public static void level2() {
        level3(); // Calls the next level
    }

    public static void level3() {
        // Throws an exception that propagates up the stack
        int result = 10 / 0; // ArithmeticException
    }
}

