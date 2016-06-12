class Extremity:
    def __init__(self):
        pass

    @classmethod
    def count_in_values(cls, distribution, confidence_interval):
        if cls.count_in_possible(confidence_interval, distribution):
            return CountIn.count_ins(confidence_interval, distribution, 1)
        else:
            return None

    @classmethod
    def count_in_possible(cls, confidence_interval, distribution):
        return 1 - confidence_interval >= distribution[0]

    @classmethod
    def bounding_name(cls):
        return "Extremity"


class Bounded:
    def __init__(self):
        pass

    @classmethod
    def count_in_values(cls, distribution, confidence_interval):
        if cls.count_in_possible(confidence_interval, distribution):
            return CountIn.count_ins(confidence_interval, distribution, 2)
        else:
            return None

    @classmethod
    def count_in_possible(cls, confidence_interval, distribution):
        if distribution is None:
            return False
        else:
            return (len(distribution) > 0) & (1.0 - confidence_interval >= 2 * distribution[0])

    @classmethod
    def bounding_name(cls):
        return "Bounded"


class CountIn:
    def __init__(self):
        pass

    @classmethod
    def count_ins(cls, confidence_interval, distribution, count_in_multiplication_factor):
        counted_in_confidence_interval = 0.0
        i = 0
        while counted_in_confidence_interval + count_in_multiplication_factor * distribution[i] <= 1 \
                - confidence_interval:
            counted_in_confidence_interval += count_in_multiplication_factor * distribution[i]
            i += 1
        return i
