# 5_lang_frequency
The script is designed to find 10 most frequent words in the text.

The script can work with texts written in any language.

To run the script in console you should write:
```bash
python3 lang_frequency.py --path "./filename.txt"
```
or
```bash
python3 lang_frequency.py --path "/home/user/Documents/filename.txt"
```
Where **--path** the argument which assumes the script is a relative or full path to file with text.

For this text and will be counted the frequency of words.


##### The script can test for the most frequent words in the text, two different calculation methods.
For this you need to run the script in the following way:
```bash
python3 lang_frequency.py --testing --path "./filename.txt"
```
or
```bash
python3 lang_frequency.py --testing --path "/home/user/Documents/filename.txt"
```
Where **--testing** the argument, which starts the testing of two different calculation methods,
compares the results and displays the results of their work.
