class Wrappee:
    def print(self):
        pass


class PrintableString(Wrappee):
    def __init__(self, string: str):
        self._base = string

    def print(self):
        return self._base


class Decorator(Wrappee):
    def __init__(self, wrappee):
        self._wrappee = wrappee

    @property
    def wrappee(self):
        return self._wrappee

    def print(self):
        return self._wrappee.print()


class PostCommaDecorator(Decorator):
    def print(self):
        return self._wrappee.print() + ", "


class PostEndlDecorator(Decorator):
    def print(self):
        return self._wrappee.print() + "\n"


class PostExclaimDecorator(Decorator):
    def print(self):
        return self._wrappee.print() + "! "


class PostWordDecorator(Decorator):
    def __init__(self, wrappee: Wrappee, post_word):
        super().__init__(wrappee)
        self._post_word = post_word

    def print(self):
        return self._wrappee.print() + self._post_word


class PreWordDecorator(Decorator):
    def __init__(self, wrappee, pre_word):
        super().__init__(wrappee)
        self._pre_word = pre_word

    def print(self):
        return self._pre_word + self._wrappee.print()


custom_string = PrintableString("")
custom_string = PostWordDecorator(custom_string, "Hello")
custom_string = PostCommaDecorator(custom_string)
custom_string = PostWordDecorator(custom_string, "World")
custom_string = PostExclaimDecorator(custom_string)
custom_string = PostEndlDecorator(custom_string)

print(custom_string.print())
