from django.test import TestCase
from django.urls import reverse

from .models import Objeto


class ObjetoViewTests(TestCase):
    def setUp(self):
        self.objeto = Objeto.objects.create(
            nombre='Paraguas',
            descripcion='Paraguas negro',
            entregado=False,
        )

    def test_editar_objeto_muestra_formulario(self):
        response = self.client.get(reverse('editar_objeto', args=[self.objeto.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Editar Objeto')
        self.assertContains(response, 'Paraguas negro')

    def test_editar_objeto_guarda_cambios(self):
        response = self.client.post(
            reverse('editar_objeto', args=[self.objeto.id]),
            {
                'nombre': 'Paraguas azul',
                'descripcion': 'Actualizado',
                'entregado': 'on',
            },
        )

        self.assertRedirects(response, reverse('listar_objetos'))
        self.objeto.refresh_from_db()
        self.assertEqual(self.objeto.nombre, 'Paraguas azul')
        self.assertTrue(self.objeto.entregado)

    def test_eliminar_objeto_muestra_confirmacion_y_elimina(self):
        url = reverse('eliminar_objeto', args=[self.objeto.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '¿Está seguro')

        response = self.client.post(url)
        self.assertRedirects(response, reverse('listar_objetos'))
        self.assertFalse(Objeto.objects.filter(id=self.objeto.id).exists())
