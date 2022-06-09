import random


class SimpleClass:

    index = 1

    def __init__(self, word="headphones", value=1):  # initializes parameters
        self.class_number = self.index
        self.__class__.index = self.index + 1  # it refers to the class attribute it was created in before init
        self.word = word
        self.value = value
        # self.value = self.random()
        self.list = [1, 0, 2]

    @staticmethod
    def random():
       return random.randint(0, 9)

    def change_to_random(self):
        number = self.random()  # when referring to a method or its parameter, we need to always precede it with self
        self.value = number

    def change_number(self, value=123):
        self.value = value

    def change_word(self, word="entertaining"):
        self.word = word

    def reverse(self):

        s = len(self.word)
        new_word = []  # an array of one-element strings
        while s != 0:
            new_word += self.word[s - 1]  # new_word.append(word[s - 1])
            s -= 1
        # print(new_word)
        self.word = ''.join(new_word)
        # creates a string from the list items that is in the argument of this method.
        # And what it is called on, an empty string "", is inserted between the list items to form a string

    def palindrome(self):

        for i in range(0, int(len(self.word) / 2)):
            if self.word[i] != self.word[len(self.word) - i - 1]:
                print(f"{self.word} it is not a palindrome")
                return False
        print(f"{self.word} is a palindrome")
        return True

    def write(self):
        return print(f'The number of the object {self.class_number} is {self.value} (using the method of a built-in class)')


def main():

    obj1 = SimpleClass("kajak", 40)
    obj2 = SimpleClass(value=15)

    print("This is Object 1")
    print(obj1.word, obj1.list)
    obj1.write()
    print('\n')

    print("This is Object 2")
    print(obj2.word)
    obj2.write()
    print('\n')

    print("Invoke a change_number on object 2 with no parameter")
    obj2.change_number()
    obj2.write()
    print('\n')

    print("Invoke a change_number on object 2 with parameter")
    obj2.change_number(321)
    obj2.write()
    print('\n')

    print(f'The word of object 2 is {obj2.word}')
    print('\n')

    print("Invoke a change_word on object 2 with no parameter")
    obj2.change_word()
    print(f'The word of object 2 is {obj2.word}')
    print('\n')

    print("Invoke a change_word on object 2 with parameter")
    obj2.change_word("book")
    print(f'The word of object 2 is {obj2.word}')
    print('\n')

    print("Invoke a change_to_random on object 1")
    obj1.change_to_random()
    obj1.write()
    print('\n')

    obj2.reverse()
    print(f'The reversed word of object 2 is {obj2.word}')
    print('\n')

    obj1.palindrome()


if __name__ == "__main__":
    main()
