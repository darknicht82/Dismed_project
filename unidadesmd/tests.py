from django.test import TestCase
from .models import UnidadMedica
from django.urls import reverse


class UnidadMedicaViewTest(TestCase):
    def test_mostrar_unidadesmd_view(self):
        # Aquí puedes crear algunas unidades médicas de prueba si lo necesitas
        response = self.client.get(reverse("mostrar_unidadesmd"))
        self.assertEqual(response.status_code, 200)

    def test_mostrar_unidadmd_view(self):
        # Crear una unidad médica de prueba
        unidad = UnidadMedica.objects.create(nombre_unidad="Test Unidad Médica")
        response = self.client.get(reverse("mostrar_unidadmd", args=[unidad.idudm]))
        self.assertEqual(response.status_code, 200)
