#include <iostream>
#include <chrono>
#include <thread>
#include <random>
#include <algorithm>

// Bubblesort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
                std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
            if (arr[j] > arr[j+1])
                std::swap(arr[j], arr[j+1]);
        }
        //std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
    }
}

// selectionsort
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int minIndex = i;
        for (int j = i+1; j < n; j++) {
                std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
            if (arr[j] < arr[minIndex])
                minIndex = j;
        }
        std::swap(arr[i], arr[minIndex]);
        //std::this_thread::sleep_for(std::chrono::milliseconds(1000)); // تاخیر 1 ثانیه
    }
}

// merge sort
void merge(int arr[], int left, int middle, int right) {
    int i, j, k;
    int n1 = middle - left + 1;
    int n2 = right - middle;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++){
            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
        L[i] = arr[left + i];}
    for (j = 0; j < n2; j++){
            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
        R[j] = arr[middle + 1 + j];
    }

    i = 0;
    j = 0;
    k = left;

    while (i < n1 && j < n2) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // تاخیر 1 ثانیه
        arr[k] = R[j];
        j++;
        k++;
    }

    //std::this_thread::sleep_for(std::chrono::milliseconds(1000)); // تاخیر 1 ثانیه
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int middle = left + (right - left) / 2;

        mergeSort(arr, left, middle);
        mergeSort(arr, middle + 1, right);

        merge(arr, left, middle, right);
    }
}

int main() {

    int arr[10] = {9, 2, 8, 5, 1, 4, 7, 6, 3, 10};

    // Bubblesort
    auto startTime = std::chrono::steady_clock::now();
    bubbleSort(arr, 10);
    auto endTime = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endTime - startTime);
    std::cout << "runtime bubblesort  :  " << duration.count() << " microseconds" << std::endl;

    // selectionSort
    startTime = std::chrono::steady_clock::now();
    selectionSort(arr, 10);
    endTime = std::chrono::steady_clock::now();
    duration = std::chrono::duration_cast<std::chrono::microseconds>(endTime - startTime);
    std::cout << "runtime selection sort  :  " << duration.count() << " microseconds" << std::endl;

    // mergeSort
    startTime = std::chrono::steady_clock::now();
    mergeSort(arr, 0, 9);
    endTime = std::chrono::steady_clock::now();
    duration = std::chrono::duration_cast<std::chrono::microseconds>(endTime - startTime);
    std::cout << "runtime mergesort  :   " << duration.count() << " microseconds" << std::endl;

    return 0;
}
