import unittest 
import Nodo
class TestPolinomio(unittest.TestCase):

    def setUp(self):
        self.p1 = Nodo.Polinomio()
        Nodo.Polinomio.agregar_termino(self.p1, 1, 5)
        Nodo.Polinomio.agregar_termino(self.p1, 2, 2)
        self.p2 = Nodo.Polinomio()
        Nodo.Polinomio.agregar_termino(self.p2, 1, 4)
        Nodo.Polinomio.agregar_termino(self.p2, 3, 6)
        self.p3 = Nodo.Polinomio()

    def test_agregar_termino(self):
        Nodo.Polinomio.agregar_termino(self.p3, 3, -1)
        Nodo.Polinomio.agregar_termino(self.p3, 2, 2)
        Nodo.Polinomio.agregar_termino(self.p3, 1, 4)
        self.assertEqual(Nodo.Polinomio.mostrar(self.p3), "-1x^3+2x^2+4x^1")

    def test_modificar_termino(self):
        Nodo.Polinomio.modificar_termino(self.p1, 1, 7)
        self.assertEqual(Nodo.Polinomio.mostrar(self.p1), "+2x^2+7x^1")

    def test_obtener_valor(self):
        self.assertEqual(Nodo.Polinomio.obtener_valor(self.p2, 1), 4)
        self.assertEqual(Nodo.Polinomio.obtener_valor(self.p2, 3), 6)

    def test_eliminar_termino(self):
        Nodo.Polinomio.eliminar_termino(self.p1, 1)
        self.assertEqual(Nodo.Polinomio.mostrar(self.p1), "+2x^2")

    def test_existe_termino(self):
        self.assertTrue(Nodo.Polinomio.existe_termino(self.p1, 1))
        self.assertFalse(Nodo.Polinomio.existe_termino(self.p2, 2))

    def test_sumar(self):
        p4 = Nodo.Polinomio.sumar(self.p1, self.p2)
        self.assertEqual(Nodo.Polinomio.mostrar(p4), "+6x^3+2x^2+9x^1")

    def test_restar(self):
        p5 = Nodo.Polinomio.restar(self.p1, self.p2)
        self.assertEqual(Nodo.Polinomio.mostrar(p5), "-6x^3+2x^2+1x^1")

if __name__ == '__main__':
    unittest.main()