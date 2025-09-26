#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value   # use setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")
            self._value = ""

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]+(?:\s|$)', self.value)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)

    def __str__(self):
        return self.value
