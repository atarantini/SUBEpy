"""
SUBEpy is a small toolkit to work with Argentina's transport intelligent card
"""

def verify_card_number(nro):
	"""
	Verify if a given complete card number is correct
	"""
	if len(nro) is 16 and int(nro[-1]) is get_validator(nro[:-1]):
			return True
	return False

def get_validator(nro):
	"""
	Get validator digit for a card number
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

#
# main
#
nro = '6061267025125269' # random generated card number
print verify_card_number(nro)
