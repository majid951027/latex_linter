import unittest
from latex_linter import linter_rules


class test_cases(unittest.TestCase):
    def test_newlines(self):
        linter = linter_rules(["Det här är en subsection \n \subsection"])
        linter.add_blank_lines()

    def test_tabs(self):
        linter = linter_rules(
            ["\begin{center} \n Laborationsuppgifter \n \end{center}"]
        )
        linter.tab_adding()


if __name__ == "__main__":
    unittest.main()
