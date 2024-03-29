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
import argparse

from subepy import verify_card_number

#
# main
#
if __name__ == '__main__':
	#parse command line arguments
	parser = argparse.ArgumentParser(description='SUBEpy can validate SUBE intelligent card numbers')
	parser.add_argument('number', type=str,  help='SUBE complete card number (16 digits)')
	args = parser.parse_args()
	number = args.number

	if verify_card_number(number):
		print str(number), 'is a VALID card number'
	else:
		print str(number), 'is NOT a valid card number'
