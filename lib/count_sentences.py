#!/usr/bin/env python3

# lib/count_sentences.py

import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # use setter for validation

    # VALUE property
    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    # METHODS
    def is_sentence(self):
        return bool(self.value) and self.value.endswith(".")

    def is_question(self):
        return bool(self.value) and self.value.endswith("?")

    def is_exclamation(self):
        return bool(self.value) and self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0
        # Use regex to split on punctuation that marks end of sentence
        sentences = re.split(r'[.!?]+', self.value)
        # Remove empty fragments (strip whitespace too)
        clean_sentences = [s for s in sentences if s.strip()]
        return len(clean_sentences)

