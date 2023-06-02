#include <ctype.h> // archive added for reference reasons
#include <cs50.h> // below is an old C code with cs50 functions
#include <stdio.h> // it has been added for reference for ASCII substitution 
#include <stdlib.h> // and case sensitivity (to be added later in the final python version)
#include <string.h>
void cipher(string word, int n);
bool only_digits(string s);
string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string alphalow = "abcdefghijklmnopqrstuvwxyz";
int main(int argc, string argv[])
{
    if (argc != 2 || only_digits(argv[1]) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    string word = get_string("plaintext: ");
    cipher(word, atoi(argv[1]));
}
void cipher(string word, int n)
{
    while (n > 26)
    {
        n = n - 26;
    }
    char word1[strlen(word)];
    for (int i = 0; word[i] != '\0'; i++)
    {
        if (word[i] > 64 && word[i] < 91)
        {
            int letter = (word[i] - 65);
            int shift = letter + n;
            if (shift >= 26)
            {
                shift = shift - 26;
            }
            char ch = alpha[shift];
            word1[i] = ch;
        }
        else if (word[i] > 96 && word[i] < 123)
        {
            int letter = (word[i] - 97);
            int shift = letter + n;
            if (shift >= 26)
            {
                shift = shift - 26;
            }
            char ch = alphalow[shift];
            word1[i] = ch;
        }
        else
        {
            word1[i] = word[i];
        }
    }
    printf("ciphertext: %s\n", word1);
}
bool only_digits(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {
        if (isdigit(s[i]) ==  false)
        {
            return false;
        }
    }
    return true;
}
