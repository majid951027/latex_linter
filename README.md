Linter for LaTeX
This is a simple linter for LaTeX files. It reads a LaTeX file and performs several formatting checks to improve the readability of the file. The linting rules are specified in a JSON file, and the program outputs the edited file with the suffix "_edited.tex".

How to Use
The program can be run from the command line using the following command:

python3 latex_linter.py fileName.tex

Replace "fileName.tex" with the name of the LaTeX file you want to modify.

Linting Rules
The program currently checks for the following rules:

Newline after Sentence
Adds a new line after every sentence.

Adding Tabs
Adds indentation using tabs for specific environments, such as "begin" and "end".

Adding Blank Lines
Adds a blank line after every section, such as "chapter", "section", "subsection", and "subsubsection".

Formatting Comments
Formats comments to be in the same line as the text.

The rules can be customized in the rules.json file. Each rule has a boolean value that specifies whether the rule should be applied or not.

Dependencies
The program requires the argparse and json libraries to run.
