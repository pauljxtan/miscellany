/* K&R Exercise 1-15 */

#include <stdio.h>

float fahr_to_celsius(float);
float celsius_to_fahr(float);

int main() {
    float fahr, celsius;

    printf("Fahrenheit\tCelsius\n");
    for (fahr = 0.0; fahr <= 300.0; fahr += 20.0) {
        celsius = fahr_to_celsius(fahr);
        printf("%3.0f\t\t%5.1f\n", fahr, celsius);
    }
    printf("\n");

    printf("Fahrenheit\tCelsius\n");
    for (fahr = 300.0; fahr >= 0.0; fahr -= 20.0) {
        celsius = fahr_to_celsius(fahr);
        printf("%3.0f\t\t%5.1f\n", fahr, celsius);
    }
    printf("\n");

    printf("Celsius\t\tFahrenheit\n");
    for (celsius = 0.0; celsius <= 150.0; celsius += 10.0) {
        fahr = celsius_to_fahr(celsius);
        printf("%3.0f\t\t%5.1f\n", celsius, fahr);
    }
    printf("\n");

    printf("Celsius\t\tFahrenheit\n");
    for (celsius = 150.0; celsius >= 0.0; celsius -= 10.0) {
        fahr = celsius_to_fahr(celsius);
        printf("%3.0f\t\t%5.1f\n", celsius, fahr);
    }
    printf("\n");

    return 0;
}

float fahr_to_celsius(float fahr) {
    float celsius;

    celsius = (5.0 / 9.0) * (fahr - 32.0);
    return celsius;
}

float celsius_to_fahr(float celsius) {
    float fahr;

    fahr = (9.0 / 5.0) * celsius + 32.0;
    return fahr;
}
