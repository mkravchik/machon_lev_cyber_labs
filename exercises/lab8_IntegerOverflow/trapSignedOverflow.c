#include <stdio.h>
#include <limits.h>
int add_signed(int a, int b){
	return a + b;
}

int main(int argc, char *argv[]){
	int a = INT_MAX;
	int b = INT_MAX;
	printf("%d\n", add_signed(a,b));
	return 0;
}
