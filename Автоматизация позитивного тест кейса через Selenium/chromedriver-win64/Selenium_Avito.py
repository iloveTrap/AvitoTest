import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
# selenium.webdriver.chrome.service import Service
import time

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def add_favorite_selenium(url):
    # Установите путь к директории, где находится chromedriver.exe
    #service = Service(executable_path='C:/Zadanie (avito)/Chromedriver-win64/chromedriver.exe')
    #В данном случае Selenium самостоятельно в проекте находит webdriver
    option = webdriver.ChromeOptions()

    # Создание экземпляра браузера с указанием пути к драйверу
    #driver = webdriver.Chrome(service=service, options=option)

    driver = webdriver.Chrome(options=option)
    try:
        # Переход на указанную страницу
        logging.info(f"Открывается страница: {url}")
        driver.get(url)

        # Ожидание полной загрузки страницы
        logging.info("Страница успешно загружена.")

        # Получение кнопки "Добавить в избранное"
        add_to_favorite_button = driver.find_element(By.CLASS_NAME, 'desktop-usq1f1')
        logging.info("Найдена кнопка 'Добавить в избранное'.")
        time.sleep(1)

        # Нажатие кнопки "Добавить в избранное"
        add_to_favorite_button.click()
        logging.info("Кнопка 'Добавить в избранное' нажата.")

        # Ожидание 3 секунд после клика
        time.sleep(3)
        logging.info("Ожидание 3 секунды после нажатия на кнопку.")

        # Вывод успешного завершения операции
        logging.info("Объявление успешно добавлено в избранное!")

    except Exception as e:
        # Обработка и вывод ошибок
        logging.error("Произошла ошибка: %s", e)

    finally:
        # Закрытие браузера и вывод сообщения в лог
        driver.quit()
        logging.info("Браузер закрыт.")


# URL объявления для добавления в избранное
add_url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"

# Вызов функции для добавления объявления в избранное
add_favorite_selenium(add_url)
