import time


def is_perfect_square(calc, n):
    """
    Check if n is a perfect square using the calculator.

    Logic:
    1. Clear the calculator.
    2. Enter the number n digit by digit.
    3. Press the square root button ("√x").
    4. Read the result from the calculator.
    5. Check if the result is (approximately) an integer (meaning n has an integer square root).
    """
    calc.clear()
    for digit in str(n):
        calc.click_button(digit)
    calc.click_button("√x")
    time.sleep(1)  # wait for the calculator to compute
    result = calc.get_result()

    try:
        val = float(result)
    except ValueError:
        return False  # If result is not a number, n is not a perfect square

    # Check if val is very close to an integer (tolerance for floating point errors)
    return abs(val - round(val)) < 1e-9


def is_prime(calc, n):
    """
    Check if a number n is prime using only calculator operations.

    Logic:
    - Prime numbers are > 1 and have no divisors other than 1 and themselves.
    - Check all integers i from 2 up to sqrt(n).
    - For each i:
      * Calculate n ÷ i using the calculator.
      * Extract floor of the division result.
      * Multiply floor_val * i and check if it equals n.
      * If equal, n is divisible by i, so not prime.
    - If no divisor found, n is prime.
    """
    if n < 2:
        return False

    import math
    limit = int(math.sqrt(n)) + 1

    for i in range(2, limit):
        # Perform n ÷ i on calculator
        calc.clear()
        for d in str(n):
            calc.click_button(d)
        calc.click_button("÷")
        for d in str(i):
            calc.click_button(d)
        calc.click_button("=")
        time.sleep(0.5)
        div_result = calc.get_result()

        try:
            div_val = float(div_result)
        except ValueError:
            continue  # If result invalid, skip

        floor_val = int(div_val)

        # Perform floor_val × i on calculator to verify exact divisibility
        calc.clear()
        for d in str(floor_val):
            calc.click_button(d)
        calc.click_button("×")
        for d in str(i):
            calc.click_button(d)
        calc.click_button("=")
        time.sleep(0.5)
        mul_result = calc.get_result()

        try:
            mul_val = float(mul_result)
        except ValueError:
            continue

        # If floor_val * i == n, n is divisible by i => not prime
        if abs(mul_val - n) < 1e-9:
            return False

    return True  # No divisors found, n is prime


def prime_factors(calc, n):
    """
    Find prime factors of n using calculator steps only.

    Logic:
    - Start dividing n by smallest possible divisor starting from 2.
    - For each divisor:
      * Calculate n ÷ divisor.
      * Extract floor of the division.
      * Multiply floor_val × divisor.
      * If multiplication equals n exactly, divisor is a prime factor.
      * Append divisor to factors list and update n = floor_val.
      * Otherwise increment divisor and try again.
    - Continue until n reduced to 1.
    """
    factors = []
    current_n = n
    divisor = 2

    while current_n > 1:
        # current_n ÷ divisor on calculator
        calc.clear()
        for d in str(current_n):
            calc.click_button(d)
        calc.click_button("÷")
        for d in str(divisor):
            calc.click_button(d)
        calc.click_button("=")
        time.sleep(0.5)
        div_result = calc.get_result()

        try:
            div_val = float(div_result)
        except ValueError:
            break

        floor_val = int(div_val)

        # floor_val × divisor on calculator
        calc.clear()
        for d in str(floor_val):
            calc.click_button(d)
        calc.click_button("×")
        for d in str(divisor):
            calc.click_button(d)
        calc.click_button("=")
        time.sleep(0.5)
        mul_result = calc.get_result()

        try:
            mul_val = float(mul_result)
        except ValueError:
            break

        # If multiplication matches current_n exactly, divisor is a prime factor
        if abs(mul_val - current_n) < 1e-9:
            factors.append(divisor)
            current_n = floor_val  # Reduce n by dividing by divisor
        else:
            divisor += 1  # Try next divisor

    return factors
