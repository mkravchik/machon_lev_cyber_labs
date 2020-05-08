#include <stdio.h>

int main(int argc, char *argv[]){
        signed short signed_short = -1;
        unsigned short unsigned_short = 0;

        signed int signed_int = -1;
        unsigned int unsigned_int = 0;

        /*  Integral promotion rules promote to types 'int' and 'int'; Usual
	    arithmetic rules don't need to do anything because types are the same.
	    */
        if(signed_short < unsigned_short){
                printf("%hd < %hu\n", signed_short, unsigned_short);
        }else{
                printf("%hd > %hu\n", signed_short, unsigned_short);
        }

        /*  Integral promotion rules don't need to do anything because types
	    are 'int' and 'unsigned int'.  Usual arithmetic conversion rules
	    require that types be both signed or both unsigned an in this case
	    the signed_int is converted to an unsigned int in a well-defined
	    way to have the value UINT_MAX, which is greater than 0.
	   */
        if(signed_int < unsigned_int){
                printf("%d < %u\n", signed_int, unsigned_int);
        }else{
                printf("%d > %u\n", signed_int, unsigned_int);
        }
        return 0;
}
