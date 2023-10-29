#!/usr/bin/python3
"""Module for 5-text_indentation
"""

def text_indentation(text):
    """function that prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(string): Text to be indented

    Raises:
    TypeError: if "text" is not a string

    Example:
    >>>text_indentation("Hello Courage. Are you certain?")
    Hello Courage.
    <BLANKLINE>
    Are you certain?
    <BLANKLINE>
    """

if not isinstance(text, string):
    raise TypeError("text must be a string")


for special_char('.', '?', ':'):
    text = (special_char + ('\n' * 2)).join(
                [line.lstrip(' ') for line in text.split(special_char)]
                )

    #Print new string
    print("{}".format(text), end='')
