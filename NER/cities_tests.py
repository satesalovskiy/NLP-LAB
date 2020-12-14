import unittest
import MyNER

class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = MyNER.MyNER()
    
    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))
        
    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('липецк', 'город'))

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('сургут', None))

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('липецк', 'город'))

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))

    def test_6(self):
        testing_address = 'сургут югорская 30/2'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('сургут', None))

    def test_7(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))

    def test_8(self):
        testing_address = 'ты сургут улица 30 лет победы'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('сургут', None))

    def test_9(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('нальчик', 'город'))

    def test_10(self):
        testing_address = 'null'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))

    def test_11(self):
        testing_address = '60 мегабит я'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))

    def test_12(self):
        testing_address = 'сургут крылова 53/4'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('сургут', None))

    def test_13(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, ('москва', None))

    def test_14(self):
        testing_address = 'мое 3 парковая'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))

    def test_15(self):
        testing_address = 'Пришвина 17'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))

    def test_16(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res = self.NERInstance.nerCities(testing_address)
        self.assertEqual(res, (None, None))

if __name__ == '__main__':
    unittest.main()
    
    