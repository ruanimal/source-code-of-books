#include <stdio.h>
#include <string.h>

int main(void) {
    char *p = "abcdef", *p2;
    printf("*p addr: %p, p[2]:%c content:%s \n", p, p[2], p);
    p2 = p;
    printf("*p2 addr: %p, p2[2]:%c content:%s \n", p2, p[2], p2);
    char p3[10];
    // p3 = p;   // p3不是可修改的左值
    strcpy(p3, p);
    printf("*p3 addr: %p, p3[2]:%c content:%s \n", p3, p3[2], p3);
    return 0;
}

/* output
*p addr: 0x10d9c2f3a, p[2]:c content:abcdef
*p2 addr: 0x10d9c2f3a, p2[2]:c content:abcdef
*p3 addr: 0x7ffee223d29e, p3[2]:c content:abcdef
 */
