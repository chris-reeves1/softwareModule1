package DConditionals;

public class Main {
    public static void main(String[] args) {
        
        //int number = 10;
        //String result = (number > 0) ? "Positive" : "Negative";
        //System.out.println(result);

        //int a = 10;
        //int b = 15;
        //int c = 3;

        //String result = !(a > b) ? (b > c ? "B is greater than c" : "C is greater than b") : "A is largest";
        
        //System.out.println(result);

        //int number = -5;
        //int absoluteValue = (number < 0) ? -number : number;
        //System.out.println(absoluteValue); 

        //int number = 9;
        //int squareOrDouble = (number % 2 == 0) ? number * number : number * 2;
        //System.out.println(squareOrDouble); // Outputs: 18

        //public static int methodOne(int x){
          //  return x * 2;
        //}
        
        //public static int squareValue(int x) {
           // return x * x;
        //}
        
        //int number = 4;
        //int result = (number % 2 == 0) ? doubleValue(number) : squareValue(number);
        //System.out.println(result);
        //int number = 5;
        //if (number > 0)
         //   System.out.println("Number is positive");
            
        //System.out.println("number is not postive");

        int day = 1;
switch (day) {
    case 1:
        System.out.println("Monday");
        // i want to fall through!!!!! 
    case 2:
        System.out.println("Tuesday");
        
    case 3:
        System.out.println("Wednesday");
        
    default:
        System.out.println("Other day");
}
        

    }
}
