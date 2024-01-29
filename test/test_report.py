import os
from report import Report  # Asegúrate de importar correctamente tu clase
import pytest


class TestReport:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Código de configuración (opcional)
        yield
        # Elimina la carpeta devices después de cada test si existe
        if os.path.exists("devices/"):
            os.rmdir("devices/")

    def test_verify_devices_exists(self):
        # Preparar el entorno
        os.makedirs("devices/", exist_ok=True)

        report = Report()
        assert report.verify_devices() is True, "Debería retornar True si la carpeta devices existe"

    def test_verify_devices_not_exists(self):
        report = Report()
        assert report.verify_devices() is False, "Debería retornar False si la carpeta devices no existe"