from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from calculator_page import CalculatorPage
from utils import is_perfect_square, is_prime, prime_factors

service = Service('C:\\Users\\Home\\Downloads\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
calc = CalculatorPage(driver)

# Question 1: Expression calculation
expressions = [
    "10+5-2*2/1",    # Expected: 26
    "7+3*4-6/2"      # Expected: 7+3=10 → *4=40 → -6=34 → /2=17 (calculator steps)
]
for expr in expressions:
    result = calc.calculate_expression(expr)
    print(f"Question 1 - Result of '{expr}': {result}")

# Question 2: Perfect square check
square_tests = [49, 50]  # 49 is perfect square (7x7), 50 is not
for n in square_tests:
    if is_perfect_square(calc, n):
        print(f"Question 2 - {n} is a perfect square")
    else:
        print(f"Question 2 - {n} is not a perfect square")

# Question 3: Prime number check
prime_tests = [29, 30]  # 29 is prime, 30 is not
for n in prime_tests:
    if is_prime(calc, n):
        print(f"Question 3 - {n} is a prime number")
    else:
        print(f"Question 3 - {n} is not a prime number")

# Question 4: Prime factorization
factor_tests = [84, 60]  # 84 = [2, 2, 3, 7], 60 = [2, 2, 3, 5]
for n in factor_tests:
    factors = prime_factors(calc, n)
    print(f"Question 4 - Prime factors of {n}: {factors}")

driver.quit()
