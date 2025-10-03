def input_value() -> int:
    return int(input("Enter integer x: "))

def display_array(arr):
    print(f"\nInput integer is: {arr}")

def reverse_integer(x):
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x != 0:
        digit = x % 10
        x //= 10
        # Check overflow before multiplying or adding
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
            return 0
        rev = rev * 10 + digit
    return sign * rev if INT_MIN <= sign * rev <= INT_MAX else 0

if __name__ == "__main__":
    x = input_value()
    display_array([x])
    result = reverse_integer(x)
    print(f"Reversed integer is: {result}")


