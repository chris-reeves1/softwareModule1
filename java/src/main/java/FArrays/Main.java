package FArrays;

public class Main {
public static void main(String[] args) {
        Main lab7 = new Main();
        lab7.start();
}
    public void start() {
        int[] numbers = {1, 3, -5, 7, 0, 4, 6, 8};

        System.out.println("** Task 1: Sum of numbers **");
        int sum = findSum(numbers);
        System.out.println("Sum: " + sum);

        System.out.println("\n** Task 2: Average of numbers **");
        double average = findAverage(numbers);
        System.out.println("Average: " + average);

        System.out.println("\n** Task 3: Minimum number **");
        int min = findMin(numbers);
        System.out.println("Minimum: " + min);

        System.out.println("\n** Task 4: Maximum number **");
        int max = findMax(numbers);
        System.out.println("Maximum: " + max);

        System.out.println("\n** Task 5: Index of zero **");
        int zeroIndex = findIndexOfZero(numbers);
        System.out.println("Index of zero: " + (zeroIndex != -1 ? zeroIndex : "Not found"));

        System.out.println("\n** Task 6: Bubble Sort **");
        bubbleSort(numbers);
        System.out.print("Sorted array: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    private int findSum(int[] numbers) {
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        return sum;
    }

    private double findAverage(int[] numbers) {
        return (double) findSum(numbers) / numbers.length;
    }

    private int findMin(int[] numbers) {
        int min = numbers[0];
        for (int num : numbers) {
            if (num < min) {
                min = num;
            }
        }
        return min;
    }

    private int findMax(int[] numbers) {
        int max = numbers[0];
        for (int num : numbers) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }

    private int findIndexOfZero(int[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == 0) {
                return i;
            }
        }
        return -1; // Return -1 if zero is not found
    }

    private void bubbleSort(int[] numbers) {
        int n = numbers.length;
        boolean swapped;
        do {
            swapped = false;
            for (int i = 0; i < n - 1; i++) {
                if (numbers[i] > numbers[i + 1]) {
                    int temp = numbers[i];
                    numbers[i] = numbers[i + 1];
                    numbers[i + 1] = temp;
                    swapped = true;
                }
            }
        } while (swapped);
    }
}









