package Linheritance;

import java.util.ArrayList;
import java.util.List;

class Animal {
    public void speak1() {
        System.out.println("Animal speaks.");
    }
}

class Dog extends Animal {
    //@Override
    public void speak() {
        System.out.println("Dog barks.");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog(); // Upcasting
        //animal = (Dog) animal;
        Dog myDog = (Dog) animal;
        myDog.speak();
        }
    
}