from sys import argv

script, varfile, hostfile = argv

v = open(varfile,'w')

import getpass

u = (raw_input("What is your username? "))
p = (getpass.getpass(prompt="What is your password? "))

x = '''
---

username: %s
password: %s
host: "{{ ios_cli_host | default(inventory_hostname) }}"
''' % (u, p)

v.write(x)

g = open(hostfile, 'w')

d = '''
[test2]'''

g.write(d)

m = int(raw_input("How many hosts would you grab the config from? "))

for z in xrange(1, m+1):
	h  = (raw_input("What is Host %s? " %(z)))
	l = '''
%s''' %(h)
	g.write(l)

g.close
v.close
