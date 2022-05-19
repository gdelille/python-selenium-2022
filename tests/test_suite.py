# class TestSuite:
#     @classmethod
#     def setup_class(cls):
#         print('Se ejecuta una sola vez al inicio')

#     def setup_method(self):
#         print('Se ejecuta antes de cada test case')
      
#     def test_first(self):
#         print('Primer test')

#     def test_second(self):
#         print('Segundo test')
    
#     def test_third(self):
#         print('Tercer test')
    
#     def do_something(self):
#         pass


##############################################

# import pytest


# class TestSuite:
#     @classmethod
#     def setup_class(cls):
#         print("SE EJECUTA UNA SOLA VEZ AL INICIO")

#     def setup_method(self):
#         print("SE EJECUTA ANTES DE CADA TEST CASE")

#     def test_first(self):
#         print("TEST FIRST")

#     def test_second(self):
#         print("TEST SECOND")

#     def test_third(self):
#         print("TEST THIRD")
#         assert 5 == 3

#     def do_something(self):
#         pass

#     def teardown_method(selfs):
#         print("SE EJECUTA AL FINAL DE CADA TEST CASE")

#     @classmethod
#     def teardown_class(cls):
#         print("SE EJECUTA UNA SOLA VEZ AL FINAL")

#################################

import pytest


class TestSuite:
    @classmethod
    def setup_class(cls):
        print("SE EJECUTA UNA SOLA VEZ AL INICIO")

    def setup_method(self):
        print("SE EJECUTA ANTES DE CADA TEST CASE")

    @pytest.mark.smoke
    def test_first(self):
        print("TEST FIRST")

    @pytest.mark.regression
    def test_second(self):
        print("TEST SECOND")

    @pytest.mark.touch
    def test_third(self):
        print("TEST THIRD")

    def do_something(self):
        pass

    def teardown_method(selfs):
        print("SE EJECUTA AL FINAL DE CADA TEST CASE")

    @classmethod
    def teardown_class(cls):
        print("SE EJECUTA UNA SOLA VEZ AL FINAL")








