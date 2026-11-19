import pytest

from pages.frames_page import FramesPage


@pytest.fixture()
def frames_page(browser):
    return FramesPage(browser, "http://the-internet.herokuapp.com")


def test_frames(frames_page):
    frames_page.open("/iframe")

    # Переключаемся внутрь iFrame
    frames_page.switch_to_iframe()

    # Проверяем текст внутри фрейма
    assert frames_page.get_frame_text() == "Your content goes here.", (
        f"Текст во фрейме не совпал: '{frames_page.get_frame_text()}'"
    )

    # Возвращаемся к основному документу
    frames_page.switch_to_default_content()
