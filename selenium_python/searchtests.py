from tkinter import Button
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID,"search")
    
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME,"q")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")
    
    """
        Verificar si el boton esta disponible
    """

    def test_search_button_enabled(self):
        button = self.driver.find_element(By.CLASS_NAME,"button")
    
    """
        lista de los elementos que encontramos
    """
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME,"promos")
        banners = banner_list.find_elements(By.TAG_NAME,'img')
        self.assertEqual(3, len(banners))
    
    """
        Permite identificar los elementos cuando algo
        no es lo sufucientemente explicito por ejemplo
        cuando no tenemos ni id ni clase
    """

    def test_vip_promo(self):
        # ruta obtenido de xpath nos indica donde se encunetra el elemento en este caso la img
        # a traves de los nodos XML en el sitio web
        vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')
    
    """
        Identificar elementos con selectores de css
    """
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)