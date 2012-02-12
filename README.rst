========
 SUBEpy
========

A small python toolkit to work with SUBE intelligent card systems

-------
 Usage
-------

Stand alone usage:

`./sube.py 1234567890123456`

As a library in your code:

`
import from sube import verify_card_number

card_number = '1234567890123456'
print verify_card_number(card_number)	# should return True or False
`

-------
 Notes
-------

Based on the PHP code published in http://pastebin.com/9xrYNZK1
