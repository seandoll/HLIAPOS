import math


class Distribution:
    def __init__(self):
        pass

    @classmethod
    def frequency_distribution(cls, implementation, trials):
        return implementation.frequency_distribution(trials)

    @classmethod
    def percentage_distribution(cls, implementation, trials):
        if trials == 0:
            return None

        return implementation.percentage_distribution(trials)

    @classmethod
    def count_ins(cls, count_in_instance, distribution, confidence_interval):
        return count_in_instance.count_in_values(distribution, confidence_interval)

    @classmethod
    def print_distribution_percent(cls, dist):
        print("With " + str(len(dist)) + " trials")
        for x in range(len(dist)):
            print(str(x) + " band is " + str(dist[x] * 100) + "% likely")


class BinomialDistribution:
    def __init__(self):
        pass

    @classmethod
    def number_possible_values(cls, trials):
        if trials == 0:
            return 0
        else:
            return 2 ** trials

    @classmethod
    def frequency_distribution(cls, trials):
        dist = list()
        for x in range(trials + 1):
            occurrences = 1.0 * math.factorial(trials) / (math.factorial(x) * math.factorial(trials - x))
            dist.append(occurrences)
        return dist

    @classmethod
    def percentage_distribution(cls, trials):
        dist = cls.frequency_distribution(trials)
        percent = list()
        possible_values = cls.number_possible_values(trials)

        for x in range(trials + 1):
            percent.append(1.0 * dist[x] / possible_values)

        return percent

    @classmethod
    def count_ins(cls, count_in_instance, distribution, confidence_interval):
        return count_in_instance.count_in_values(distribution, confidence_interval)

    @classmethod
    def distribution_name(cls):
        return "Binomial"


class UniformDistribution:
    def __init__(self):
        pass

    @classmethod
    def number_possible_values(cls, trials):
        if trials == 0:
            return 0
        else:
            return trials + 1

    @classmethod
    def frequency_distribution(cls, trials):
        return [1] * (trials + 1)

    @classmethod
    def percentage_distribution(cls, trials):
        possible_values = cls.number_possible_values(trials)
        return [1.0 / possible_values] * (trials + 1)

    @classmethod
    def count_ins(cls, count_in_instance, distribution, confidence_interval):
        return count_in_instance.count_in_values(distribution, confidence_interval)

    @classmethod
    def distribution_name(cls):
        return "Uniform"
