#include <stdio.h>

extern int count;   // 引用式申明, 外部链接

static int total = 0;   // 文件作用域, 静态定义, 内部链接

void accumulate(int k);   // k, 函数原型作用域

void accumulate(int k) {   // k, 块级作用域
    static int subtotal = 0;   // 块级作用域, 静态定义, 内部链接
    if (k <= 0) {
        printf("loop cycle: %d\n", count);
        printf("subtotal: %d; total: %d\n", subtotal, total);
        subtotal = 0;
    } else {
        subtotal += k;
        total += k;
    }
}
