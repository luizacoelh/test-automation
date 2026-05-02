from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
