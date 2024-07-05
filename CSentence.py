from Cstring import Cstring


class CSentence:
    """
    A class to represent a sentence composed of multiple Cstring objects,
    mimicking an array of strings to construct sentences.

    Attributes:
        string (list[Cstring]): A list of Cstring objects representing words in a sentence.
    """
    '''
    c = Cstring(['h','e','l','l','o'])
    print(c.strstr(1, 4).string())
    '''

    def __init__(self, cstrings: list[Cstring] = None):
        """
        Initializes the CSentence with an optional list of Cstring objects.

        Args:
            cstrings (list[Cstring], optional): A list of Cstring objects that make up the sentence.
                                                Defaults to None, which will initialize an empty sentence.
        """
        # self.sentence = ''
        if cstrings is not None:
            self.cstrings = cstrings
        else:
            self.cstrings = [None]

    def get_sentence(self) -> str:
        """
        Constructs and returns the sentence as a concatenated string of words.

        Returns:
            str: The full sentence constructed from the Cstring objects,
                 where each word is separated by a space.
        """
        '''
        c = Cstring(['h','e','l','l','o'])
        print(c.string())
        '''
        my_string = ' '
        for i in self.cstrings:
            if i is not None:
                #my_string = ''.join(self.lst[:-1])
                my_string += i.string()
            my_string += ' '
        return my_string

'''
if __name__ == "__main__":
    c1 = Cstring(['h', 'e', 'l', 'l', 'o'])
    c2 = Cstring(['I', 'R', 'V', 'I', 'N', 'E'])
    c = CSentence([c1, c2])
    print(c.get_sentence())
#  print(c)
'''