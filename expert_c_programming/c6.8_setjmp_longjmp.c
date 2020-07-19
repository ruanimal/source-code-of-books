#include <stdio.h>
#include <setjmp.h>
#include <string.h>

jmp_buf buf;

void banana(void) {
    printf("in banana() \n");
    longjmp(buf, 1);
    printf("you'll never see this, because i longjmp'd\n");
}

int main(void) {
    if (setjmp(buf)) {
        printf("back in main, buf[0]: %d\n", buf[0]);
    } else {
        buf[0] = 42;
        printf("first time through\n");
        banana();
    }
    return 0;
}
