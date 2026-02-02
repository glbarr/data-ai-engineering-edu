# Problem 001 — Container With Most Water
# Two-pointers approach (O(n) time, O(1) space)

def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_a = 0
    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        if area > max_a:
            max_a = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_a

if __name__ == "__main__":
    print(max_area([1,8,6,2,5,4,8,3,7]))  # expected 49
