Implement a finite-state machine for morphological parsing. In this example, we'll create a simple machine to generate plural forms of English nouns using python.

PROGRAM :-

import inflect

def generate_plural(singular_noun):
    p = inflect.engine()
    return p.plural(singular_noun)

if __name__ == "__main__":
     
    singular_nouns = ['cat', 'dog', 'book', 'city', 'country', 'apple']
    for singular_noun in singular_nouns:
        plural_form = generate_plural(singular_noun)
        print(f"The plural of {singular_noun} is {plural_form}")


