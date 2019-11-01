#include <stdio.h>

int main(void){
    int l, l1, l2;
    short s;
    char c;

    l = 0xdeadbeef;
    s = l;
    c = l;

	l1 = s;
	l2 = c;
 
    printf("l = 0x%x %d (%zu bits)\n", l, l, sizeof(l) * 8);
    printf("s = 0x%hx %hd (%zu bits)\n", s, s, sizeof(s) * 8);
    printf("c = 0x%hhx %hhd (%zu bits)\n", c, c, sizeof(c) * 8);
    printf("l1 = 0x%x %d (%zu bits)\n", l1, l1, sizeof(l1) * 8);
    printf("l2 = 0x%x %d (%zu bits)\n", l2, l2, sizeof(l2) * 8);
}
