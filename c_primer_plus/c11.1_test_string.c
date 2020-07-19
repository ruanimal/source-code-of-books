#include <stdio.h>

static char s[] = "aaaa";

int main(void) {
    printf("%s, %p %p", s, &s, &"aaaa");
}
