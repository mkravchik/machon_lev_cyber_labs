#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/types.h>

int secretCode = ###CODE###;

void dump_stack(void **stack, size_t n, void **arg0) {
    void** arg0_ = stack + n;
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
        printf("\n");
    }
}

void vuln(int win, char *str) {
    int win_ = win;
    int dummy[3 + ###RND###];
    char buf[64];
    size_t register dump_len = ((uintptr_t) &str - (uintptr_t) &buf[0]) / sizeof(void *) + 1;

    strcpy(buf, str);

    dump_stack((void **) buf, dump_len, (void **) &win);
    printf("win = %d\n", win);
    if (win == 1) {
        // execl("/bin/sh", "sh", NULL);
        printf("\nYOU WIN. At this point you would get a shell\n");
        // Print flag
        printf("Go get your treasure, the code is flag{%d}\n", secretCode);
        fflush(stdout);
        exit(0);

    } else {
        printf("Sorry, you lose.\n");
    }
    exit(0);
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: stack_overwrite [str]\n");
        return 1;
    }

    vuln(0, argv[1]);
    return 0;
}
