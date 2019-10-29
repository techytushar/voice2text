# coding=utf-8

import speech_recognition as sr
from nltk import pos_tag

import re

from .utils import curr_to_symbol, num_dict, title_dict, rep_dict

def clean_text(text):
    for word, value in num_dict.items():
        text = text.replace(word, value)
    return text

def convert_titles(text):
    # converts name titles to their acronyms
    pos = pos_tag(text.split())
    tok = text.split()
    for i in range(len(tok)):
        if (tok[i].lower() in title_dict.keys()) and (pos[i+1][1]=='NNP'):
            tok[i] = title_dict[tok[i].lower()]
    return ' '.join(tok)

def convert_currency(text):
    # converts 20 dollars to $20
    for word, value in curr_to_symbol.items():
        regex = '\d+\s' + word + 's?'
        while True:
            match = re.search(regex, text, flags=re.IGNORECASE)
            if match is None:
                break
            start, end = match.start(), match.end()
            temp = text[start:end]
            temp = temp.split(' ')
            temp = ''.join([value, temp[0]])
            text = text[:start] + temp + text[end:]
    return text

def convert_repetitions(text):
    # converts double C to CC
    tok = text.split()
    i, l = 0, len(tok)
    while i<l:
        if (tok[i] in rep_dict.keys()) and (len(tok[i+1])==1):
            tok[i+1] = tok[i+1]*rep_dict[tok[i]]
            tok.pop(i)
            l -= 1
        i += 1
    return ' '.join(tok)

def convert():
    rec = sr.Recognizer()
    rec.energy_threshold = 1000
    with sr.Microphone() as source:
        print("Speak Something...")
        audio = rec.listen(source)
        print("Audio Recorded. Converting to text now...")

    try:
        text = rec.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not send the request. Please check your internet connection and try again; {e}")
    
    text = clean_text(text)
    text = convert_currency(text)
    text = convert_titles(text)
    text = convert_repetitions(text)
    return text