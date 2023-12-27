import re


e = re.compile(r'(?: {2}|\t){1}(\w+)(?: ?= ?models.\w+\(){1}') 
while True:
    fields = []
    blank_lines = 2
    print('Paste your model class declaration, then press Enter. ')
    while blank_lines > 0:
        line = input()
        if line:
            m = e.search(line)
            if m:
                fields.append(m.group(1))
        else:
            if blank_lines <= 0:
                break
            blank_lines -= 1
    print('\nfields = ', fields)

    a = input('\nPress Enter to quit. \nTry again? ')
    if not a or a.strip().lower() in ('n', 'no', 'q', 'quit', 'exit', 'end', 'cancel'):
        break
