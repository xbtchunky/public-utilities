def wrap(s):
	return '\033[' + s + '95m'

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
	DARK_GREEN = wrap('32')
	DARK_RED = wrap('31')
	DARK_BLUE = wrap('34')
	DARK_PINK = wrap('35')
	DARK_GREY = wrap('36')
	RED_HIGHLIGHT = wrap('41')
	GREEN_HIGHLIGHT = wrap('42')
	BLUE_HIGHLIGHT = wrap('44')
	PINK_HIGHLIGHT = wrap('45')
	GREY_HIGHLIGHT = wrap('46')
	YELLOW = wrap('93')
	PINK = wrap('95')
	HIGHLIGHT = wrap('7')
	LIGHT_RED_HIGHLIGHT = wrap('101')
	LIGHT_GREEN_HIGHLIGHT = wrap('102')
	LIGHT_YELLOW_HIGHLIGHT = wrap('103')
	LIGHT_BLUE_HIGHLIGHT = wrap('104')
	LIGHT_PINK_HIGHLIGHT = wrap('105')
	CYAN_HIGHLIGHT = wrap('106')
	WHITE_HIGHLIGHT = wrap('107')

def dark_green_text(s):
	return bcolors.DARK_GREEN + str(s) + bcolors.ENDC
def dark_red_text(s):
	return bcolors.DARK_RED + str(s) + bcolors.ENDC
def dark_blue_text(s):
	return bcolors.DARK_BLUE + str(s) + bcolors.ENDC
def dark_pink_text(s):
	return bcolors.DARK_PINK + str(s) + bcolors.ENDC
def dark_grey_text(s):
	return bcolors.DARK_GREY + str(s) + bcolors.ENDC
def red_highlight_text(s):
	return bcolors.RED_HIGHLIGHT + str(s) + bcolors.ENDC
def green_highlight_text(s):
	return bcolors.GREEN_HIGHLIGHT + str(s) + bcolors.ENDC
def blue_highlight_text(s):
	return bcolors.BLUE_HIGHLIGHT + str(s) + bcolors.ENDC
def pink_highlight_text(s):
	return bcolors.PINK_HIGHLIGHT + str(s) + bcolors.ENDC
def grey_highlight_text(s):
	return bcolors.GREY_HIGHLIGHT + str(s) + bcolors.ENDC
def yellow_text(s):
	return bcolors.YELLOW + str(s) + bcolors.ENDC
def pink_text(s):
	return bcolors.PINK + str(s) + bcolors.ENDC
def highlight_text(s):
	return bcolors.HIGHLIGHT + str(s) + bcolors.ENDC
def light_red_highlight_text(s):
	return bcolors.LIGHT_RED_HIGHLIGHT + str(s) + bcolors.ENDC
def light_green_highlight_text(s):
	return bcolors.LIGHT_GREEN_HIGHLIGHT + str(s) + bcolors.ENDC
def light_yellow_highlight_text(s):
	return bcolors.LIGHT_YELLOW_HIGHLIGHT + str(s) + bcolors.ENDC
def light_blue_highlight_text(s):
	return bcolors.LIGHT_BLUE_HIGHLIGHT + str(s) + bcolors.ENDC
def light_pink_highlight_text(s):
	return bcolors.LIGHT_PINK_HIGHLIGHT + str(s) + bcolors.ENDC
def cyan_highlight_text(s):
	return bcolors.CYAN_HIGHLIGHT + str(s) + bcolors.ENDC
def white_highlight_text(s):
	return bcolors.WHITE_HIGHLIGHT + str(s) + bcolors.ENDC
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