========
 SUBEpy
========

A small python toolkit to work with SUBE intelligent card systems

-------
 Usage
-------

Stand alone usage:

		$ python sube.py 1234567890123456

		1234567890123456 is NOT a valid card number

As a library in your code:

		import from subepy import verify_card_number


		card_number = '1234567890123456'

		print verify_card_number(card_number)

		# False

-------
 Notes
-------

This code is based on PHP code released at http://pastebin.com/9xrYNZK1 on Jan 27th 2012 by 'A guest' user.
