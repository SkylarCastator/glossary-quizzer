import json
import pyfiglet
import os
import quiz as Quiz
import dropdownmenu
import glossary_scaper as Scraper
import validators


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
        selected_option = dropdownmenu.dropdown_menu(self.main_menu_options)
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
            print("No quizs available.")
            self.open_main_menu()
        else:
            quiz_names.append("Back")
            selected_option = dropdownmenu.dropdown_menu(quiz_names)
            if selected_option != "Back":
                selected_option = quiz_options[selected_option]
                self.launch_quiz(f'{path}/{selected_option}')
            else:
                self.open_main_menu()

    def launch_quiz(self, quiz_path):
        with open(quiz_path, 'r') as json_file:
            data = json.load(json_file)
            quiz_name = data["name"]
            glossary_terms = data['glossary']
        quiz = Quiz.Quiz(self, quiz_name, glossary_terms)
        quiz.generate_definition_question()

    def load_quiz(self):
        url = str(input("What is the wikipedia url you want to scrape?"))
        if url != "" and validators.url(url):
            glossary_terms = Scraper.scrape_glossary_terms(url)
            file_name = url.replace("https://en.wikipedia.org/wiki/", "")
            with open(f'glossary_data/{file_name}.json', 'w') as json_file:
                data = {
                    "name": file_name,
                    'glossary': glossary_terms
                }
                json.dump(data, json_file, indent=4)
            print(f"Scraping Finished for {file_name}")
        else:
            print(f"URL : {url} not found\n")
        self.open_main_menu()


if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("Glossary Quizzer")
    print(ascii_banner)
    main = Application()