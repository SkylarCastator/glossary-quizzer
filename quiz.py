import random
import json
from simple_term_menu import TerminalMenu
import pyfiglet


class Quiz:
    def __init__(self):
        pass

    def generate_definition_question(self):
        random_term = random.choice(glossary_terms)
        question = f"Given the definition, what is the correct term?"
        question_prompt = random_term['definition']
        options = self.generate_term_options(random_term['term'])
        print(question)
        print(question_prompt)
        print("")
        terminal_menu = TerminalMenu(options)
        selected_option_index = terminal_menu.show()

        # Get the selected option
        selected_option = options[selected_option_index]

        # Check the answer
        if selected_option == random_term['term']:
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer is: {random_term['term']}")
        print("")
        self.generate_definition_question()

    def generate_term_options(self, correct_option):
        options = [correct_option]

        # Generate three incorrect options randomly from other glossary terms
        while len(options) < 4:
            random_term = random.choice(glossary_terms)
            random_definition = random_term['term']
            if random_definition not in options:
                options.append(random_definition)

        # Shuffle the options
        random.shuffle(options)
        return options

    def generate_question(self):
        random_term = random.choice(glossary_terms)

        # Prompt user with a multiple-choice question
        question = f"What does '{random_term['term']}' mean?"
        options = self.generate_options(random_term['definition'])
        print(question)
        print("")
        terminal_menu = TerminalMenu(options)
        selected_option_index = terminal_menu.show()

        # Get the selected option
        selected_option = options[selected_option_index]

        # Check the answer
        if selected_option == random_term['definition']:
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer is: {random_term['definition']}")
        print("")
        self.generate_question()

    def generate_options(self, correct_option):
        options = [correct_option]

        # Generate three incorrect options randomly from other glossary terms
        while len(options) < 4:
            random_term = random.choice(glossary_terms)
            random_definition = random_term['definition']
            if random_definition not in options:
                options.append(random_definition)

        # Shuffle the options
        random.shuffle(options)
        return options


# Load the glossary terms from the JSON file
with open('glossary_data/cg_glossary.json', 'r') as json_file:
    data = json.load(json_file)
    glossary_terms = data['glossary']

ascii_banner = pyfiglet.figlet_format("Quizzer")
print(ascii_banner)
quiz = Quiz()
quiz.generate_definition_question()