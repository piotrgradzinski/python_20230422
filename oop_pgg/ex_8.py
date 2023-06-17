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
