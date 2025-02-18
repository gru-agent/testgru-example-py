import pytest
from src.sort import bubble_sort

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_random_list():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_duplicate_elements():
    assert bubble_sort([3, 3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3, 3]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([-5, -10, 0, -3, 8, -1]) == [-10, -5, -3, -1, 0, 8]

def test_bubble_sort_floating_numbers():
    assert bubble_sort([3.14, 1.41, 2.71, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_bubble_sort_mixed_numbers():
    assert bubble_sort([1, -2, 3.14, -4.5, 0, 2.5]) == [-4.5, -2, 0, 1, 2.5, 3.14]

def test_bubble_sort_large_numbers():
    assert bubble_sort([1000000, 999999, 1000001]) == [999999, 1000000, 1000001]

def test_bubble_sort_small_numbers():
    assert bubble_sort([0.0001, 0.0002, 0.0003]) == [0.0001, 0.0002, 0.0003]
