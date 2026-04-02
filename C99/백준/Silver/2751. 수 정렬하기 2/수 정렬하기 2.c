#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define maxArraySize 1000000


/*
struct Array {
	int data[maxArraySize];
	int size;
	int back;
	int front;
};

void InitArray(struct Array* array) {
	array->size = 0;
	array->back = 0;
	array->front = 0;
}

void Push(struct Array* array, int x) {
	array->data[array->back++] = x;
	array->size++;
}

int Pop(struct Array* array) {
	return array->data[array->front++];
}

int Front(struct Array* array) {
	return array->data[array->front];
}

void Marge(struct Array* array, struct Array* left, struct Array* right) {

	for (int i = 0; i < (left->size + right->size); i++) {
		if (Front(left) >= Front(right)) {
			Push(array, Pop(left));
		}
		else {
			Push(array, Pop(right));
		}
	}
}

void MargeSort(struct Array* array) {
	struct Array left;
	struct Array right;

	InitArray(&left);
	InitArray(&right);


	if (array->size != 1) {
		//반으로 나누기
		for (int i = 0; i < array->size / 2; i++) {
			if (array->size != 0) {
				Push(&left, array->data[i]);
			}
			else {
				printf("Array empty!\n");
			}
		}

		//반으로 나누기
		for (int i = array->size / 2; i < array->size; i++) {
			if (array->size != 0) {
				Push(&right, array->data[i]);
			}
			else {
				printf("Array empty!\n");
			}
		}
		MargeSort(&left);
		MargeSort(&right);

		Marge(array, &left, &right);

	}
}

int main() {
	int n;
	struct Array array;
	InitArray(&array);
	

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int x;
		scanf("%d", &x);
		Push(&array, x);
	}

	MargeSort(&array);
	for (int i = 0; i < n; i++) {
		printf("%d\n", Pop(&array));
	}


	return 0;
}

*/

void Merge(int arr[], int left, int right, int mid, int temp[]) {
	int i = left;
	int j = mid + 1;
	int k = left; //temp의 인덱스

	while (i <= mid && j <= right) {
		if (arr[i] <= arr[j]) {
			temp[k++] = arr[i++];
		}
		else {
			temp[k++] = arr[j++];
		}
	}

	while (i <= mid || j <= right) {
		if (i <= mid) {
			temp[k++] = arr[i++];
		}
		else {
			temp[k++] = arr[j++];
		}
	}

	for (int p = left; p < k; p++) {
		arr[p] = temp[p];
	}
}

void MergeSortRecursive(int arr[], int left, int right, int temp[]) {
	if (left < right) {
		int mid = (left + right) / 2;

		MergeSortRecursive(arr, left, mid, temp);
		MergeSortRecursive(arr, mid + 1, right, temp);

		Merge(arr, left, right, mid, temp);
	}
}

void MergeSort(int arr[], int n) {
	int* temp = (int*)malloc(n * sizeof(int));
	if (temp == NULL) {
		printf("MergeSort: Memory 터짐\n");
		return;
	}

	MergeSortRecursive(arr, 0, n-1, temp);
}

int main() {
	int n;
	scanf("%d", &n);

	int* arr = (int*)malloc(n * sizeof(int)); //malloc 앞 (int*)는 저 주소는 int로 읽어야한다는걸 명시해줌.
	if (arr == NULL) {
		printf("Main: Memory 터짐\n");
		return 1;
	}

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	MergeSort(arr, n);

	for (int i = 0; i < n; i++) {
		printf("%d\n", arr[i]);
	}

}