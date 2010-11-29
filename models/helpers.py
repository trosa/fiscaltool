import urllib

def get_people(letter, venue):
	url = '''
	http://vestibular.ufrgs.br/cv2011/fiscais_coordenadores/Fiscais/fi2011_%s.htm''' % letter.upper()
	sock = urllib.urlopen(url)
	lines = []
	for line in sock.readlines():
		line = line.decode('windows-1252').encode('utf-8')
		if line[:3] == ' 00':
			linesp = line.split('  ')
			linesp = filter(lambda x: x!='', linesp)
			if linesp[2].strip() == str(venue):
				lines.append(linesp[1])
	
	return lines

def get_venues():
	url = 'http://www.vestibular.ufrgs.br/cv2011/fiscais_coordenadores/Fiscais/LOCA2011.HTM'
	sock = urllib.urlopen(url)
	lines = []
	for line in sock.readlines():
		if line[0] != '<':
			line = line.decode('windows-1252').encode('utf-8')
			lines.append(line[:40])
	return lines

