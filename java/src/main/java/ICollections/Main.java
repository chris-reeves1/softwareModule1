package ICollections;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Main {

public static void main(String[] args) {
        ArrayList<String> cars = new ArrayList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add(0, "Mazda"); // Insert element at the beginning of the list (0)

        cars.set(0, "Honda");
        cars.remove(1);

        for (int i = 0; i < cars.size(); i++) {
            System.out.println(cars.get(i));
        }

        for (String i : cars) {
            System.out.println(i);
          }

        Collections.sort(cars);  // Sort cars
        for (String i : cars) {
        System.out.println(i);
        }

        System.out.println(cars);


        ArrayDeque<Integer> deque = new ArrayDeque<>();

        deque.addFirst(10);
        deque.addFirst(20);
        deque.pollFirst();
        System.out.println(deque.peekFirst());

        //for (String element : deque) {
        //    System.out.println(element);
        //}

            // Creating a HashMap
            HashMap<String, Integer> map = new HashMap<>();

            // Adding key-value pairs
            map.put("Alice", 30);
            map.put("Bob", 25);
            map.put("Charlie", 35);

            map.putIfAbsent("Eve", 28);

            System.out.println(map); // Output: {Alice=30, Bob=25, Charlie=35}
            map.remove("Bob"); // Removes key "Bob"
            System.out.println(map);

            // Iterating over keys
    for (String key : map.keySet()) {
        System.out.println("Key: " + key);
    }

    // Iterating over values
    for (Integer value : map.values()) {
        System.out.println("Value: " + value);
    }
    }
    }
