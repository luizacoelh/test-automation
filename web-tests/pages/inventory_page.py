from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def add_product_to_cart(self, index=0):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
        buttons[index].click()

    def get_cart_count(self):
        badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(badge[0].text) if badge else 0

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
