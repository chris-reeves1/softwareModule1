package BBasics;

public class Main {
    public static void main(String[] args) {
        //int x = 10; // primitive type - directly stores the value in stack memory. 
        //String name = "Alice"; // reference type, references an object. 
                            // the ref is stored on the stack, object stored in heap. 


        // primitive
        //int a = 5;
        //int b = a; // -- copy of the value
        //b = 10;
        //System.out.println(a);
        //System.out.println(b);

        //ref type -- allows multiple references to the same object.

        //int[] arr = {1, 2, 3};
        ///int[] ref = arr;
        //ref[0] = 100;
        //System.out.println(arr[0]);
        //System.out.println(ref[0]);

        //int i = 5;
        //int result = ++i; //pre-increment
        //System.out.println(i);
        //System.err.println(result);

        //int i = 5;
        //int result = i++;
        //System.out.println(i);
        //System.out.println(result);

        //for (int i = 0; i < 5; ++i){
        //   System.out.println(i);
        //}

        // implicit casting
        //int num = 100;
        //long l = num;

        //System.out.println(l);

        // explicit casting
        //double d = 100.5;
        //int num = (int) d;  
        //System.out.println(num); // truncated. 
        
        //Parsing
        String intString = "123";
        int number = Integer.parseInt(intString);
        System.out.println(number);

        String doubleString = "45.67";
        double decimal = Double.parseDouble(doubleString);
        System.out.println(decimal);

        String booleanString = "true";
        boolean flag = Boolean.parseBoolean(booleanString);
        System.out.println(flag);

        }     
}

/*
 * naming convention:
 * Always start with a letter, never a number.
 * Dont use reserved words.
 * case-sensitive, (but Student as method name wouold be allowed)
 * classes PascalCasing
 * Methods and variables camelCasing
 * packages lower-case
 * 
 * variables:
 * Must be declared with a type.
 * Variables - local variables are only valid within their block. 
 * must be initialsed wioth a value.
 * Variable reassignment:
 * primitive types:
 *  - type is copied when assigned or passed.
 * ref types:
 *  - allows multiple references to the same object. 
 * 
 * Standard mathmatical operators like in python. 
 * 
 * ++ and -- : commonly used Loops, incement numeric types by 1. 
 * 
 * pre ++x - the increment happens before the value is used in an expression. 
 * 
 * post x++ - this happens after an expression
 * 
 * Casting:
 * implicit casting (that can naturally happen also called widening.)
 * small -> big
 * byte -> short -> int -> long -> float -> double.  
 * 
 * Explicit casting (narrowing):
 * larger to small -- lead to data and prescision loss. 
 * 
 * casting Strings to numbers (parsing)
 * Wrapper classes Boolean, Integer, Double, provide methods for parsing.
 * 
 * 
 */