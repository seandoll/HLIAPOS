import numpy
from distribution import BinomialDistribution
from bounding import Bounded


class Scenario:
    def __init__(self):
        pass

    dataList = list()
    sortedDataList = list()
    confidence_interval = 0
    case_name = ""
    distribution_profile = BinomialDistribution
    distribution_bounding = Bounded

    @classmethod
    def data_list(cls):
        return cls.dataList

    @classmethod
    def add_item(cls, value):
        cls.dataList.append(value)
        cls.sortedDataList = cls.dataList[:]
        cls.sortedDataList.sort()

    @classmethod
    def clear_list(cls):
        cls.dataList = list()
        cls.sortedDataList = list()

    @classmethod
    def median(cls):
        return numpy.median(cls.dataList)
