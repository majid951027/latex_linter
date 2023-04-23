import argparse
import json

# from read import read_file
# from rules_file import Rules
# from output import Output


def read_file(file):
    """The function that read the input file and send the content further"""
    file_content = []
    with open(file, "r") as textfile:
        file_content = textfile.readlines()
        textfile.close()
    return file_content


class Output:
    """Here we write all the output in a new file"""

    def __init__(self, content, file):
        self.content = content
        file_created = file.replace(".tex", "_edited.tex")
        self.new_file = open(file_created, "w")

    def edited_file(self):
        """The function that writes the outcomes"""
        for line in self.content:
            self.new_file.writelines(line)
        self.new_file.close()


class linter_rules:
    """Here is the all the used rules"""

    def __init__(self, content):
        self.lines_container = content
        self.obj = None
        with open("rules.json", "r") as myjsonfile:
            jsondata = myjsonfile.read()
            self.obj = json.loads(jsondata)
            myjsonfile.close()

    def add_newline(self):
        # Adds a new line after every sentence.
        if self.obj.get("newline", False):
            for i, line in enumerate(self.lines_container):
                if "%" in line:
                    continue
                for symbols in [". ", "!", "?"]:
                    if symbols in line:
                        split_line = line.split(symbols)
                        split_line = [
                            s.strip() for s in split_line
                        ]  # Remove whitespace
                        split_line = [s + symbols for s in split_line[:-1]] + [
                            split_line[-1]
                        ]
                        line = "\n".join(split_line)
                self.lines_container[i] = line
        else:
            print(
                "The newline option is not set correctly in the JSON file. Please read the README file."
            )

    def tab_adding(self):
        try:
            if self.obj.get("adding_tabs", False):
                for line_num, line in enumerate(self.lines_container):
                    words = line.split()
                    try:
                        if words[0].find("begin{") == True:
                            begin_env = words[0]
                            start, end = begin_env.index("{"), begin_env.index("}")
                            env_name = begin_env[start : end + 1]
                            end_env = r"\end" + env_name
                            while (
                                line_num < len(self.lines_container) - 1
                                and end_env not in self.lines_container[line_num + 1]
                            ):
                                self.lines_container[line_num + 1] = (
                                    "\t" + self.lines_container[line_num + 1]
                                )
                                line_num += 1
                    except IndexError:
                        continue
            else:
                print("something is wrong")
        except KeyError:
            print("something is wrong in json file")

    def add_blank_lines(self):
        """Adds a blank line after every section."""
        sign_list = ["\chapter", "\section", "\subsection", "\subsubsection"]
        try:
            if self.obj.get("blank_lines", False):
                for index, line in enumerate(self.lines_container):
                    seperated_words = line.split()
                    try:
                        if seperated_words[0].startswith(tuple(sign_list)):
                            if self.lines_container[index + 1] != "\n":
                                self.lines_container.insert(index + 1, "\n")
                                index += 1
                    except IndexError:
                        continue
            else:
                print(
                    "The value of 'blank_lines' in the JSON file is either False or missing. Please read README file."
                )
        except KeyError:
            print(
                "The JSON file does not contain the key 'blank_lines'. Please read README file."
            )

    def format_comment(self):
        """Formats comments to be in the same line as the text."""
        try:
            if self.obj.get("comment_space", True):
                for index, line in enumerate(self.lines_container):
                    if " %" in line:
                        self.lines_container[index] = line.replace("%", "% ")
            else:
                print(
                    "The value of 'format_comment' in the JSON file is either False or missing. Please read README file."
                )
        except KeyError:
            print(
                "The JSON file does not contain the key 'format_comment'. Please read README file."
            )


def _main_():
    parser = argparse.ArgumentParser(description="Name of the file")
    parser.add_argument(
        "fileName", type=str, help="name of latex file you want to modify"
    )
    args = parser.parse_args()
    fileName = args.fileName
    if fileName.endswith(".tex") is False:
        print("The file format is unacceptable. Please insert a tex file")
    else:
        try:
            input_file = read_file(fileName)
            user_object = linter_rules(input_file)
            user_object.add_newline()
            user_object.format_comment()
            user_object.tab_adding()
            user_object.add_blank_lines()
            result = Output(user_object.lines_container, fileName)
            result.edited_file()
        except FileNotFoundError:
            print("The file cannot be found.")


if __name__ == "__main__":
    _main_()
