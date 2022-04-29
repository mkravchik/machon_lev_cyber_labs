#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int secretCode = ###CODE###;

#define STATUS_WINNER 'WIN!'

typedef struct _word_struct
{
    char word[32 + ###RND###];
    char result[48 + ###RND###];
    int status;
} word_struct, *word_data;

int get_input(char *word, int len)
{
    int wordSize = 0;
    char *locWord = malloc(len+4);
    if(!locWord)
        return -2;
    printf("Enter your guess: ");
    fgets(locWord,len+4,stdin);
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

void check_input(word_data w)
{
    //todo: implement this
    printf("Incorrect word!\n");
    w->status = strlen(w->word);
}

int main(int argc, char* argv[])
{
    //check with sizeof - off by one + strcpy (overwrite the next with 0)
    //strcpy that will copy that additional symbol
    //strncat that will start later because there is a 0 later
    word_struct guess;
    int i,offset,len,ret;
    printf("Welcome to Alladin's magic cave!\n");
    printf("Enter the secret word and get the treasure cave entrance code!\n");
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
    if(guess.status == STATUS_WINNER)
        strcpy(guess.result,"CORRECT! YOU ENTERED: ");
    else
        strcpy(guess.result,"WRONG! YOUR WORD:  ");

    //we don't use unsafe str functions, we copy strings carefully one-by-one!
    offset = strlen(guess.result);
    len = strlen(guess.word);    
    for(i = 0; i < len; ++i)
        guess.result[offset+i] = guess.word[i];
    guess.result[offset+i] = '\0';

    printf("%s\n",guess.result);

    // give them the flag?
    if(guess.status == STATUS_WINNER)
        printf("It was cool, wasn't it ?! Go get your treasure, the code is %d\n", secretCode);
    else
        printf("Better luck next time!\n");

    return 0; 
}

