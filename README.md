# Voice2Text

## Task 1

The task was to create a reusable library that can convert speech to cleaned text.

### How to use

The module works with Python >= 3.6. It is made in the form of a Python package. Inside the cloned folder run the following command to install the package:

```shell
pip install .
```

Now open the Python shell and use as below:

```python
import voice2text as v
v.convert()
```

The `convert()` function will listen to your message and return you the cleaned text. Make sure you have a working internet connection.


### Approach
I used the Python's `speech_recognition` module to convert the speech to text and then processed the text to convert it.  
To solve the task I created 4 functions

* First function does the basic text cleaning.
* Then the currency words are converted to symbols, such as `10 dollars` is converted to `$10`. It converts the word into its symbol only when the word is found with a number. For ex. it will convert `I have 10 dollars` to `I have $10` but the sentence `Euro is stronger than dollar` will remain unchanged.
* Then the title words are converted to their acronyms such as `doctor` to `Dr.`. In this also if a title appears then it checks if it appears with a name of a person (using Named Entity Recognition) then only it converts it into its acronym.
* The last one converts the repetitions. Such as `double A` is converted to `AA`

## Task 2

To design a spoken English to written English conversion system that can be continuously matured overtime.

### Approach

Converting speech to text is a trivial task and can be done using the existing APIs with good accuracy. The main challenge lies in the conversation, to get a text from the user and generating a valid response. This is challenging because there are numerous rules and exceptions present in every language and all those are very hard to capture.

For building a conversational bot, the best approach would be to construct a deep learning RNN model and train it on a dataset. After training we can evaluate the performance and fine tune it. Using the various NLP libraries we can hard-code some of the conversational rules and clean the text input by the user. Then feed the cleaned text to the bot to generate better response.
