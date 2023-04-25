from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexLocators:
    locator_search_field = (By.ID, "text")
    locator_search_button = (By.CLASS_NAME, "mini-suggest__popup-content")
    locator_first_link = (By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/a')
    locator_search_result = (By.ID, "search-result")
    more_button = (By.CLASS_NAME, "services-suggest__icons-more")
    image_icon_css = "body > div.popup2.services-more-popup.services-more-popup_pinnable_yes." \
                     "services-more-popup_suggest_yes.popup2_theme_normal.popup2_autoclosable_" \
                     "yes.popup2_services-more_yes.popup2_view_classic.i-bem.popup2_js_inited." \
                     "services-more-popup_js_inited.popup2_visible_yes > div > div > div.scrollbar__scrollable " \
                     "> div > div.services-more-popup__section.services-more-popup__section-all > " \
                     "div.services-more-popup__section-content > span:nth-child(9) > a"
    locator_image_icon = (By.CSS_SELECTOR, image_icon_css)
    locator_image_first_category = (By.XPATH, '//div[contains(@class,"page-layout")]/descendant::div[contains(@class,"PopularRequestList-Item PopularRequestList-Item_pos_0")]')
    locator_image_search_field = (By.XPATH, '//input[@class="input__control mini-suggest__input"]')
    locator_first_image = (By.CSS_SELECTOR, '.serp-item__preview')
    locator_image_true = (By.CSS_SELECTOR, '.MMImage-Origin')
    locator_image_true_css = '.MMImage-Origin'
    next_button = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button')
    previous_button = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button')


class Search(BasePage):

    def enter_words(self, element, words):
        search_field = self.find_element(element)
        search_field.click()
        search_field.send_keys(words)
        return search_field

    def check_first_link(self):
        element = self.find_element(YandexLocators.locator_first_link)
        link = element.get_attribute("href")
        return link

    def press_enter(self):
        search_field = self.find_element(YandexLocators.locator_search_field)
        search_field.send_keys(Keys.ENTER)

    def click_to_button(self, button):
        more_button = self.find_element(button)
        more_button.click()

    def get_attribute(self, element, att):
        elem = self.find_element(element)
        return elem.get_attribute(att)

    def get_the_value(self, locator):
        search_field_name = self.find_element(locator)
        return search_field_name.get_attribute("value")

    def category_name(self, locator):
        category = self.find_element(locator)
        return category.text

    def open_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])


