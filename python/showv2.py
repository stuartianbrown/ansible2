from sys import argv

script, hostfile, taskfile = argv

hosts = open(hostfile, 'w')

hostnames = '''
[gns]'''

hosts.write(hostnames)

hostnumber = int(raw_input("How many hosts would you like to compare? "))

for z in xrange(1, hostnumber+1):
	h  = (raw_input("What is host {0}? ".format(z)))
	j = '''
{0}'''.format(h)
	hosts.write(j)

hosts.close

tasks = open(taskfile, 'w')


play = '''
---
- ios_command:
    provider: "{{ cli }}"
    commands:
'''

tasks.write(play)

commands = int(raw_input("How many 'show' commands would you like to run? "))

for x in xrange(0, commands):
	c = (raw_input("Please type your full show command: "))
	k = '''
      - {0} '''.format(c)

	tasks.write(k)

output = '''
  register: output

- name: show debug
  debug: var=output.stdout_lines
'''

tasks.write(output)

tasks.close
