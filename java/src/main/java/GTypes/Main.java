package GTypes;

public class Main {
    public static void main(String[] args) {
                // Create an object of the Person class
                Person person1 = new Person();
                // Access and modify fields
                person1.name = "Alice";
                person1.age = 30;
                // Call a method
                person1.introduce();
        
                Person person2 = person1; // Both refer to the same object
                person2.name = "Bob";
        
                person1.introduce(); // Output: Hi, my name is Bob and I am 30 years old.
        
                Person person3 = null;
                //person3.introduce(); // This will throw a NullPointerException.
        
                person1.setAge(55);
                person1.setName("Smith");
                person1.getName();
                person2.getAge();
                person1.introduce();


                int a = 5;
    int b = 5;
    System.out.println(a == b); // true (values are equal)

    //Person person4 = new Person();
    //Person person5 = person4;
    //System.out.println(person4 == person5); // true (same reference)

    //Person person6 = new Person();
    //System.out.println(person4 == person6); // false (different references)

    //Person person7 = new Person();
    //Person person8 = person7; // Both point to the same object

    //person8 = new Person();

    BankAccount bnk = new BankAccount();
        bnk.deposit(-5);
        }

      }

       class BankAccount {
        private double balance;

        public void deposit(double amount) {
            if (amount > 0) {
                balance += amount;
            } else {
                throw new IllegalArgumentException("Deposit amount must be positive.");
            }
        }

        public void withdraw(double amount) {
            if (amount > 0 && amount <= balance) {
                balance -= amount;
            } else {
                throw new IllegalArgumentException("Invalid withdrawal amount.");
            }
        }
    }




