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
    printf("Invalid number of arguments\n");
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
  char *alphabet_a[11] = {'b', 'd', 'f', 'h', 'l','n', 'p', 'r', 't', 'v', 'y'};

  char *alphabet_b[12] = {'a', 'c', 'e', 'g', 'i', 'm','o', 'q', 's', 'u', 'x', 'z'};

  //Search in the alphabet the same word
  for(int i = 0; i < 12; i++)
  {
    if(ch == alphabet_b[i])
    {
        return alphabet_b[(i + (keyValue*2)) % 11];
    }else if (ch== alphabet_a[i]) {
        return alphabet_a[(i+keyValue % 10)];
    }
  }
}

bool isExeption(char ch)
{
  return ch == ' ' || ch == ',' || ch == '.' || ch == '?' || ch == '!' ||
  ch == '"' || ch == '\n' || ch == ';' || ch == ':' || ch == ']' || ch == '[';

}
