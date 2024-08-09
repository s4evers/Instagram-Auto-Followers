from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

def generate_random_string(length=12):
    "Сгенерировать случайную строку букв и цифр."
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_email():
    "Создайте случайный адрес электронной почты."
    return f"{generate_random_string(10)}@{generate_random_string(5)}.com"

def generate_random_login():
    "Сгенерируйте случайное имя для входа."
    return generate_random_string(16)

def run_script():
    chrome_options = Options()
    chrome_options.add_extension("buster.crx") 
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://smmpanel.com/signup")
        time.sleep(2)

        # Генерация случайных данных
        random_login = generate_random_login()
        random_email = generate_random_email()

        # Ввод данных
        login_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'login'))
        )
        login_input.send_keys(random_login)
        time.sleep(2)

        email_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        )
        email_input.send_keys(random_email)
        time.sleep(1)

        first_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'first_name'))
        )
        first_name_input.send_keys('myseleniumtest')
        time.sleep(2)

        last_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'last_name'))
        )
        last_name_input.send_keys('seleniumtest')
        time.sleep(1)

        whatsapp_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'whatsapp'))
        )
        whatsapp_input.send_keys('myseleniumtest')
        time.sleep(2)

        skype_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'skype'))
        )
        skype_input.send_keys('myseleniumtest')
        time.sleep(1)

        telegram_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'telegram'))
        )
        telegram_input.send_keys('seleniumtest')
        time.sleep(2)

        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )
        password_input.send_keys('qwertyuiop')
        time.sleep(1)

        retry_password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'password_again'))
        )
        retry_password_input.send_keys('qwertyuiop')
        time.sleep(2)

        # Прокрутка страницы вниз на 500 пикселей
        driver.execute_script("window.scrollBy(0, 500);")

        # Переключение на iframe
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']"))
        )
        driver.switch_to.frame(iframe)

        # Выбор и клик на reCAPTCHA checkbox
        re_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'recaptcha-checkbox-border'))
        )
        re_button.click()
        time.sleep(2)

        # Переключение обратно из iframe
        driver.switch_to.default_content()

        # Проверка наличия CAPTCHA challenge
        try:
            iframe_challenge = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]'))
            )
            driver.switch_to.frame(iframe_challenge)
            time.sleep(3)

            # Нажмите на кнопку расширения Buster
            buster_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]'))
            )
            buster_button.click()
            time.sleep(5)

            # Переключение обратно из iframe
            driver.switch_to.default_content()

        except Exception as e:
            # Если CAPTCHA не требуется, продолжайте выполнение скрипта
            print("CAPTCHA не требуется или произошла ошибка при работе с CAPTCHA:", e)
            driver.switch_to.default_content()

        # Нажатие кнопки отправки
        terms_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='RegistrationForm[termsofservice]']"))
        )
        terms_checkbox.click()

        time.sleep(1)

        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign up']"))
        )
        sign_up_button.click()

        time.sleep(1)

        # Найдите элемент <select> по его селектору
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@id='orderform-category']"))
        )

        # Создайте объект Select и выберите опцию по значению
        select = Select(select_element)
        select.select_by_value('20379')

        link_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'field-orderform-fields-link'))
        )
        link_input.send_keys('https://instagram.com/cs.mer6/')
        time.sleep(1)

        quality_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'field-orderform-fields-quantity'))
        )
        quality_input.send_keys('49')
        time.sleep(1)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

        time.sleep(2)
        print("Скрипт выполнен успешно!")

    except Exception as ex:
        print("Произошла ошибка:", ex)

    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    num_retries = int(input("Введите количество повторений: "))

    while num_retries > 0:
        run_script()
        num_retries -= 1
        print(f"Осталось повторений: {num_retries}")
        time.sleep(5)  # Пауза между попытками, при необходимости
