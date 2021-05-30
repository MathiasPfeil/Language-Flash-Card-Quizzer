import random
import csv
import sys
import re
from os import listdir

class FlashCards:

    def __init__(self, cmd_args, word_list_dir, languages):
        self.__wrong_words = [] # When answer incorrect, question is stored here
        self.__words       = [] # Words loaded from CSV file are stored here
        self.__correct     = 0  # Incrementer for num of correct answers
        self.__cmd_args    = cmd_args
        self.__word_set    = 0
        self.__trans_dir   = 0
        self.__file_names  = listdir(word_list_dir)
        self.__languages   = languages

    # Main entry point
    def run(self):
        self.__get_word_set()
        self.__get_translate_direction()
        self.__import_words()
        self.__check_words()
        self.__print_results()
        self.__update_missed_words()

    # Ask user to choose the word-set they
    # would like to practice
    def __get_word_set(self):
        for i, file_name in enumerate(self.__file_names):
            print(f"Test on {re.sub('.csv', '', file_name)} words - {i}")
        test_direction = int(input("Word set: "))
        self.__word_set = 'words/' + self.__file_names[test_direction]

    # Open word-set csv file and store data in
    # word_set variable
    def __import_words(self):
        with open(self.__word_set, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                self.__words.append(row)

        random.shuffle(self.__words)

    # Ask user to choose if they want English
    # to Norwegian, or the opposite direction
    def __get_translate_direction(self):
        print(f"If {self.__languages[1]} to {self.__languages[0]}, answer: 0")
        print(f"If {self.__languages[0]} to {self.__languages[1]}, answer: 1")
        translate_direction = int(input("Translate direction: "))
        self.__trans_dir = translate_direction

    # Main loop run to quiz the user
    def __check_words(self):
        for i, word in enumerate(self.__words):
            answer = input(str(i) + ' ' +self.__languages[self.__trans_dir] + ' translation for ' + word[self.__trans_dir] + ': ')
            if(answer in word[int(not self.__trans_dir)] and answer != ''):
                print('Right!')
                self.__correct+=1
            else:
                self.__wrong_words.append(word)
                print('Wrong... The correct answer was: ' + word[int(not self.__trans_dir)])

    # After quiz is over, print the results
    def __print_results(self):
        print(f"""
        Total words:       {str(len(self.__words))}
        Correct answers:   {str(self.__correct)}
        Incorrect answers: {str(len(self.__words) - self.__correct)}
        """)

    # Store missed questions in the missed_words
    # csv file for later practice
    def __update_missed_words(self):
        update_missed_words = input("Would you like to update missed_words.csv file? y/n ")
        if(update_missed_words == 'y'):
            open('./words/missed_words.csv', 'w').close()
            with open('./words/missed_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for word_pair in self.__wrong_words:
                    writer.writerow(word_pair)

fc = FlashCards(sys.argv, "./words", ['English','Norwegian'])
fc.run()