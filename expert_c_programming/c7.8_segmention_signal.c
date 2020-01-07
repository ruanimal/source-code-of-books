#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

void handler(int s) {
    if (s == SIGBUS) {
        printf("now get a bus error signal.\n");
    } else if (s == SIGSEGV) {
        printf("now get a segmentation violation signal\n");
    } else if (s == SIGILL) {
        printf("now get an illegal instruction signal\n");
    }
    exit(1);
}

int main(void) {
    int *p = NULL;
    signal(SIGBUS, handler);
    signal(SIGSEGV, handler);
    signal(SIGILL, handler);
    *p = 0;
    return 0;
}
