# 🧽 Web Calculator Automation Project

Automation of mathematical operations using a web browser on [theonlinecalculator.com](https://www.theonlinecalculator.com), implemented with Python, Selenium WebDriver, and the Page Object Model (POM) design pattern.

---

## 📁 Project Structure

```
calculator_project/
├── calculator_test.py         # Main test execution file
├── calculator_page.py         # Page Object representing the calculator interface
└── utils.py                   # Utility functions: perfect square, prime check, prime factorization
```

---

## ⚙️ Technologies Used

* Python 3
* Selenium WebDriver
* ChromeDriver
* Page Object Model (POM)

---

## ✨ Features

### 1. Expression Evaluation

Evaluate arithmetic expressions using calculator buttons only, e.g., `10+5-2*2/1`.

### 2. Perfect Square Check

Determine if a number is a perfect square using the calculator's square root function.

### 3. Prime Number Check

Check if a number is prime by simulating trial division through calculator operations only.

### 4. Prime Factorization

Extract prime factors of a number by repeatedly dividing using the calculator, storing valid divisors.

---

## 🚀 How to Run

1. Install required packages:

```bash
pip install selenium
```

2. Make sure [ChromeDriver](https://sites.google.com/chromium.org/driver/) is installed and its path is set correctly.

3. Run the test file:

```bash
python calculator_test.py
```

---

## 📄 Sample Output

```
Question 1 - Result of '10+5-2*2/1': 26
Question 2 - 49 is a perfect square
Question 2 - 50 is not a perfect square
Question 3 - 29 is a prime number
Question 3 - 30 is not a prime number
Question 4 - Prime factors of 84: [2, 2, 3, 7]
Question 4 - Prime factors of 60: [2, 2, 3, 5]
```

---

## 📌 Notes

* The project uses `time.sleep()` to allow the calculator time to update. This can be improved by using explicit waits (`WebDriverWait`).
* Button identification relies on specific attributes (e.g., `value`, `name`). Any change to the calculator UI may require updates.

---

## 👤 Author - Snir Oded

Developed using Selenium and Python.

Feel free to contribute or suggest improvements!
