import random
import json
import dropdownmenu


class Quiz:
    def __init__(self, main, name, glossary_terms):
        self.main = main
        self.name = name
        print(f"{name} Quiz")
        print(f"The Quiz contains {len(glossary_terms)} items.\n")
        self.question_num = 1
        self.original_set = glossary_terms.copy()
        self.quiz_set = glossary_terms
        self.correct_answers = []
        self.incorrect_answers = []

    def generate_definition_question(self):
        if len(self.quiz_set) > 0:
            random_term = random.choice(self.quiz_set)
            question = f"Given the definition, what is the correct term? \n {random_term['definition']}"
            answer = random_term['term']
            options = self.generate_term_options(answer)
            selected_option = self.prompt_question(question, options)
            self.check_answer(selected_option, answer, random_term)
            self.quiz_set.remove(random_term)
            self.question_num += 1
            self.active_quiz_data()
            self.question_menu()
        else:
            self.show_quiz_results()

    def prompt_question(self, question, options):
        print(f"{self.question_num}. {question} \n")
        selected_option = dropdownmenu.dropdown_menu(options)
        return selected_option

    def check_answer(self, selected_option, answer, question):
        if selected_option == answer:
            print("Correct!")
            self.correct_answers.append(question)
        else:
            print("Incorrect!")
            print(f"The correct answer is: {answer}")
            self.incorrect_answers.append(question)
        print("")

    def generate_term_options(self, correct_option):
        options = [correct_option]
        while len(options) < 4:
            random_term = random.choice(self.original_set)
            random_definition = random_term['term']
            if random_definition not in options:
                options.append(random_definition)

        # Shuffle the options
        random.shuffle(options)
        return options

    def question_menu(self):
        options = ["Continue", "Quit"]
        selected_option = dropdownmenu.dropdown_menu(options)
        if selected_option == "Quit":
            exit()
        else:
            self.generate_definition_question()

    def show_quiz_results(self):
        with open(f'temp/{self.name}.json', 'r') as json_file:
            data = json.load(json_file)
        print(f"You just finished the {self.name} quiz!")
        correct = len(data["correct"])
        total_questions = len(data["original"])
        score = int((correct/total_questions) * 100.0)
        print(f"You Scored : {score}% or got {correct}/{total_questions} correct!")
        print(f"Access your test results using this file : temp/{self.name}.json\n")
        options = ["Main Menu", "Quit"]
        selected_option = dropdownmenu.dropdown_menu(options)
        if selected_option == "Quit":
            exit()
        else:
            self.main.open_main_menu()

    def active_quiz_data(self):
        quiz_data = {
            "name": self.name,
            "glossary": self.quiz_set,
            "original": self.original_set,
            "incorrect": self.incorrect_answers,
            "correct": self.correct_answers
        }
        with open(f'temp/{self.name}.json', 'w') as json_file:
            json.dump(quiz_data, json_file, indent=4)


