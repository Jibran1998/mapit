import webbrowser,sys

from prompt_toolkit.clipboard import pyperclip

address=sys.argv

if len(address)>1:
    address = ''.join(address[1:])
else:
    address=pyperclip.paste()

webbrowser.open(f"https://www.google.com/maps/place/{address}")
