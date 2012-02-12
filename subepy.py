"""
SUBEpy is a small toolkit to work with Argentina's transport intelligent card

Copyright 2011 Andres Tarantini (atarantini@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def verify_card_number(nro):
	"""
	Verify if a given complete card number is correct

	@param	String/Int	The 16 digit numbers of the card
	@return Bool		True if card is valid, false otherwise
	"""
	if type(nro) is not str: nro = str(int)
	if len(nro) is 16 and int(nro[-1]) is get_validator(nro[:-1]):
			return True
	return False

def get_validator(nro):
	"""
	Get validator digit for a card number

	@param	String	The 15 digit numbers of the card, without the validation digit
	@return Int		The validation digit
	"""
	nros = [int(n) for n in list(nro)]
	for i in range(len(nros)):
		if i % 2 == 0:
			if nros[i]*2 > 9:
				nros[i] = nros[i]*2 - 9
			else:
				nros[i] = nros[i]*2
	nrosum = sum(nros)
	if nrosum % 10 != 0:
		return 10 - nrosum % 10
	return 0

def random_card_number():
	from random import randint

	num = randint(100000000000000, 999999999999999)
	return str(num)+str(get_validator(str(num)))
