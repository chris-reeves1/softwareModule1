package ELoops;

public class Main {
public static void main(String[] args) {
    
    for (int i = 1; i <= 5; i++) {
        System.out.println("Count: " + i);
    }

    //for (type element : collection/array) {
    //}
    
    int[] numbers = {1, 2, 3, 4, 5};
    for (int number : numbers) {
        System.out.println("Number: " + number);
    }
  
}
}