from sys import argv

import getpass

script, workfile = argv

f = open(workfile, 'w')

u = (raw_input("What is your username? "))
p = (getpass.getpass(prompt="What is your password? "))

x = '''
---

username: %s
password: %s
host: "{{ ios_cli_host | default(inventory_hostname) }}"

''' % (u, p)

z = str(x)

f.write(z)

f.close() 
