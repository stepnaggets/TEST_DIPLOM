"""
Реализация алгоритмов сортировки и поиска.
"""

from typing import List, Optional


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Сортировка пузырьком.
    
    Args:
        arr (List[int]): Неотсортированный список.
    
    Returns:
        List[int]: Отсортированный список.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Бинарный поиск в отсортированном массиве.
    
    Args:
        arr (List[int]): Отсортированный список.
        target (int): Искомый элемент.
    
    Returns:
        Optional[int]: Индекс элемента или None, если не найден.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def fibonacci(n: int) -> int:
    """
    Вычисляет n-ное число Фибоначчи.
    
    Args:
        n (int): Номер числа.
    
    Returns:
        int: Число Фибоначчи.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)
    
    target = 22
    index = binary_search(sorted_arr, target)
    print(f"Index of {target}:", index)