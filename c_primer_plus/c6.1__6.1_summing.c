#include <stdio.h>

int main(void) {
    long num;
    long sum = 0L;

    // int status;
    printf("Please enter an integer to be summed ");
    printf("(q to quit): ");
    while (scanf("%ld", &num) == 1) {
        sum += num;
        printf("Please enter next integer (q to quit): ");
    }
    printf("Those integers sum to %ld.\n", sum);
}
