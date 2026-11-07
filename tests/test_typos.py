# Тест со skipif
import os

import pytest

from conftest import BASE_URL
from pages.typos_page import TyposPage, KNOWN_VARIANTS

RUN_TYPOS_LOOP = os.getenv("RUN_TYPOS_LOOP", "1") == "1"


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_paragraph_matches_known_variant(browser):
    """Текст параграфа при каждой загрузке — один из двух известных вариантов."""
    page = TyposPage(browser, BASE_URL)
    page.open(page.PATH)

    text = page.paragraph_text()
    assert text in KNOWN_VARIANTS, f"Неизвестный текст: {text!r}"


@pytest.mark.advanced
@pytest.mark.skipif(not RUN_TYPOS_LOOP,
                    reason="пропускается, если задана RUN_TYPOS_LOOP=0")
def test_both_variants_occur_on_reload(browser):
    # ловлю оба варианта текст (с\без опечатки)
    page = TyposPage(browser, BASE_URL)
    seen = set()
    for _ in range(10):
        page.open(page.PATH)
        seen.add(page.paragraph_text())
        if len(seen) == len(KNOWN_VARIANTS):
            break

    assert seen == set(KNOWN_VARIANTS)
