import pytest

from pages.dynamic_controls_page import DynamicControlsPage


@pytest.fixture()
def dynamic_controls_page(browser):
    return DynamicControlsPage(browser, "http://the-internet.herokuapp.com")


def test_dynamic_controls(dynamic_controls_page):
    dynamic_controls_page.open("/dynamic_controls")

    dynamic_controls_page.click_remove()
    assert dynamic_controls_page.wait_for_message() == "It's gone!", (
        "Не появилось сообщение 'It's gone!'"
    )

    # проверяем отсутствие чекбокса
    assert not dynamic_controls_page.is_checkbox_present(), (
        "Чекбокс всё ещё на странице после Remove"
    )

    # поле неактивно
    assert not dynamic_controls_page.is_input_enabled(), (
        "Поле ввода должно быть неактивным до нажатия Enable"
    )

    # Нажимаем Enable, ждём сообщение и проверяем активность
    dynamic_controls_page.click_enable()
    assert dynamic_controls_page.wait_for_message() == "It's enabled!", (
        "Не появилось сообщение 'It's enabled!'"
    )
    assert dynamic_controls_page.is_input_enabled(), (
        "Поле ввода должно стать активным после Enable"
    )
