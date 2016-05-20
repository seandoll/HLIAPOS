import unittest
import scenario


class TestListPopulation(unittest.TestCase):
    def test_empty_data(self):
        a = scenario.Scenario()
        result = a.data_list()
        self.assertEqual(len(result), 0)

    def test_clear_list(self):
        a = scenario.Scenario()
        a.clear_list()
        self.assertEqual(len(a.data_list()), 0)
        self.insertItems(a, 1)
        self.assertEqual(len(a.data_list()), 1)
        a.clear_list()
        self.assertEqual(len(a.data_list()), 0)

    def test_single_item(self):
        a = scenario.Scenario()
        a.clear_list()
        a.add_item(123)
        result = a.data_list()
        self.assertEqual(len(result), 1)

    def test_confidence_interval(self):
        a = scenario.Scenario()
        a.confidence_interval = 90
        self.assertEqual(90, a.confidence_interval)

    def test_median(self):
        a = scenario.Scenario()
        self.setSize(a, 3)
        self.assertEqual(2, a.median())
        self.setSize(a, 4)
        self.assertEqual(2.5, a.median())
        self.setSize(a, 5)
        self.assertEqual(3, a.median())
        self.setSize(a, 6)
        self.assertEqual(3.5, a.median())

    def insertItems(self, caseData, items):
        for index in range(items):
            caseData.add_item(index + 1)

        return caseData

    def setSize(self, caseData, items):
        caseData.clear_list()
        self.insertItems(caseData, items)

if __name__ == '__main__':
    unittest.main()
