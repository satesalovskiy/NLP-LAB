import MyNER
import unittest


class TestPersons(unittest.TestCase):
    def setUp(self):
        self.NERInstance = MyNER.MyNER()

    def test_1(self):
        testing_address = 'Иванов Петр Васильевич'
        res = self.NERInstance.totalNERPersons(testing_address)
        self.assertEqual(res.first, 'Петр')
        self.assertEqual(res.middle, 'Васильевич')
        self.assertEqual(res.last, 'Иванов')

    def test_2(self):
        testing_address = 'шипицын дмитрий вячеславович'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'дмитрий')
        self.assertEqual(res.middle, 'вячеславович')
        self.assertEqual(res.last, 'шипицын')

    def test_3(self):
        testing_address = 'елена владимировна'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'елена')
        self.assertEqual(res.middle, 'владимировна')
        self.assertEqual(res.last, None)

    def test_4(self):
        testing_address = 'басалаева юлия михайловна'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'юлия')
        self.assertEqual(res.middle, 'михайловна')
        self.assertEqual(res.last, 'басалаева')

    def test_5(self):
        testing_address = 'ну я как раз по фамилии есть смотри мам'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, None)
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, None)

    def test_6(self):
        testing_address = 'глушенков власти на android'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, None)
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, 'глушенков')

    def test_7(self):
        testing_address = 'фамилию сказать что за фамилия терентьева людмила'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'людмила')
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, 'терентьева')

    def test_8(self):
        testing_address = 'елена владимировна'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'елена')
        self.assertEqual(res.middle, 'владимировна')
        self.assertEqual(res.last, None)

    def test_9(self):
        testing_address = 'анюта'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'анюта')
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, None)

    def test_10(self):
        testing_address = 'р1 артем витальевич'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'артем')
        self.assertEqual(res.middle, 'витальевич')
        self.assertEqual(res.last, None)
        
    def test_11(self):
        testing_address = 'фитнес веретельников олег викторович'
        res = self.NERInstance.totalNERPersons(testing_address)

        self.assertEqual(res.first, 'олег')
        self.assertEqual(res.middle, 'викторович')
        self.assertEqual(res.last, 'веретельников')


if __name__ == '__main__':
    unittest.main()