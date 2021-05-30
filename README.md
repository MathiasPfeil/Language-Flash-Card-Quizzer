# Language Flash Card Quizzer (Python)

A small command line application I built to quiz myself on Norwegian, but it will work for any language. Functions like a set of flash cards. You will be given a word, which you have to translate. If your translation is correct, you get a point, and if not, that word is added to a list you can revisit later to refine your skills.

## How to use it

To begin, we can run `python main.py` while in our main directory to start the script.

Once the script is run, you will first be asked to select a word-set. At the moment, we only have the default set, so select the corresponding number (0).

You will then be asked the direction of the translation. Depending on which option you select, you will have to translate Norwegian into English, or vise-versa. Select whichever you prefer.

You are now ready to start translating. Once finished translating, you will get a rundown of how you did, and will be asked if you want to update the missed_words.csv file. Select y in order to create the missed_words.csv file.

If you now run the script again, you will notice that missed_words will now be one of the word-sets available. This means you can focus just on the words you are having difficulty with.

## How to customize.

If you want to add words to quiz on, or learn a different language, you can simply replace the words inside the default.csv file, or create a new file and follow the format found in default.csv. Any new csv file added to the words directory will automatically appear in the script when you are selecting word-sets.

## Requirements

Only tested on Python 3.7.3