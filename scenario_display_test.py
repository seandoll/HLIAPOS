import unittest
from scenario_display import ScenarioDisplayConsole
from scenario import Scenario
import distribution
from bounding import Bounded, Extremity


class ScenarioDisplayTest(unittest.TestCase):
    def test_set_case_name(self):
        scenario = Scenario
        scenario.case_name = "Example session title"
        self.assertEqual(scenario.case_name, "Example session title")
        display = ScenarioDisplayConsole
        display.display(scenario)

    @staticmethod
    def test_set_confidence_interval():
        scenario = Scenario
        scenario.confidence_interval = .5

    @staticmethod
    def test_show_single_item():
        scenario = Scenario
        scenario.case_name = "Single item"
        scenario.confidence_interval = 0.5
        scenario.add_item(17)
        ScenarioDisplayConsole.display(scenario)

    @staticmethod
    def test_show_rule_of_five_binomial_distribution():
        scenario = Scenario
        scenario.distribution_profile = distribution.BinomialDistribution
        scenario.distribution_bounding = Bounded
        scenario.case_name = "Rule of 5"
        scenario.confidence_interval = 0.9
        scenario.clear_list()
        scenario.add_item(17)
        scenario.add_item(25)
        scenario.add_item(65)
        scenario.add_item(45)
        scenario.add_item(12)
        # display = ScenarioDisplay_Console
        ScenarioDisplayConsole.display(scenario)

    @staticmethod
    def test_show_two_items_linear_distribution():
        scenario = Scenario
        scenario.case_name = "Two items linear - low confidence"
        scenario.confidence_interval = 0.32
        scenario.distribution_profile = distribution.UniformDistribution
        scenario.distribution_bounding = Extremity
        scenario.clear_list()
        scenario.add_item(17)
        scenario.add_item(25)
        ScenarioDisplayConsole.display(scenario)

if __name__ == '__main__':
    unittest.main()
