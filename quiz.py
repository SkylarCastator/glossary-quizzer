import random
import json
from simple_term_menu import TerminalMenu
import pyfiglet


class Quiz:
    def __init__(self, glossary_terms):
        print(f"The Quiz contains {len(glossary_terms)} items.")
        print("")
        self.question_num = 1
        self.original_set = glossary_terms
        self.quiz_set = glossary_terms
        self.incorrect_answers = []

    def generate_definition_question(self):
        random_term = random.choice(self.quiz_set)
        question = f"Given the definition, what is the correct term?"
        question_prompt = random_term['definition']
        options = self.generate_term_options(random_term['term'])
        print(f"{self.question_num}. {question}")
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
            self.incorrect_answers.append(random_term)
        print("")
        self.quiz_set.remove(random_term)
        self.question_num += 1
        self.active_quiz_data()
        self.question_menu()

    def generate_term_options(self, correct_option):
        options = [correct_option]

        # Generate three incorrect options randomly from other glossary terms
        while len(options) < 4:
            random_term = random.choice(self.original_set)
            random_definition = random_term['term']
            if random_definition not in options:
                options.append(random_definition)

        # Shuffle the options
        random.shuffle(options)
        return options

    def generate_question(self):
        random_term = random.choice(self.quiz_set)

        # Prompt user with a multiple-choice question
        question = f"{self.question_num}. What does '{random_term['term']}' mean?"
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
            self.incorrect_answers.append(random_term)
        print("")
        self.quiz_set.remove(random_term)
        self.question_num += 1
        self.active_quiz_data()
        self.question_menu()
        #self.generate_question()

    def generate_options(self, correct_option):
        options = [correct_option]

        # Generate three incorrect options randomly from other glossary terms
        while len(options) < 4:
            random_term = random.choice(self.original_set)
            random_definition = random_term['definition']
            if random_definition not in options:
                options.append(random_definition)

        # Shuffle the options
        random.shuffle(options)
        return options

    def question_menu(self):
        options = ["Continue", "Quit"]
        terminal_menu = TerminalMenu(options)
        selected_option_index = terminal_menu.show()
        selected_option = options[selected_option_index]
        if selected_option == "Quit":
            exit()
        else:
            self.generate_definition_question()

    def active_quiz_data(self):
        quiz_name = "computer_graphics"
        quiz_data = {
            "quiz_data_path": quiz_name,
            "questions_remaining": self.quiz_set,
            "questions_incorrectly_answered": self.incorrect_answers
        }
        with open(f'temp/{quiz_name}.json', 'w') as json_file:
            json.dump(quiz_data, json_file, indent=4)


