import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime
import os


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_consulta_sisben(browser):
    page = browser

    page.goto("https://www.sisben.gov.co/Paginas/landing.html")
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(3000)

    page.locator("a[href='consulta-tu-grupo.html']").first.click()
    page.wait_for_load_state("networkidle", timeout=20000)
    page.wait_for_timeout(3000)

    page.evaluate("window.scrollBy(0, 1500)")
    page.wait_for_timeout(1000)

    # Localizar el frame correcto
    target_frame = None
    for frame in page.frames:
        try:
            select = frame.locator("#TipoID")
            select.wait_for(state="visible", timeout=3000)
            if select.count() > 0:
                target_frame = frame
                break
        except Exception:
            continue

    if target_frame is None:
        raise Exception("No se encontró #TipoID en ningún frame")

    # Seleccionar tipo de documento
    target_frame.locator("#TipoID").select_option(value="3")
    target_frame.wait_for_timeout(2000)

    # Input número documento
    target_frame.locator("#documento").wait_for(state="visible", timeout=10000)
    target_frame.locator("#documento").fill("1000100100") # Cambiar por un documento de identidad válido
    target_frame.wait_for_timeout(500)

    # Botón [Consultar]
    target_frame.locator("#botonenvio").click()

    target_frame.wait_for_timeout(500)

    # Evidencia
    os.makedirs("evidencias", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"evidencias/consulta_{timestamp}.png", full_page=True)