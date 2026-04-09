#include <stdio.h>
  #include <string.h>

  int main() {
      int count = 0;
      int word;
      int inWord = 0;  // 현재 단어 안에 있는지 여부

      while((word = getchar()) != '\n' && word != EOF) {
          if(word != ' ') {
              if(inWord == 0) {
                  count++;       // 새 단어 시작
                  inWord = 1;
              }
          } else {
              inWord = 0;
          }
      }

      printf("%d", count);
  }