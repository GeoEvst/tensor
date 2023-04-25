import time
import pytest
from selenium.webdriver.common.keys import Keys

from YaPages import Search, YandexLocators


def test_yandex_search_task_1(browser):
    """Открывает страницу, проверяет наличие поля поиска"""
    global yandex_main_page

    yandex_main_page = Search(browser)
    yandex_main_page.open_site()
    assert yandex_main_page.check_element_id("text") is True


def test_check_search_field_task_1(browser):
    """Вводит текст в строку поиска, проверяет наличие подсказок (suggest)"""

    yandex_main_page.enter_words(YandexLocators.locator_search_field, "Тензор")
    assert yandex_main_page.check_element_class_name("mini-suggest__popup-content") is True
    yandex_main_page.press_enter()
    return yandex_main_page


def test_check_search_result_task_1(browser):
    """Проверка наличия страницы поиска."""
    assert yandex_main_page.check_element_id("search-result") is True


def test_check_first_link_task_1(browser):
    """Проверка, что первая ссылка ведет на tensor.ru"""
    assert yandex_main_page.check_first_link() == 'https://tensor.ru/'


def test_check_menu_button_task_2(browser):
    """Проверка наличия кнопки меню"""
    global yandex_im_page

    yandex_im_page = Search(browser)
    yandex_im_page.open_site()
    yandex_im_page.click_to_button(YandexLocators.locator_search_field)
    yandex_im_page.click_to_button(YandexLocators.more_button)
    assert yandex_im_page.check_element_css(YandexLocators.image_icon_css) is True


def test_check_moves_to_image_task_2(browser):
    """Проверка перехода на картинки"""
    yandex_im_page.click_to_button(YandexLocators.locator_image_icon)
    yandex_im_page.open_new_window()
    url = yandex_im_page.return_url()
    assert url == 'https://yandex.ru/images/'


def test_check_first_category_task_2(browser):
    """Проверка наименования категории"""
    yandex_im_page.find_element(YandexLocators.locator_image_first_category)
    yandex_im_page.click_to_button(YandexLocators.locator_image_first_category)
    search_field_name = yandex_im_page.get_the_value(YandexLocators.locator_image_search_field)
    category_name = yandex_im_page.category_name(YandexLocators.locator_image_first_category)
    assert category_name == search_field_name


def test_check_open_image_task_2(browser):
    """Проверка открытия картинки"""
    yandex_im_page.click_to_button(YandexLocators.locator_first_image)
    time.sleep(0.1)
    assert yandex_im_page.check_element_css(YandexLocators.locator_image_true_css) is True


def test_another_image_task_2(browser):
    """Проверяем что картинка переключилась"""
    global first_image

    first_image = yandex_im_page.get_attribute(YandexLocators.locator_image_true, 'src')
    yandex_im_page.click_to_button(YandexLocators.next_button)
    next_image = yandex_im_page.get_attribute(YandexLocators.locator_image_true, 'src')
    assert first_image != next_image


def test_check_first_image_task_2(browser):
    """Проверяем что картинка переключилась обратно"""
    yandex_im_page.click_to_button(YandexLocators.previous_button)
    time.sleep(0.1)
    current_image = yandex_im_page.get_attribute(YandexLocators.locator_image_true, 'src')
    time.sleep(0.1)
    assert current_image == first_image


# def test_task_1(browser):
#     """Проверка поисковой выдачи"""
#
#     yandex_main_page = Search(browser)
#     yandex_main_page.open_site()
#     assert yandex_main_page.check_element_id("text") is True
#
#     yandex_main_page.enter_words(YandexLocators.locator_search_field, "Тензор")
#     assert yandex_main_page.check_element_class_name("mini-suggest__popup-content") is True
#
#     yandex_main_page.press_enter()
#     assert yandex_main_page.check_element_id("search-result") is True
#
#     assert yandex_main_page.check_first_link() == 'https://tensor.ru/'
#
#
# def test_task_2(browser):
#     """Проверка картинок"""
#
#     yandex_im_page = Search(browser)
#     yandex_im_page.open_site()
#     yandex_im_page.click_to_button(YandexLocators.locator_search_field)
#     yandex_im_page.click_to_button(YandexLocators.more_button)
#     assert yandex_im_page.check_element_css(YandexLocators.image_icon_css) is True
#
#     yandex_im_page.click_to_button(YandexLocators.locator_image_icon)
#     yandex_im_page.open_new_window()
#     url = yandex_im_page.return_url()
#     assert url == 'https://yandex.ru/images/'
#
#     yandex_im_page.find_element(YandexLocators.locator_image_first_category)
#     yandex_im_page.click_to_button(YandexLocators.locator_image_first_category)
#     search_field_name = yandex_im_page.get_the_value(YandexLocators.locator_image_search_field)
#     category_name = yandex_im_page.category_name(YandexLocators.locator_image_first_category)
#     assert category_name == search_field_name
#
#     yandex_im_page.click_to_button(YandexLocators.locator_first_image)
#     time.sleep(0.1)
#     assert yandex_im_page.check_element_css(YandexLocators.locator_image_true_css) is True
#
#     first_image = yandex_im_page.get_attribute(YandexLocators.locator_image_true, 'src')
#     yandex_im_page.click_to_button(YandexLocators.next_button)
#     next_image = yandex_im_page.get_attribute(YandexLocators.locator_image_true, 'src')
#     assert first_image != next_image
#
#     yandex_im_page.click_to_button(YandexLocators.previous_button)
#     time.sleep(0.1)
#     current_image = yandex_im_page.get_attribute(YandexLocators.locator_image_true, 'src')
#     time.sleep(0.1)
#     assert current_image == first_image
