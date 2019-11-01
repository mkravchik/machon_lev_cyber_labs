#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define REAL_PWD "MycoolestPWD"

void dump_stack(void **stack, size_t n, void **arg0) {
    //printf("Stack dump (stack at %p, len %d, arg0 at %p): \n", stack, n, arg0);
    while (n-- > 0) {
        printf("0x%08x: 0x%08x", (unsigned int)&stack[n], (unsigned int)stack[n]);
        if (n == 0) {
            printf(" (beginning of buffer)");
        }
        if (&stack[n] == arg0 + 1) {
            printf(" (second argument)");
        }
        if (&stack[n] == arg0) {
            printf(" (first argument)");
        }
        if (&stack[n] == arg0 - 1) {
            printf(" (saved eip)");
        }
        if (&stack[n] == arg0 - 2) {
            printf(" (saved ebp)");
        }
        printf("\n");
    }
}
 
void main(int argc, char** argv[])
{
    char correct[4] = "NO!";
    char response[16];
    puts("Enter password: ");
    gets(response);
    dump_stack((void **) response, 12, (void **) &argc);
    if (strcmp(response, REAL_PWD) == 0)
        strcpy(correct,"YES");
    printf("correct (%p) %s response (%p) %s\n", correct, correct, response, response );
    if (strcmp(correct,"YES") == 0)
        printf ("You win!\n");
    else 
	    printf("You lose :-)\n");
}

