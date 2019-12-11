/* 总线错误
其实并没有出现, 很怪..
*/
#include <stdio.h>

int main(void) {
    union {
        char a[10];
        int i;
    } u;
    int *p = (int *) & (u.a[1]);
    *p = 17; /* p中未对齐的地址会引起一个总线错误*/
    printf("*p : %d", *p);
    return 0;
}
