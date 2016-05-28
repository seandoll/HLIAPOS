from distribution import Distribution

distribution = Distribution


class ScenarioDisplayConsole:
    def __init__(self):
        pass

    @classmethod
    def display(cls, scenario):
        cls.__print_heading(scenario)
        cls.__print_sorted_data(scenario)

    @classmethod
    def __print_sorted_data(cls, scenario):
        data_items = len(scenario.data_list())
        if data_items == 0:
            return

        count_ins = ScenarioDisplayConsole.__count_in(scenario)
        for i in range(data_items):
            message = str(scenario.sortedDataList[i])
            if count_ins is not None:
                if i == count_ins - 1:
                    message += " Lower bound"
                if i == data_items - count_ins:
                    message += " Upper bound"

            print(message)

    @classmethod
    def __count_in(cls, scenario):
        dist = Distribution.percentage_distribution(scenario.distribution_profile, len(scenario.data_list()))
        count_in = distribution.count_ins(scenario.distribution_bounding, dist, scenario.confidence_interval)
        if count_in is None:
            return 0
        else:
            return count_in

    @classmethod
    def __print_heading(cls, scenario):
        cls.__print_title_header(scenario)
        cls.__print_title_forecast(scenario)

    @classmethod
    def __print_title_forecast(cls, scenario):
        title = cls.__title_forecast(scenario, 20)
        cls.__print_underlined_text(title)

    @classmethod
    def __print_title_header(cls, scenario):
        title = cls.__title_header(scenario)
        cls.__print_underlined_text(title)

    @classmethod
    def __title_header(cls, scenario):
        title = scenario.case_name
        title += cls.__title_confidence_interval(scenario.confidence_interval)
        title += cls.__title_distribution(scenario.distribution_profile)
        title += cls.__title_measurements(scenario)
        title += cls.__title_sum_of_measurements(scenario)
        # title += cls.__title_bounding(scenario.distribution_bounding)
        return title

    @classmethod
    def __print_underlined_text(cls, title):
        print(title)
        print ''.join(["=" for i in xrange(len(title))])

    @classmethod
    def __title_confidence_interval(cls, confidence_interval):
        return cls.value_separator() + "CI = " + str(confidence_interval)

    @classmethod
    def __title_distribution(cls, distribution_profile):
        return cls.value_separator() + "Dist = " + distribution_profile.distribution_name()

    @classmethod
    def __title_bounding(cls, bounding):
        return cls.value_separator() + "Bounding = " + bounding.bounding_name()

    @classmethod
    def __title_measurements(cls, scenario):
        return cls.value_separator() + "Measurements = " + str(len(scenario.data_list()))

    @classmethod
    def __title_sum_of_measurements(cls, scenario):
        return cls.value_separator() + "Sum = " + str(sum(scenario.data_list()))

    @classmethod
    def value_separator(cls):
        return " :: "

    @classmethod
    def __title_forecast(cls, scenario, target_measurements):
        forecast = cls.count_in_display_text(scenario)
        forecast += cls.__lower_bound_forecast(scenario, target_measurements)
        forecast += cls.__upper_bound_forecast(scenario, target_measurements)
        return forecast

    @classmethod
    def count_in_display_text(cls, scenario):
        return "Count Ins: " + str(cls.__count_in(scenario))

    @classmethod
    def __lower_bound_forecast(cls, scenario, target_measurements):
        forecast = cls.value_separator() + "Lower bound forecast: "
        if cls.__count_in_possible(scenario):
            count_in = cls.__count_in(scenario)
            forecast += str(scenario.sortedDataList[count_in - 1] * target_measurements)
        else:
            forecast += "Not possible"

        return forecast

    @classmethod
    def __upper_bound_forecast(cls, scenario, target_measurements):
        forecast = cls.value_separator() + "Upper bound forecast: "
        if cls.__count_in_possible(scenario):
            count_in = cls.__count_in(scenario)
            forecast += str(scenario.sortedDataList[len(scenario.data_list()) - count_in] * target_measurements)
        else:
            forecast += "Not possible"

        return forecast

    @classmethod
    def __count_in_possible(cls, scenario):
        if len(scenario.data_list()) == 0 or cls.__count_in(scenario) == 0:
            return False

        return True

