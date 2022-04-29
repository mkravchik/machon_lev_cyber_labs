#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int secretCode = ###CODE###;

void print_secret_code(){
    //TODO - call this from somewhere...
    printf("You get better at this stuff, ah?! Go get your treasure, the code is %d\n", secretCode);
}

void  fill_array(int array[], size_t len){
  unsigned int i;
  for (i = 0; i < len; i++){
    array[i] = i * 10;
  }
}

void place_int_array(int slot,int value){
  int array[###SAFES###];
  fill_array(array, sizeof(array)/sizeof(array[0]));

  if(slot>###SAFES###) //we stop bad guys here
    printf("safe number is greater than ###SAFES###, out of bounds.\n");
  else{
    array[slot]=value; 
    printf("filled safe %d with %d.\n",slot,value);
  }
  return;
}

int main(int argc,char **argv){
  if(argc!=3){
    printf("Welcome to Alladin's magic cave!\n");
    printf("Enter the secret number into the right safe and get the treasure cave entrance code!\n");
    printf("syntax: %s [SAFE NUMBER] [SECRET NUMBER]\n",argv[0]);

    //TEMP TEMP - for debugging only
    printf("print_secret_code function = %p\n", print_secret_code);
  }
  else
    place_int_array(atoi(argv[1]),atoi(argv[2]));
  
  exit(0);
}
