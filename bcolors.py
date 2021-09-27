class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def blue_text(s):
	return bcolors.BLUE + str(s) + bcolors.ENDC

def cyan_text(s):
	return bcolors.CYAN + str(s) + bcolors.ENDC

def green_text(s):
	return bcolors.GREEN + str(s) + bcolors.ENDC

def red_text(s):
	return bcolors.FAIL + str(s) + bcolors.ENDC

def underlined_text(s):
	return bcolors.UNDERLINE + str(s) + bcolors.ENDC


def greenprint(s):
    print(bcolors.UNDERLINE + bcolors.GREEN + str(s) + bcolors.ENDC)

def failprint(s):
	print(bcolors.FAIL + bcolors.UNDERLINE + str(s) + bcolors.ENDC)

def colorprint(s, blue=False, cyan=False, green=False, warning=False, fail=False, underline=False, snip=False, red=False):
	s = str(s)

	color = ''
	if blue:
		color = bcolors.BLUE
	elif cyan:
		color = bcolors.CYAN
	elif green:
		color = bcolors.GREEN
	elif red:
		color = bcolors.FAIL

	extras = ''
	if warning:
		color += bcolors.WARNING
	if fail:
		color += bcolors.FAIL
	if underline:
		color += bcolors.UNDERLINE

	if snip:
		s = s[0:80] + ' ...'

	print(color + extras + s + bcolors.ENDC)