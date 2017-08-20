from sys import argv

script, varfile, hostfile, taskfile = argv

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

m = int(raw_input("How many hosts would you like to compare? "))

for z in xrange(1, m+1):
	h  = (raw_input("What is host %s? " %(z)))
	l = '''
%s''' %(h)
	g.write(l)
#	v.write(l)

g.close
v.close

f = open(taskfile, 'w')


k = '''
---
- ios_command:
    username: "{{ username }}"
    password: "{{ password }}"
    host: "{{ host }}"
    commands:
'''

f.write(k)

c = int(raw_input("How many 'show' commands would you like to run? "))

for x in xrange(0, c):
	y = (raw_input("Please type your full show command: "))
	w = '''
      - %s ''' %(y)

	f.write(w)

z = '''
  register: output

- name: show debug
  debug: var=output.stdout_lines
'''

f.write(z)

f.close
