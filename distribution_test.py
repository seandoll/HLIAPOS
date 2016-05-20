import unittest
from distribution import BinomialDistribution, Distribution
from bounding import Bounded, Extremity


class BinomialExpansionNumberOfPossibleValuesTests(unittest.TestCase):
    def test_empty_binary_string(self):
        exp = BinomialDistribution
        number_of_possible_values = exp.number_possible_values(0)
        self.assertEqual(number_of_possible_values, 0)

    def test_single_character_binary_string(self):
        exp = BinomialDistribution
        number_of_possible_values = exp.number_possible_values(1)
        self.assertEqual(number_of_possible_values, 2)

    def test_multiple_character_binary_string(self):
        exp = BinomialDistribution
        number_of_possible_values = exp.number_possible_values(2)
        self.assertEqual(number_of_possible_values, 4)
        number_of_possible_values = exp.number_possible_values(4)
        self.assertEqual(number_of_possible_values, 16)
        number_of_possible_values = exp.number_possible_values(8)
        self.assertEqual(number_of_possible_values, 256)


class BinomialExpansionDistributionOfPossibleValuesTests(unittest.TestCase):
    def test_distribution_count(self):
        instance = BinomialDistribution
        exp = Distribution()
        distribution = exp.frequency_distribution(instance, 1)
        self.assertEqual(distribution[0], 1)
        self.assertEqual(distribution[1], 1)

        distribution = exp.frequency_distribution(instance, 2)
        self.assertEqual(distribution[0], 1)
        self.assertEqual(distribution[1], 2)
        self.assertEqual(distribution[2], 1)

        distribution = exp.frequency_distribution(instance, 3)
        self.assertEqual(distribution[0], 1)
        self.assertEqual(distribution[1], 3)
        self.assertEqual(distribution[2], 3)
        self.assertEqual(distribution[3], 1)

        distribution = exp.frequency_distribution(instance, 4)
        self.assertEqual(distribution[0], 1)
        self.assertEqual(distribution[1], 4)
        self.assertEqual(distribution[2], 6)
        self.assertEqual(distribution[3], 4)
        self.assertEqual(distribution[4], 1)

    def test_binomial_expansion_distribution_percent(self):
        instance = BinomialDistribution
        distribution = Distribution.percentage_distribution(instance, 1)
        self.assertEqual(distribution[0], 1.0 / 2)
        self.assertEqual(distribution[1], 1.0 / 2)

        distribution = Distribution.percentage_distribution(instance, 2)
        self.assertEqual(distribution[0], 1.0 / 4)
        self.assertEqual(distribution[1], 2.0 / 4)
        self.assertEqual(distribution[2], 1.0 / 4)

        distribution = Distribution.percentage_distribution(instance, 3)
        self.assertEqual(distribution[0], 1.0 / 8)
        self.assertEqual(distribution[1], 3.0 / 8)
        self.assertEqual(distribution[2], 3.0 / 8)
        self.assertEqual(distribution[3], 1.0 / 8)

    def test_binomial_expansion_bounded_count_in_values_for_given_confidence(self):
        distribution = Distribution.percentage_distribution(BinomialDistribution, 1)
        bounded_instance = Bounded
        confidence_interval = .50
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, None)

        distribution = BinomialDistribution.percentage_distribution(2)
        confidence_interval = .50
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

        distribution = BinomialDistribution.percentage_distribution(3)
        confidence_interval = .50
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

        distribution = BinomialDistribution.percentage_distribution(5)
        confidence_interval = .9
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

        distribution = BinomialDistribution.percentage_distribution(8)
        confidence_interval = .9
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 2)

        distribution = BinomialDistribution.percentage_distribution(11)
        confidence_interval = .9
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 3)

        distribution = BinomialDistribution.percentage_distribution(13)
        confidence_interval = .9
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 4)

        distribution = BinomialDistribution.percentage_distribution(5)
        confidence_interval = .9
        count_in_values = BinomialDistribution.count_ins(bounded_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

    def test_binary_expansion_extremity_count_in_values(self):
        extremity_instance = Extremity
        distribution = Distribution.percentage_distribution(BinomialDistribution, 1)
        confidence_interval = .51
        count_in_values = BinomialDistribution.count_ins(extremity_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, None)

        distribution = Distribution.percentage_distribution(BinomialDistribution, 1)
        confidence_interval = .5
        count_in_values = BinomialDistribution.count_ins(extremity_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

        distribution = Distribution.percentage_distribution(BinomialDistribution, 2)
        confidence_interval = .5
        count_in_values = BinomialDistribution.count_ins(extremity_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

        distribution = Distribution.percentage_distribution(BinomialDistribution, 3)
        confidence_interval = .51
        count_in_values = BinomialDistribution.count_ins(extremity_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

        distribution = Distribution.percentage_distribution(BinomialDistribution, 3)
        confidence_interval = .5
        count_in_values = BinomialDistribution.count_ins(extremity_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 2)

        distribution = Distribution.percentage_distribution(BinomialDistribution, 4)
        confidence_interval = .9375
        count_in_values = Distribution.count_ins(extremity_instance, distribution, confidence_interval)
        self.assertEqual(count_in_values, 1)

if __name__ == '__main__':
    unittest.main()
