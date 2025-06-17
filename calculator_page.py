'''🧱 Project structure according to Page Object Model
calculator_project/
│
├── calculator_test.py         # Main test execution file
├── calculator_page.py         # Class representing the calculator page
└── utils.py                   # Helper functions (perfect square, prime, prime factors)
'''

from selenium.webdriver.common.by import By  # For locating elements
import time  # Used for simple sleep (could be improved)

from selenium.webdriver.support.ui import WebDriverWait  # Explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.theonlinecalculator.com/")  # Open the calculator page
        # Create a WebDriverWait object to wait up to 10 seconds for a condition
        self.wait = WebDriverWait(self.driver, 10)
        # Wait until the calculator element is present on the page before continuing
        self.wait.until(EC.presence_of_element_located((By.ID, "calculator")))

    def click_button(self, value):
        try:
            # Try to find the button on the page by its value attribute
            button = self.driver.find_element(By.XPATH, f"//input[@value='{value}']")
        except:
            # If the button is not found, check if it's a clear button which can have different values
            if value in ["AC", "CE"]:
                # Find clear button by its name attribute if value-based search failed
                button = self.driver.find_element(By.NAME, "clearButton")
            else:
                # Re-raise the exception if it's another button that was not found
                raise
        button.click()  # Click the button

    def clear(self):
        # Click the "AC" button to clear the calculator before starting new calculation
        self.click_button("AC")

    def calculate_expression(self, expression):
        self.clear()  # Clear calculator before calculation
        for char in expression:
            # Map characters in expression to corresponding calculator buttons
            if char == '*':
                self.click_button("×")  # Multiplication button on calculator
            elif char == '/':
                self.click_button("÷")  # Division button
            elif char == '-':
                # Use the en dash '−' (unicode) because that's what calculator uses, not regular minus '-'
                self.click_button("−")
            elif char == '+':
                self.click_button("+")
            else:
                self.click_button(char)  # For digits and decimal point
        self.click_button("=")  # Press equals to get result
        time.sleep(1)  # Wait for result to appear (could be improved with explicit wait)
        return self.get_result()  # Return the displayed result

    def get_result(self):
        # Find the display element by ID and get its current value (result of calculation)
        display = self.driver.find_element(By.ID, "display")
        return display.get_attribute("value")
