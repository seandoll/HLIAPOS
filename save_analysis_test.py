import unittest
from scenario import Scenario
from save_analysis import SaveAnalysis
import webbrowser
from bounding import Bounded, Extremity
from distribution import BinomialDistribution, UniformDistribution, Distribution
from scenario_display import ScenarioDisplayConsole


class SaveAnalysisText(unittest.TestCase):
    def test_view_distribution_graph(self):
        this_file = SaveAnalysis
        scenario = Scenario
        scenario.clear_list()
        self.__add_items(scenario)
        this_file.save_data(scenario)
        self.__show_boundings_for_scenario(scenario)
        self.__load_chart_page()

    @staticmethod
    def __add_items(scenario):
        scenario.confidence_interval = 0.90
        scenario.add_item(636)

    @staticmethod
    def __show_bounding_for_uniform_extremity_scenario(scenario):
        scenario.case_name = "Uniform Extremity"
        scenario.distribution_profile = UniformDistribution
        scenario.distribution_bounding = Extremity
        ScenarioDisplayConsole.display(scenario)

    @staticmethod
    def __show_bounding_for_uniform_bounded_scenario(scenario):
        scenario.case_name = "Uniform Bounded"
        scenario.distribution_profile = UniformDistribution
        scenario.distribution_bounding = Bounded
        ScenarioDisplayConsole.display(scenario)

    @staticmethod
    def __show_bounding_for_binomial_extremity_scenario(scenario):
        scenario.case_name = "Binomial Extremity"
        scenario.distribution_profile = BinomialDistribution
        scenario.distribution_bounding = Extremity
        ScenarioDisplayConsole.display(scenario)

    @staticmethod
    def __show_bounding_for_binomial_bounded_scenario(scenario):
        scenario.case_name = "Binomial Bounded"
        scenario.distribution_profile = BinomialDistribution
        scenario.distribution_bounding = Bounded
        ScenarioDisplayConsole.display(scenario)

    @staticmethod
    def __load_chart_page():
        new_tab = 0
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(chrome_path).open("http://localhost:63342/HLIAPOS/BinomialAndUniformDistribution.html",
                                         new=new_tab)

    def __show_boundings_for_scenario(self, scenario):
        print("\nUniform Distribution Percentages")
        print(Distribution.percentage_distribution(UniformDistribution, len(scenario.dataList)))
        self.__show_bounding_for_uniform_bounded_scenario(scenario)
        self.__show_bounding_for_uniform_extremity_scenario(scenario)
        print("\nBinomial Distribution Percentages")
        print(Distribution.percentage_distribution(BinomialDistribution, len(scenario.dataList)))
        self.__show_bounding_for_binomial_bounded_scenario(scenario)
        self.__show_bounding_for_binomial_extremity_scenario(scenario)


if __name__ == '__main__':
    unittest.main()
