package HEnums;

public class Main {
public static void main(String[] args) {
    printDay(Day.MONDAY); // Valid
    //printDay(5);       // Invalid, won't compile

    Day today = Day.FRIDAY;
    System.out.println("Today is: " + today);

    for (Day day : Day.values()) {
        System.out.println(day);
    }

    Day day = Day.valueOf("MONDAY");
    System.out.println("Day is: " + day);

    Level level = Level.HIGH;
    System.out.println("Severity: " + level.getSeverity());
    System.out.println("Severity: " + level.getDescription());

    Day today1 = Day.FRIDAY;

    switch (today1) {
        case MONDAY -> System.out.println("Start of the work week!");
        case FRIDAY -> System.out.println("Almost the weekend!");
        case SUNDAY -> System.out.println("Relax, it's Sunday!");
        default -> System.out.println("Midweek day.");
    }


    StringBuilder sb = new StringBuilder("Hello");
    sb.append(" World"); // Appends " World"
    sb.insert(5, ",");   // Inserts a comma after "Hello"
    sb.replace(0, 5, "Hi"); // Replaces "Hello" with "Hi"
    sb.reverse();        // Reverses the string
    System.out.println(sb.toString()); // Output: "dlroW ,iH"
}
    
    public static void printDay(Day day) {
        System.out.println("The day is: " + day);
    }



}
