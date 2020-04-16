# Ben Lizza
# 04/61/20

    def bubble_sort(self, arr):
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if arr[i - 1] > arr[i]:
                    swap(i - 1, i)
                    swapped = True

        return arr

    def selection_sort(self, arr):
        for i in range(len(arr)):
            minimum = i

            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j

            arr[minimum], arr[i] = arr[i], arr[minimum]

        return arr

    def insertion_sort(self, arr):
        for i in range(len(arr)):
            cursor = arr[i]
            pos = i

            while pos > 0 and arr[pos - 1] > cursor:
                arr[pos] = arr[pos - 1]
                pos = pos - 1

            arr[pos] = cursor

        return arr

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left, right = merge_sort(arr[:mid]), merge_sort(arr[:mid])

        return merge(left, right, arr.copy())

    def merge(self, left, right, merged):
        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor + right_cursor] = left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1
        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]
        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]

        return merged
# QUICK SORT
    def partition(self, array, begin, end):
        pivot_idx = begin
        for i in xrange(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(self, array, begin, end):
        if begin >= end:
            return
        pivot_idx = partition(array, begin, end)
        quick_sort_recursion(array, begin, pivot_idx-1)
        quick_sort_recursion(array, pivot_idx+1, end)

    def quick_sort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        return quick_sort_recursion(array, begin, end)

