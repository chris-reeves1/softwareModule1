package GTypes;

public class Person {
    // Fields (state of the object - discussed later)
    String name = "string";
    int age;

    // constuctor
    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    public Person() {
        this("unknown", 10);
    }

    // Single-parameter constructor
    public Person(String name) {
        this.name = name;
        this.age = 18; // Default age
    }

    // Methods (behavior of the object)
    public void introduce() {
        System.out.println("Hi, my name is " + name + " and I am " + age + " years old.");
    }
    
    // Setter for name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for age
    public int getAge() {
        return age;
    }
    public String getName(){
        return name;
    }

    // Setter for age
    public void setAge(int age) {
        if (age > 0) { // Validation
            this.age = age;
     }
    }

    }


