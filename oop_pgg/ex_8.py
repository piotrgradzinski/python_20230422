"""
Implement classes responsible for creating documents in MarkDown syntax.
Create the `Element` base class containing the basic implementation of the `render()`
method and several of its derived classes (Header and Link).
Create the `Document` class to render the added elements.

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

Example of use:

UML: https://drive.google.com/file/d/1ZblDnt6xSjpuPfO-1dtnh8K09CwtuLMK/view

Example:
document = Document()
document.add_element(HeaderElement('Chapter 1'))
document.add_element(LinkElement('www.alx.pl', 'https://www.alx.pl'))
document.add_element(Element('To be or not to be'))
document.render()

Chapter 1
=========
[www.alx.pl](https://www.alx.pl)
To be or not to be
"""


class Element:
    def __init__(self, content: str):
        self._content = content

    def __str__(self):
        return f"{self._content}"

class HeaderElement(Element):
    def __str__(self):
        return f"{self._content}\n{'=' * len(self._content)}"

class LinkElement(Element):
    def __init__(self, content: str, url: str):
        super().__init__(content)
        self._url = url

    def __str__(self):
        return f"[{self._content}]({self._url})"

class Document:
    def __init__(self):
        self._elements = []

    def add_element(self, element: Element):
        self._elements.append(element)

    def __str__(self):
        return '\n'.join([str(element) for element in self._elements])

    def render(self):
        print(self.__str__())  # or print(self) or print(str(self))


document = Document()
document.add_element(HeaderElement('Chapter 1'))
document.add_element(LinkElement('www.alx.pl', 'https://www.alx.pl'))
document.add_element(Element('To be or not to be'))
document.render()