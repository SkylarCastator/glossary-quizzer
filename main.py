import json
import pyfiglet
import os
import quiz as Quiz
from simple_term_menu import TerminalMenu
import glossary_scaper as Scraper


class Application:
    def __init__(self):
        self.main_menu_options = ["Start Quiz", "Load Quiz", "Resume Quiz", "Quit"]
        self.open_main_menu()

    def get_quiz_information(self, path):
        quiz_data_files = os.listdir(path)
        organized_list = {}
        for item in quiz_data_files:
            if ".json" in item:
                with open(f'{path}/{item}', 'r') as json_file:
                    data = json.load(json_file)
                    organized_list[data["name"]] = item
        return organized_list

    def open_main_menu(self):
        terminal_menu = TerminalMenu(self.main_menu_options)
        selected_option_index = terminal_menu.show()
        selected_option = self.main_menu_options[selected_option_index]
        if selected_option == "Quit":
            exit()
        elif selected_option == "Start Quiz":
            self.open_quiz_options("glossary_data")
        elif selected_option == "Load Quiz":
            self.load_quiz()
        elif selected_option == "Resume Quiz":
            self.open_quiz_options("temp")
        else:
            pass

    def open_quiz_options(self, path):
        quiz_options = self.get_quiz_information(path)
        quiz_names = list(quiz_options.keys())
        if len(quiz_names) < 1:
            print("No quiz's to resume.")
            self.open_main_menu()
        else:
            terminal_menu = TerminalMenu(quiz_names)
            selected_option_index = terminal_menu.show()
            selected_option = quiz_options[quiz_names[selected_option_index]]
            self.launch_quiz(f'{path}/{selected_option}')

    def launch_quiz(self, quiz_path):
        with open(quiz_path, 'r') as json_file:
            data = json.load(json_file)
            quiz_name = data["name"]
            glossary_terms = data['glossary']
        quiz = Quiz.Quiz(quiz_name, glossary_terms)
        quiz.generate_definition_question()

    def load_quiz(self):
        url = str(input("What is the wikipedia url you want to scrape?"))
        #url = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'
        glossary_terms = Scraper.scrape_glossary_terms(url)
        file_name = url.replace("https://en.wikipedia.org/wiki/", "")
        with open(f'glossary_data/{file_name}.json', 'w') as json_file:
            data = {
                "name": file_name,
                'glossary': glossary_terms
            }
            json.dump(data, json_file, indent=4)
        print(f"Scraping Finished for {file_name}")
        self.open_main_menu()


if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("Glossary Quizzer")
    print(ascii_banner)
    main = Application()