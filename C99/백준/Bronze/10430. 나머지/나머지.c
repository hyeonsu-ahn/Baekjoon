#include <stdio.h>

int main(void) {
	int A;
	int B;
	int C;

	scanf("%d %d %d", &A, &B, &C);

	int one = (A + B) % C;
	int two = ((A % C) + (B % C)) % C;
	int three = (A*B) % C;
	int four = ((A % C) *(B % C)) % C;

	printf("%d\n", one);
		printf("%d\n", two);
		printf("%d\n", three);
		printf("%d\n", four);
}