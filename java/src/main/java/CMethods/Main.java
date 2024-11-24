package CMethods;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    
        String name = "Chris";
        int age = 10;
        double x = 54.35;

        String formattedString = String.format("Hello %s, your age is %d, also %.2f", name, age, x);
        
        System.out.printf(formattedString);
        
        } 
}


/*
 * Methods:
 * a block of code that performs a specific task, like python. 
 * Must be in the body of the class.
 * 
 * signature defines visibility, name, params, return types. 
 * Access_modifiers:
 *  - public: accesbile from any class.
 *  - protected: accessible from package and sub-classes
 *  - private: Within the class only.
 *  - default (no modifier): accessable within package. 
 * 
 * return types: 
 *  - void (no return value)
 *  - Value (String, int etc....)
 * 
 * params:
 *  - can be none -- void greet(){}
 *  - can be single -- void greet(String a){}
 *  - multi -- void greet(String a, int b)
 * 
 * Making an object:
 * ClassName objectName = new ClassName();
 * 
 * public void add(int a, int b){
        System.out.println(a + b);

         public static void main(String[] args) {
        Main c = new Main();
        c.add(5, 10);

        public static void main(String[] args) {
        //Main c = new Main();
        System.out.println(add(5, 5));
        }

    public static int add(int a, int b){
        return a + b;
    }

    Method overloading:
    multiplie methods with ths same name but different params. 
    changes:
    - the order
    - the number of params
    - types of params 
    Defaults are not supported in JAva (they are in c#)

    Main c = new Main();
        c.greet("john");

        }

    public void greet(String name){
        System.out.println("hello, " + name);
    }

    public void greet(){
        greet("chris");
    }

    scanner:
    - scanner can read frm multiple sources.
    - We must make an object of Scanner to use.
    - import java.util.Scanner; 
    
    Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter your name: ");
        String name = scanner.nextLine(); //Reads a whole line
        
        System.out.println("hello " + name);
        scanner.close();

        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter your age: ");
        int age = scanner.nextInt(); 

        System.out.println("Enter your salary: ");
        double salary = scanner.nextDouble();

        scanner.nextLine();

        System.out.println("enter your name: ");
        String name = scanner.nextLine();

        
        System.out.println("hello " + name + " age " + age + " salery " + salary);
        scanner.close();

    printf - for formatting strings
    + 
    printf() prints directly to system.out. 
    - %d - number
    - %s - string
    - %b - boolean
    - %f - float 

       System.out.printf("integer: %d%nString: %s%nFloat: %f%n", 10, "hello-world"
        , 3.11455);
        }

    String name = "Chris";
        int age = 10;
        double x = 54.35;

        //String formattedString = ""
        
        System.out.printf("Hello %s, your age is %d, also %2f", name, age, x);


 */