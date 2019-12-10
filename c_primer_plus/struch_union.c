/*
结构体和联合一起使用, 为数据提供不同的视图
 */
#include <stdio.h>
#include <string.h>

void printBits(unsigned char num) {
   for(int bit=0;bit<(sizeof(unsigned char) * 8); bit++) {
      printf("%i ", num & 0x01);
      num = num >> 1;
   }
}

struct box_props {
    unsigned int a : 1;
    unsigned int b : 1;
    unsigned int c : 1;
    unsigned int d : 1;
    unsigned int e : 1;
    unsigned int f : 1;
    unsigned int g : 1;
    unsigned int h : 1;
};

union View {
    struct box_props st_view;
    unsigned char us_view;
};

int main(void) {
    union View box = {{1,0,1,1,1,0,0,0}};
    printf("a is %d\n", box.st_view.a);
    printf("b is %d\n", box.st_view.b);
    printf("c is %d\n", box.st_view.c);
    printf("d is %d\n", box.st_view.d);
    printf("e is %d\n", box.st_view.e);
    printf("f is %d\n", box.st_view.f);
    printf("g is %d\n", box.st_view.g);
    printf("h is %d\n", box.st_view.h);
    printf("total is ");
    printBits(box.us_view);
    return 0;
}
