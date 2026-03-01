#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

//forward decl
int setresgid(uid_t ruid, uid_t euid, uid_t suid);

/*
 * Goal: Get the program to run this function.
 */
void shell(void) {
    execl("/bin/sh", "sh", NULL);
}

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


void vuln(char *str) {
    char buf[64];
    strcpy(buf, str);
    //dump_stack((void **) buf, 21, (void **) &str);
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: buffer_overflow [str]\n");
        return 1;
    }

    uid_t egid = getegid();
    int res = setresgid(egid, egid, egid);
    printf("res %d\n", res);
    printf("main function = %p. But where is the shell?\n", main);
    vuln(argv[1]);
    return 0;
}


