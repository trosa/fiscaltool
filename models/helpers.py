import urllib

def get_people(letter, venue):
	url = '''
	http://vestibular.ufrgs.br/cv2011/fiscais_coordenadores/Fiscais/fi2011_%s.htm''' % letter.upper()
	print url
	sock = urllib.urlopen(url)
	lines = []
	for line in sock.readlines():
		if line[:3] == ' 00':
			linesp = line.split('  ')
			linesp = filter(lambda x: x!='', linesp)
			if linesp[2].strip() == str(venue):
				lines.append(linesp[1])
	
	return lines

