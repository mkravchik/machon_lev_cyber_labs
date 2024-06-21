#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int secretCode = ###CODE###;

#define STATUS_GUESSED 0x0
#define STATUS_FAIL 0x1
typedef struct _word_struct
{
    char word[32 + ###RND###];
    int status;
} word_struct;

int get_input(char *word, int len)
{
    int wordSize = 0;
    // Read into a new buffer to avoid buffer overflow
    char *locWord = malloc(len + 4);
    if(!locWord)
        return -2;
    printf("Enter your guess: ");
    fgets(locWord,len + 4,stdin);
    wordSize = strlen(locWord);
    
    // strip newline character
    if(locWord[wordSize-1] == '\n')
        locWord[wordSize-1] = '\0';
    
    if(strlen(locWord) > len)
    {
	    free(locWord);
	    return -1;
    }

    strcpy(word,locWord);
    free(locWord);
    return 1;
}

void check_input(word_struct* w)
{
    //todo: implement this
    printf("Incorrect word!\n");
}

int main(int argc, char* argv[])
{
    word_struct guess;
    int ret;
    
    printf("Welcome to Aladdin's magic cave (simple version)!\n");
    printf("Enter the secret word and get the treasure cave entrance code!\n");

    // set the result to fail by default
    guess.status = STATUS_FAIL;

    ret = get_input(guess.word, sizeof(guess.word));
    if(ret == -1)
    {
        printf("Exiting due to buffer overflow!\n");
        return -1;
    }
    else if(ret == -2)
    {
        printf("Out of resources! Exiting...\n");
        return -2;
    }
    check_input(&guess);

    if(guess.status == STATUS_GUESSED)
        printf("It was cool, wasn't it ?! Go get your treasure, the code is %d\n", secretCode);
    else
        printf("Better luck next time!\n");

    return 0; 
}

