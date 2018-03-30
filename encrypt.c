#include<stdio.h>
#include<ctype.h>
#include <stdbool.h>


void encrypt(int keyValue, FILE *text, FILE *encryptedText);
char encode(char ch, int keyValue);
bool isExeption(char ch);

int main(int argc, char* argv[])
{

  int keyValue;
  FILE *text;
  FILE *encryptedText;

  if (argc != 4)
  {
    printf("Invalid number of arguments");
    exit(0);
  }
  else
  {
    keyValue = atoi(argv[1]);
    text = fopen(argv[2], "r");
    encryptedText = fopen(argv[3], "w");
  }
  encrypt(keyValue, text, encryptedText);
}


void encrypt(int keyValue,FILE *text, FILE *encryptedText)
{
  int x;
  char newCh;
  // Read a text file character by character
  while (( x = fgetc(text)) != EOF)
  {
    if(isExeption(x)){
      fprintf(encryptedText, "%c", x );
    }
    // Upper Case
    else if (isupper(x))
    {
      x = tolower(x);
      newCh = (char) encode(x, keyValue);
      newCh = toupper(newCh);
      fprintf(encryptedText, "%c", newCh );

    }
    else
    {
    newCh =  (char) encode(x, keyValue);
    fprintf(encryptedText, "%c", newCh );

    }
  }
  fclose(text);

}

char encode(char ch, int keyValue)
{
  //Define a latin alphabet
  char *alphabet[23] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'};

  //Search in the alphabet the same word
  for(int i = 0; i < 23; i++)
  {
    if(ch == alphabet[i])
    {
      //Special case characters
      if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
      {
        return alphabet[(i + (keyValue * 3)) % 23];
      }
      else
      {
        //Encode the current character
        return alphabet[(i + keyValue) % 23];
      }
    }
  }
}

bool isExeption(char ch)
{
  return ch == ' ' || ch == ',' || ch == '.' || ch == '?' || ch == '!' ||
  ch == '"' || ch == '\n' || ch == ';' || ch == ':';

}
