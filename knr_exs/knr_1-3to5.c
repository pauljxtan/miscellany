/* K&R Exercise 1-3:
 * Modify the temperature conversion program to print a heading above the
 * table.
 * K&R Exercise 1-4
 * Write a program to print the corresponding Celsius to Fahrenheit table.
 * K&R Exercise 1-5
 * Modify the temperature conversion program to print the table in reverse
 * order, that is, from 300 degrees to 0. */

#include <stdio.h>

int main() {
    float fahr, celsius;

    printf("Fahrenheit\tCelsius\n");
    for (fahr = 0.0; fahr <= 300.0; fahr += 20.0) {
        celsius = (5.0 / 9.0) * (fahr - 32.0);
        printf("%3.0f\t\t%5.1f\n", fahr, celsius);
    }
    printf("\n");

    printf("Fahrenheit\tCelsius\n");
    for (fahr = 300.0; fahr >= 0.0; fahr -= 20.0) {
        celsius = (5.0 / 9.0) * (fahr - 32.0);
        printf("%3.0f\t\t%5.1f\n", fahr, celsius);
    }
    printf("\n");

    printf("Celsius\t\tFahrenheit\n");
    for (celsius = 0.0; celsius <= 150.0; celsius += 10.0) {
        fahr = (9.0 / 5.0) * celsius + 32.0;
        printf("%3.0f\t\t%5.1f\n", celsius, fahr);
    }
    printf("\n");

    printf("Celsius\t\tFahrenheit\n");
    for (celsius = 150.0; celsius >= 0.0; celsius -= 10.0) {
        fahr = (9.0 / 5.0) * celsius + 32.0;
        printf("%3.0f\t\t%5.1f\n", celsius, fahr);
    }
    printf("\n");

    return 0;
}
