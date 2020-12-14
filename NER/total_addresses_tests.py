import unittest
import MyNER
        
class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = MyNER.MyNER()
    
    def test_one(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.totalNERaddress(testing_address)
        #print(res[2])
        #print(res[0])
        self.assertEqual( ('комсомольский', 'проспект'), res[2])
        self.assertEqual(('50', None, None), res[0])


    def test_second(self):
        testing_address = 'город липецк улица катукова 36 a'
        res = self.NERInstance.totalNERaddress(testing_address)
        self.assertEqual(('липецк', 'город'), res[1])
        self.assertEqual( ('катукова', 'улица'), res[2])
        self.assertEqual(('36a', None, None), res[0])


    def test_third(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.totalNERaddress(testing_address)
        self.assertEqual(('сургут', None), res[1])
        self.assertEqual(('рабочая', 'улица'), res[2])
        self.assertEqual(('31а', None, None), res[0])


    def test_fouth(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('липецк', 'город'), res[1])
        self.assertEqual( ('доватора', None), res[2])
        self.assertEqual( ('18', None, None), res[0])

    def test_behtereva(self):
        testing_address =  'ну бехтеева 9 квартира 310'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual( (None, None), res[1],)
        self.assertEqual(('бехтеева', None),res[2])

        self.assertEqual(('9', None, '310'),res[0])

        #self.assertEqual(('9', None, None),res[0])
        #self.assertEqual('310', res.appartment )

    def test_moskovskaya(self):
        testing_address =  'московская 34б'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual( (None, None), res[1])
        self.assertEqual( ('московская', None), res[2])
        self.assertEqual(('34б', None, None), res[0])
        #self.assertEqual(None, res.appartment)

    def test_minina(self):
        testing_address =  'улица минина дом 1'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual((None, None), res[1])
        self.assertEqual(('минина', 'улица'), res[2])
        self.assertEqual(('1', None, None), res[0])
        #self.assertEqual( None, res.appartment)

    def test_30_let_victory(self):
        testing_address =  'сколько улица 30 лет победы 50 46'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual( (None, None), res[1])
        self.assertEqual(('30 лет победы', 'улица'), res[2])
        self.assertEqual( ('50', None, '46'), res[0])

        #self.assertEqual( ('50', None, None), res[0])
        #self.assertEqual('46', res.appartment)

    def test_tract(self):
        testing_address =  'тюменский тракт 10'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual((None, None), res[1] )
        self.assertEqual(('тюменский', 'тракт'), res[2] )
        self.assertEqual(('10', None, None), res[0] )
        #self.assertEqual( None, res.appartment)

    def test_beregovaya(self):
        testing_address =  'береговая 43 береговая 43 сургут'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('сургут', None), res[1])
        self.assertEqual(('береговая', None), res[2])
        self.assertEqual( ('43', None, None), res[0])
        #self.assertEqual(None, res.appartment)

    def test_yuogorskaya(self):
        testing_address =  'сургут югорская 30/2'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('сургут', None), res[1])
        self.assertEqual(('югорская', None), res[2])
        self.assertEqual(('30/2', None, None), res[0])
        #self.assertEqual( None, res.appartment)

    def test_index(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual((None, None), res[1] )
        self.assertEqual( (None, None), res[2])
        self.assertEqual( (None, None, None), res[0])
        #self.assertEqual( None, res.appartment)

    def test_salmanova(self):
        testing_address = 'город сургут улица фармана салманова 4'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('сургут', 'город'), res[1] )
        self.assertEqual(('фармана салманова', 'улица'), res[2])
        self.assertEqual(('4', None, None), res[0])
        #self.assertEqual( None, res.appartment)

    def test_vidnoe(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('видное', 'город'), res[1] )
        self.assertEqual( ('зеленые аллеи', None), res[2])
        self.assertEqual(('8', None, None), res[0] )
        #self.assertEqual( None, res.appartment,)

    def test_zelinskogo(self):
        testing_address = 'зелинского улица зелинского дом 2'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual( (None, None), res[1])
        self.assertEqual(('зелинского', 'улица'), res[2])
        self.assertEqual(('2', None, None), res[0])
        #self.assertEqual( None, res.appartment)

    def test_kuskovaya_corpus(self):
        testing_address = 'Кусковская 19 корпус 1 '
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual((None, None), res[1])
        self.assertEqual(('Кусковская', None), res[2])
        self.assertEqual(('19', '1', None), res[0])
        #self.assertEqual(None, res.appartment )

    def test_shosse(self):
        testing_address = 'москва щелковское шоссе 35'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('москва', None), res[1])
        self.assertEqual(('щелковское', 'шоссе'), res[2])
        self.assertEqual(('35', None, None), res[0])
        #self.assertEqual(None, res.appartment)

    def test_park(self):
        testing_address = 'город москва марьинский парк дом 25 корпус 2'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual( ('москва', 'город'), res[1])
        self.assertEqual( ('марьинский парк', None), res[2])
        self.assertEqual(('25', '2', None), res[0])
        #self.assertEqual(None, res.appartment, )

    def test_gai(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('Старый Гай'.lower(), None), (res[2][0].lower(), None))
        self.assertEqual( ('1', '2', None), res[0])
       # self.assertEqual( None, res.appartment)

    def test_third_post(self):
        testing_address = 'улица 3 почтовое отделение дом 62'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual((None, None), res[1])
        self.assertEqual(('3 почтовое отделение', 'улица'), res[2])
        self.assertEqual(('62', None, None), res[0])
        #self.assertEqual(None, res.appartment, )

    def test_july_street(self):
        testing_address = 'нижний новгород улица июльских дней 19'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual( ('нижний новгород', None), res[1])
        self.assertEqual(('июльских дней', 'улица'), res[2])
        self.assertEqual(('19', None, None), res[0])
        #self.assertEqual(None, res.appartment )

    def test_val(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual(('москва', None), res[1])
        self.assertEqual(('хамовнический вал', None), res[2])
        self.assertEqual((None, None, None), res[0])
        #self.assertEqual(None, res.appartment)

    def test_semen_bilecky(self):
        testing_address = 'город сургут улица семена билецкого 1'
        res = self.NERInstance.totalNERaddress(testing_address)

        self.assertEqual( ('сургут', 'город'), res[1])
        self.assertEqual(('семена билецкого', 'улица'), res[2])
        self.assertEqual(('1', None, None), res[0])
        #self.assertEqual( None, res.appartment,)


    def test_critical(self):
        testing_address = 'улица значит антонова овсиенко дом 19/2'
        res = self.NERInstance.totalNERaddress(testing_address)

        #print(testing_address, res)
        self.assertEqual(('антонова овсиенко', 'улица'), res[2] )
        self.assertEqual(('19/2', None, None), res[0])

    def test_critical0(self):
        testing_address = 'улица генерала армии епишева дом 9'
        res = self.NERInstance.totalNERaddress(testing_address)

        #print(testing_address, res)
        self.assertEqual(('генерала армии епишева', 'улица'), res[2] )
        self.assertEqual(('9', None, None), res[0])


    def test_critical1(self):
        testing_address = 'улица академика байкова дом 9'
        res = self.NERInstance.totalNERaddress(testing_address)

        #print(testing_address, res)
        self.assertEqual(('9', None, None), res[0])
        self.assertEqual(('академика байкова', 'улица'), res[2] )

    def test_critical2(self):
        testing_address = 'улица академика байкова дом дом дом 9'
        res = self.NERInstance.totalNERaddress(testing_address)

        #print(testing_address, res)
        self.assertEqual(('9', None, None), res[0])
        self.assertEqual(('академика байкова', 'улица'), res[2] )

    def test_critical2_3(self):
        testing_address = 'улица подзаборного байкова дом дом дом 9'
        res = self.NERInstance.totalNERaddress(testing_address)

        #print(testing_address, res)
        self.assertEqual(('9', None, None), res[0] )
        self.assertEqual(('подзаборного байкова', 'улица'), res[2] )

    def test_critical2_4(self):
        testing_address = 'улица монтажника байкова дом дом дом 9'
        res = self.NERInstance.totalNERaddress(testing_address)

        #print(testing_address, res)
        self.assertEqual(('9', None, None), res[0] )
        self.assertEqual(('монтажника байкова', 'улица'), res[2] )

    def test_critical3(self):
        testing_address = 'такзначит у меня дом номер 12 а улица джона рида'
        res = self.NERInstance.totalNERaddress(testing_address)

        #print(testing_address, res)
        self.assertEqual(('джона рида', 'улица'), res[2])
        self.assertEqual(('12', None, None), res[0])
if __name__ == '__main__':
    unittest.main()
    
    