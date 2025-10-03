def input_values() -> tuple[int, int]:
    x = int(input("Enter base x: "))
    n = int(input("Enter exponent n: "))
    return x, n

def pow_func(x: int, n: int):
    if n == 0:
        return 1
    if n < 0:
        if x == 0:
            raise ValueError("0 cannot be raised to a negative exponent")
        x = 1 / x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

if __name__ == "__main__":
    x, n = input_values()
    power = pow_func(x, n)
    print(f"Result of pow({x},{n}): {power}\n")
