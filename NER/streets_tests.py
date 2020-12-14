import unittest
import MyNER

class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = MyNER.MyNER()
    
    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual( ('комсомольский', 'проспект'), res)
        
    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual( ('катукова', 'улица'), res)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('рабочая', 'улица'), res)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('доватора', None), res)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('бехтеева', None), res)

    def test_6(self):
        testing_address = 'улица меркулова дом 24'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('меркулова', 'улица'), res)

    def test_7(self):
        testing_address = 'октябрьская 48 частный дом город сургут'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('октябрьская', None), res)

    def test_8(self):
        testing_address = 'сколько улица 30 лет победы 50 46'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('30 лет победы', 'улица'), res)

    def test_9(self):
        testing_address = 'тюменский тракт 10'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('тюменский', 'тракт'), res)

    def test_10(self):
        testing_address = 'сургут югорская 30/2'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('югорская', None), res)

    def test_11(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual((None, None), res)

    def test_12(self):
        testing_address = 'старый оскол микрорайон олимпийский дом 23 квартира 105'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('олимпийский', 'микрорайон'), res)

    def test_13(self):
        testing_address = 'город сургут улица фармана салманова 4'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual( ('фармана салманова', 'улица'), res)

    def test_14(self):
        testing_address = 'ты сургут улица 30 лет победы'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual( ('30 лет победы', 'улица'), res)

    def test_15(self):
        testing_address = 'проезд мунарева 2'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('мунарева', 'проезд'), res)

    def test_16(self):
        testing_address = 'домашний адрес где я живу'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual((None, None), res)

    def test_17(self):
        testing_address = 'артема 32 квартира 8'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual( ('артема', None), res)

    def test_18(self):
        testing_address = 'знаете знаете у меня дорогая девочка у меня уже все есть и менять из из одного переходить на другой я не хочу поэтому какой город квартира какой ничего я вам сообщать не хочу поэтому до свидания я ничего не'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual( (None, None), res)

    def test_19(self):
        testing_address = 'новогиреевская 34'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual( ('новогиреевская', None), res)

    def test_20(self):
        testing_address = 'мое 3 парковая'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('парковая', None), res)

    def test_21(self):
        testing_address = 'москва мусы джалиля 38 корпус 2'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('мусы джалиля', None), res)

    def test_22(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('горького', None), res)

    def test_23(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('каширское', 'шоссе'), res)

    def test_24(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('зеленые', 'аллеи'), res)

    def test_25(self):
        testing_address = 'дмитрия ульянова 17 корпус 1 москва'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('дмитрия ульянова', None), res)

    def test_26(self):
        testing_address = 'null'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual((None, None), res)

    def test_27(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('алтуфьевское', None), res)

    def test_28(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('маршала захарова', None), res)

    def test_29(self):
        testing_address = 'а зачем'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual((None, None), res)

    def test_30(self):
        testing_address = 'Кавказский 16'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('Кавказский', None), res)

    def test_31(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('Старый Гай'.lower(), None), res)

    def test_32(self):
        testing_address = 'зелинского улица зелинского дом 2'
        res = self.NERInstance.nerStreet(testing_address)
        self.assertEqual(('зелинского', 'улица'), res)

if __name__ == '__main__':
    unittest.main()
    
    