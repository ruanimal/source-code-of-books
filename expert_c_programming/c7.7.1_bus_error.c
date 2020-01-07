/* 总线错误
其实并没有出现, 很怪..
x86 允许地址不对齐
*/
#include <stdio.h>
#include <string.h>

void printBytes(char * s) {
    int idx = 0;
    printf("string: ");
    for (idx = 0; idx < 10; idx++) {
        printf("%x ", s[idx]);
    }
    printf("\n");
}

int main(void) {
    union {
        char a[10];
        int i;
    } u;

    // char s[] = "abcd";
    // printf("s[0] %p \n", &s[0]);
    // printf("s[1] %p \n", &s[1]);
    // printf("s[2] %p \n", &s[2]);
    // printf("sizeof s %lu \n", sizeof(s));

    // printf("sizeof u %lu \n", sizeof(u));
    int *p = (int *) & (u.a[1]);
    *p = 17; /* p中未对齐的地址会引起一个总线错误*/
    // printBytes(u.a);
    // printf("u addr %p \n", &u);
    // printf("u.a[1] addr %p \n", &u.a[1]);
    // printf("u.a[2] addr %p \n", &u.a[2]);
    // printf("*p addr:%p : %d", p, *p);
    return 0;
}
