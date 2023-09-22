# Импорт необходимых модулей
import logging
from playwright.sync_api import sync_playwright

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Определение функции для добавления объявления в избранное
def add_favorite(url):
    with sync_playwright() as playwright:
        # Запуск браузера
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Получение версии Chromium и вывод в лог
        browser_version = browser.version
        logging.info(f"Используется версия Chromium: {browser_version}")

        try:
            # Переход на указанную страницу
            logging.info(f"Открывается страница: {url}")
            page.goto(url)

            # Ожидание полной загрузки страницы
            page.wait_for_load_state(state="load")
            logging.info("Страница успешно загружена.")

            # Получение кнопки "Добавить в избранное"
            add_to_favorite_selector = "button.desktop-usq1f1"
            add_to_favorite_button = page.wait_for_selector(add_to_favorite_selector, state="visible")
            logging.info("Найдена кнопка 'Добавить в избранное'.")

            # Нажатие кнопки "Добавить в избранное"
            add_to_favorite_button.click()
            logging.info("Кнопка 'Добавить в избранное' нажата.")

            # Ожидание 3 секунд после клика
            page.wait_for_timeout(3000)
            logging.info("Ожидание 3 секунды после нажатия на кнопку.")

            # Вывод успешного завершения операции
            logging.info("Объявление успешно добавлено в избранное!")

        except Exception as e:
            # Обработка и вывод ошибок
            logging.error("Произошла ошибка: %s", e)

        finally:
            # Закрытие браузера и вывод сообщения в лог
            browser.close()
            logging.info("Браузер закрыт.")


# URL объявления для добавления в избранноеv
add_url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"

# Вызов функции для добавления объявления в избранное
add_favorite(add_url)