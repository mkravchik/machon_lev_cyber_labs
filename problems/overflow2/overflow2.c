#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
//#include "dump_stack.h"
//forward decl
int setresgid(uid_t rgid, uid_t egid, uid_t sgid);
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
        if (&stack[n] == arg0 - 2) {
            printf(" (saved ebp)");
        }
        printf("\n");
    }
}

void vuln(int win, char *str) {
    int win_ = win;
    int dummy[3];
    char buf[64];
    strcpy(buf, str);
    dump_stack((void **) buf, 26, (void **) &win);
    printf("win = %d\n", win);
    if (win == 1) {
        execl("/bin/sh", "sh", NULL);
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

    uid_t egid = getegid();
    int res = setresgid(egid, egid, egid);
    printf("res %d\n", res);
    vuln(0, argv[1]);
    return 0;
}
