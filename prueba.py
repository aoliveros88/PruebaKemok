from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import sqlite3


def setUp():
        driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
        options = webdriver.ChromeOptions() 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service('C:\dchrome\chromedriver.exe&#39;')
        driver = webdriver.Chrome(service=service, options=options)
        test_buscar(driver)

def test_buscar(driver):
        driver.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
        time.sleep(5)
        productos = driver.find_elements('xpath','//div[@class="col-sm-4 col-lg-4 col-md-4"]')
       
        listaProductos =[]
        for producto  in productos:
             list=[]
             nombre = producto.find_element('xpath','.//a[@class="title"]').text
             print(nombre)
             list.append(nombre)
             detalle = producto.find_element('xpath','.//p[@class="description"]').text
             print(detalle)
             list.append(detalle)
             precio = producto.find_element('xpath','.//h4[@class="pull-right price"]').text
             print(precio)
             list.append(precio)
             review = producto.find_element('xpath','.//p[@class="pull-right"]').text
             review_number = review[0]
             print(review_number)
             list.append(review_number)
             print(list)
             listaProductos.append(list)

        print('Lista de productos', listaProductos)

        #test_insertTable(listaProductos)
        
        #wait = WebDriverWait(webdriver, 5)
        #element = WebDriverWait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pagination a[rel=next]')))

def test_crear_tabla():
              mi_conexion = sqlite3.connect("mydatabase.db")
              cursor = mi_conexion.cursor()
              cursor.execute(
                 """CREATE TABLE productos (
                     ID INTEGER primary key AUTOINCREMENT, 
                     NOMBRE VARCHAR2(20), 
                     DETALLE VARCHAR(20),
                     PRECIO VARCHAR(10),
                     top_review bool
                 )"""
                )
              mi_conexion.commit()
              mi_conexion.close()


def test_insertTable(listaProductos):
            mi_conexion = sqlite3.connect("mydatabase.db")
            cursor = mi_conexion.cursor()
            instruccion = f"INSERT INTO productos VALUES(NULL,?,?,?,?)"
            cursor.executemany(instruccion, listaProductos )
            mi_conexion.commit()
            mi_conexion.close()


if __name__ == "__main__":
     setUp()
