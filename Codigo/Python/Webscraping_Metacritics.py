#Parte de webscraping

# Importacion de Librerias
import time
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Definimos la función
def loging():
    # Creamos una variable para Cargar e instalar los drivers
    driver = EdgeChromiumDriverManager().install()
    edge_service = Service(driver)
    edge_opc = Options()
    edge_opc.add_argument("--window-size=1020,1200")
    # edge_opc.add_argument("--headless")  # Agregar opción para ejecutar en modo headless
    # edge_opc.add_argument("--disable-gpu")  # Desactivar uso de GPU
    # edge_opc.add_argument("--no-sandbox")  # Desactivar sandboxing
    # edge_opc.add_argument("--disable-dev-shm-usage")
    navegador = webdriver.Edge(service=edge_service, options=edge_opc)
    # Pantalla completa del navegador
    navegador.maximize_window()
    # Limitamos las acciones del bot para que parezca lo más humano posible o eficiente
    wait = WebDriverWait(navegador, 10)

    datos = {
        # tabla 1 abajo
        "Nombre": [],
        "Fecha Lanzamiento": [],
        "Meta Score": [],
        "Catalogado por Meta": [],
        "User Score": [],
        "Catalogado por Usuario": [],
        # tabla 2 abajo
        "Plataforma": [],
        "Desarrollador": [],
        "Publicado por": [],
        "Genero": []
    }
    base_url = "https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2024&page="

    # Bucle de Paginas
    for page in range(1, 3):
        # Actualiza la pagina conforme al range añadiendole el numero final de la pagina
        pagina_actual = (base_url + str(page))

        navegador.get(pagina_actual)
        wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "c-finderProductCard")))
        # Soup Principal
        soup_main = BeautifulSoup(navegador.page_source, "html.parser")

        # 1.er ciclo FOR de los Primeros 12 registros
        tabla_main = soup_main.find("div", attrs={"class": "c-productListings"})
        elemento_main = tabla_main.find_all("div", attrs={"class": "c-finderProductCard c-finderProductCard-game"})
        conteo = 1

        # 2do ciclo FOR de los ultimos 12 registros
        tabla_main2 = soup_main.find("div", attrs={
            "class": "c-productListings_grid g-grid-container u-grid-columns g-inner-spacing-bottom-large g-inner-spacing-top-large"})  # Obtén el segundo div con la clase "c-productListings"
        elemento_main2 = tabla_main2.find_all("div", attrs={"class": "c-finderProductCard c-finderProductCard-game"})
        conteo2 = 1
        # Primer ciclo de los primeros 12 registros
        for _ in elemento_main[:12]:
            juego = navegador.find_element(By.XPATH,
                                           '//*[@id="__layout"]/div/div[2]/div[1]/main/section/div[3]/div[1]/div[' + str(
                                               conteo) + ']/a')
            juego.click()
            conteo += 1
            time.sleep(2)
            soup1 = BeautifulSoup(navegador.page_source, "html.parser")
            tabla1 = soup1.find("div",
                                attrs={"class": "c-productHero_score-container u-flexbox u-flexbox-column g-bg-white"})
            time.sleep(2)
            nombre = WebDriverWait(navegador, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "div.c-productHero_title"))).text
            # nombre = tabla1.find("div", attrs={"class": "c-productHero_title g-inner-spacing-bottom-medium g-outer-spacing-top-medium"}).text
            time.sleep(2)
            fecha = tabla1.find("span", attrs={"class": "u-text-uppercase"}).text
            datos["Nombre"].append(nombre)
            datos["Fecha Lanzamiento"].append(fecha)

            # meta
            meta = tabla1.find("div", attrs={"class": "c-productScoreInfo_scoreContent"})
            meta_score = meta.find("div", attrs={"class": "c-siteReviewScore"}).text
            meta_catalogado = meta.find("span", attrs={"class": "c-productScoreInfo_scoreSentiment"}).text.strip()
            datos["Meta Score"].append(meta_score)
            datos["Catalogado por Meta"].append(meta_catalogado)
            time.sleep(2)
            tabla_user_score = tabla1.find("div", attrs={
                "class": "c-siteReviewScore_background c-siteReviewScore_background-user"})
            user_score = tabla_user_score.find("div", attrs={'class': 'c-siteReviewScore'}).text
            time.sleep(2)
            tabla_user_catalogado = tabla1.find("div", attrs={"class": "c-productScoreInfo u-clearfix"})
            user_catalogado = tabla_user_catalogado.find("span", attrs={
                "class": "c-productScoreInfo_scoreSentiment"}).text.strip()
            datos["User Score"].append(user_score)
            datos["Catalogado por Usuario"].append(user_catalogado)
            time.sleep(4)
            tabla_detalles = navegador.find_element(By.XPATH,
                                                    '//*[@id="__layout"]/div/div[2]/div[1]/div[6]/div/div/div[1]/a[2]')
            tabla_detalles.click()

            soup2 = BeautifulSoup(navegador.page_source, "html.parser")
            tabla2 = soup2.find("div", attrs={"class": "c-gameDetails_sectionContainer u-flexbox u-flexbox-column"})

            plataforma = tabla2.find("div", attrs={"class": "c-gameDetails_Platforms u-flexbox u-flexbox-row"}).find(
                "li", attrs={"class": "c-gameDetails_listItem g-color-gray70 u-inline-block"}).text.strip()
            desarrollador = soup2.find("div", attrs={"class": "c-gameDetails_Developer u-flexbox u-flexbox-row"}).find(
                "li", attrs={"class": "c-gameDetails_listItem g-color-gray70 u-inline-block"}).text.strip()
            publicado = soup2.find("div", attrs={"class": "c-gameDetails_Distributor u-flexbox u-flexbox-row"}).find(
                "span", attrs={"class": "g-outer-spacing-left-medium-fluid g-color-gray70 u-block"}).text.strip()
            genero = soup2.find("li", attrs={"class": "c-genreList_item"}).text.strip()

            datos["Plataforma"].append(plataforma)
            datos["Desarrollador"].append(desarrollador)
            datos["Publicado por"].append(publicado)
            datos["Genero"].append(genero)

            navegador.get(pagina_actual)
            wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "c-finderProductCard")))
            # time.sleep(4)

        # Segundo ciclo de los ultimos 12 registros
        for _ in elemento_main2[:12]:
            juego = navegador.find_element(By.XPATH,
                                           '//*[@id="__layout"]/div/div[2]/div[1]/main/section/div[3]/div[3]/div[' + str(
                                               conteo2) + ']/a')
            juego.click()
            conteo2 += 1
            time.sleep(2)
            soup_2 = BeautifulSoup(navegador.page_source, "html.parser")
            tabla11 = soup_2.find("div", attrs={
                "class": "c-productHero_score-container u-flexbox u-flexbox-column g-bg-white"})
            time.sleep(2)
            nombre = WebDriverWait(navegador, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "div.c-productHero_title"))).text
            # nombre = tabla1.find("div", attrs={"class": "c-productHero_title g-inner-spacing-bottom-medium g-outer-spacing-top-medium"}).text
            time.sleep(4)
            fecha = tabla11.find("span", attrs={"class": "u-text-uppercase"}).text
            datos["Nombre"].append(nombre)
            datos["Fecha Lanzamiento"].append(fecha)
            time.sleep(2)
            # meta
            meta = tabla11.find("div", attrs={"class": "c-productScoreInfo_scoreContent"})
            meta_score = meta.find("div", attrs={"class": "c-siteReviewScore"}).text
            meta_catalogado = meta.find("span", attrs={"class": "c-productScoreInfo_scoreSentiment"}).text.strip()
            datos["Meta Score"].append(meta_score)
            datos["Catalogado por Meta"].append(meta_catalogado)
            time.sleep(2)
            tabla_user_score = tabla11.find("div", attrs={
                "class": "c-siteReviewScore_background c-siteReviewScore_background-user"})
            user_score = tabla_user_score.find("div", attrs={"class": "c-siteReviewScore"}).text
            time.sleep(2)
            tabla_user_catalogado = tabla11.find("div", attrs={"class": "c-productScoreInfo u-clearfix"})
            user_catalogado = tabla_user_catalogado.find("span", attrs={
                "class": "c-productScoreInfo_scoreSentiment"}).text.strip()
            datos["User Score"].append(user_score)
            datos["Catalogado por Usuario"].append(user_catalogado)
            time.sleep(4)
            tabla_detalles = navegador.find_element(By.XPATH,
                                                    '//*[@id="__layout"]/div/div[2]/div[1]/div[6]/div/div/div[1]/a[2]')
            tabla_detalles.click()
            soup22 = BeautifulSoup(navegador.page_source, "html.parser")
            tabla22 = soup22.find("div", attrs={"class": "c-gameDetails_sectionContainer u-flexbox u-flexbox-column"})

            plataforma = tabla22.find("div", attrs={"class": "c-gameDetails_Platforms u-flexbox u-flexbox-row"}).find(
                "li", attrs={"class": "c-gameDetails_listItem"}).text.strip()
            desarrollador = soup22.find("div", attrs={"class": "c-gameDetails_Developer u-flexbox u-flexbox-row"}).find(
                "li", attrs={"class": "c-gameDetails_listItem"}).text.strip()
            publicado = soup22.find("div", attrs={"class": "c-gameDetails_Distributor u-flexbox u-flexbox-row"}).find(
                "span", attrs={"class": "g-outer-spacing-left-medium-fluid"}).text.strip()
            genero = soup22.find("li", attrs={"class": "c-genreList_item"}).text.strip()

            datos["Plataforma"].append(plataforma)
            datos["Desarrollador"].append(desarrollador)
            datos["Publicado por"].append(publicado)
            datos["Genero"].append(genero)

            navegador.get(pagina_actual)
            wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "c-finderProductCard")))

    df = pd.DataFrame(datos)
    df.index = df.index + 1
    df.to_csv("C:\Users\52664\Downloads\Proyecto_final\datasets.csv")
