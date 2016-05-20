from distribution import Distribution

distribution = Distribution


class ScenarioDisplayConsole:
    def __init__(self):
        pass

    @classmethod
    def show(cls, scenario):
        cls.print_heading(scenario)
        cls.print_sorted_data(scenario)

    @classmethod
    def print_sorted_data(cls, scenario):
        data_items = len(scenario.data_list())
        if data_items == 0:
            return

        count_ins = ScenarioDisplayConsole.count_in(scenario)
        for i in range(data_items):
            message = str(scenario.sortedDataList[i])
            if count_ins is not None:
                if i == count_ins - 1:
                    message += " Lower bound"
                if i == data_items - count_ins:
                    message += " Upper bound"

            print(message)

    @classmethod
    def count_in(cls, scenario):
        dist = Distribution.percentage_distribution(scenario.distribution_profile, len(scenario.data_list()))
        return distribution.count_ins(scenario.distribution_bounding, dist, scenario.confidence_interval)

    @classmethod
    def print_heading(cls, scenario):
        title = scenario.case_name
        title += cls.title_confidence_interval(scenario.confidence_interval)
        title += cls.title_distribution(scenario.distribution_profile)
        title += cls.title_measurements(scenario)
        title += cls.title_sum_of_measurements(scenario)
        title += cls.title_bounding(scenario.distribution_bounding)
        print(title)
        print ''.join(["=" for i in xrange(len(title))])
        title = cls.title_forecast(scenario, 20)
        print(title)
        print ''.join(["=" for i in xrange(len(title))])

    @classmethod
    def title_confidence_interval(cls, confidence_interval):
        return ": CI = " + str(confidence_interval)

    @classmethod
    def title_distribution(cls, distribution_profile):
        return ": Dist = " + distribution_profile.distribution_name()

    @classmethod
    def title_bounding(cls, bounding):
        return ": Bounding = " + bounding.bounding_name()

    @classmethod
    def title_measurements(cls, scenario):
        return ": Measurements = " + str(len(scenario.data_list()))

    @classmethod
    def title_sum_of_measurements(cls, scenario):
        return ": Sum = " + str(sum(scenario.data_list()))

    @classmethod
    def title_forecast(cls, scenario, target_measurements):
        forecast = cls.lower_bound_forecast(scenario, target_measurements)
        forecast += cls.upper_bound_forecast(scenario, target_measurements)
        return forecast

    @classmethod
    def lower_bound_forecast(cls, scenario, target_measurements):
        forecast = "Lower bound: "
        if len(scenario.data_list()) == 0:
            forecast += "Not possible"
        else:
            count_in = cls.count_in(scenario)
            if count_in is None:
                forecast += "Not possible"
            else:
                if count_in is None:
                    forecast += "Not possible"
                else:
                    forecast += str(scenario.sortedDataList[count_in - 1] * target_measurements)

        return forecast + "\t"

    @classmethod
    def upper_bound_forecast(cls, scenario, target_measurements):
        forecast = "Upper bound: "
        if len(scenario.data_list()) == 0:
            forecast += "Not possible"
        else:
            count_in = cls.count_in(scenario)
            if count_in is None:
                forecast += "Not possible"
            else:
                if count_in is None:
                    forecast += "Not possible"
                else:
                    forecast += str(scenario.sortedDataList[len(scenario.data_list()) - count_in] * target_measurements)

        return forecast + "\t"

