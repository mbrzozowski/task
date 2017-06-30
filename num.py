import inflect
import sys


def number_to_text(num):
    if not num:
        return ''
    engine = inflect.engine()
    txt = engine.number_to_words(num)
    return txt.replace('-', ' ').replace(',', '').capitalize()

if __name__ == '__main__':
    for line in sys.stdin:
        if line == '\n':
            print ''
        else:
            print number_to_text(line)
