import json
from distribution import Distribution, BinomialDistribution, UniformDistribution


class SaveAnalysis(object):
    @classmethod
    def save(cls, scenario):
        f = open(scenario.case_name, "w")
        f.write(json.dumps(scenario.confidence_interval) + "\n")
        f.write(json.dumps(scenario.median()) + "\n")
        f.write(json.dumps(scenario.sortedDataList))
        f.close()

    @classmethod
    def save_data(cls, scenario):
        try:
            datafile = open(cls.scenario_filename(), mode="w")
        except OSError as os_err:
            print("OSError: " + os_err.message)
        except IOError as e:
            print("IOError: " + str(e))
        except Exception as catchall:
            print("Error : " + str(catchall))
        else:
            datafile.writelines(cls.header())
            datafile.writelines(cls.data_lines(scenario))
            datafile.close()

    @classmethod
    def header(cls):
        return "measurement" + "\t" + "uniform_frequency" + "\t" + "binomial_frequency" + "\t" + "width" + "\n"

    @classmethod
    def scenario_filename(cls, scenario):
        return scenario.case_name.replace(" ", "") + ".tsv"

    @classmethod
    def scenario_filename(cls):
        return "TestDataScenario.tsv"

    @classmethod
    def data_lines(cls, scenario):
        data_string = ""
        data_items = len(scenario.dataList)
        dist = Distribution()
        uniform_distribution = dist.percentage_distribution(UniformDistribution(), data_items)
        binomial_distribution = dist.percentage_distribution(BinomialDistribution(), data_items)

        data_string += SaveAnalysis.leading_line(binomial_distribution, scenario, uniform_distribution)
        data_string += SaveAnalysis.measurement_lines(binomial_distribution, scenario, uniform_distribution)
        data_string += SaveAnalysis.trailing_line(scenario)

        return data_string

    @classmethod
    def measurement_lines(cls, binomial_distribution, scenario, uniform_distribution):
        data_string = ""
        for x in range(len(scenario.sortedDataList)):
            if x == len(scenario.sortedDataList):
                width = scenario.sortedDataList[0]
            else:
                if len(scenario.dataList) == x + 1:
                    width = scenario.sortedDataList[0]
                else:
                    width = scenario.sortedDataList[x + 1] - scenario.sortedDataList[x]

            data_string += cls.single_line(scenario.sortedDataList[x], uniform_distribution[x + 1],
                                           binomial_distribution[x + 1], width)

        return data_string

    @classmethod
    def trailing_line(cls, scenario):
        return cls.single_line(
            float(scenario.sortedDataList[len(scenario.sortedDataList) - 1]) + float(scenario.sortedDataList[0]), 0, 0,
            0)

    @classmethod
    def leading_line(cls, binomial_distribution, scenario, uniform_distribution):
        return cls.single_line(0, uniform_distribution[0], binomial_distribution[0], scenario.sortedDataList[0])

    @classmethod
    def single_line(cls, measured_value, uniform_distribution, binomial_distribution, width):
        return str(float(measured_value)) + "\t" + str(float(uniform_distribution)) + "\t" + str(
            float(binomial_distribution)) + "\t" + str(float(width)) + "\n"
