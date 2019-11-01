#include <stdio.h>

int main(void){
    unsigned int num = 0xffffffff;

    printf("num is %zu bits long\n", sizeof(num) * 8);
    printf("num = 0x%x\n", num);
    printf("num + 1 = 0x%x\n", num + 1);

    return 0;
}
