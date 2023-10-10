def count_inversions(arr):
    def merge(arr, left, mid, right):
        left_half = arr[left:mid+1]
        right_half = arr[mid+1:right+1]
        
        i = j = k = 0
        inversions = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[left + k] = left_half[i]
                i += 1
            else:
                arr[left + k] = right_half[j]
                j += 1
                inversions += len(left_half) - i  # Count inversions when an element from the right is smaller

            k += 1

        while i < len(left_half):
            arr[left + k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[left + k] = right_half[j]
            j += 1
            k += 1

        return inversions

    def count_inversions_helper(arr, left, right):
        inversions = 0
        if left < right:
            mid = (left + right) // 2
            inversions += count_inversions_helper(arr, left, mid)
            inversions += count_inversions_helper(arr, mid + 1, right)
            inversions += merge(arr, left, mid, right)
        return inversions

    return count_inversions_helper(arr, 0, len(arr) - 1)

# Example usage:
arr = [1, 3, 2, 4, 1]
inversions = count_inversions(arr)
print("Number of inversions:", inversions)
