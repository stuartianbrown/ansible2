#!/bin/bash
clear
sudo python /etc/ansible/python/showv2.py /etc/ansible/hosts /etc/ansible/roles/showv2/tasks/main.yml
echo "Now to run the playbook....."
ansible-playbook /etc/ansible/showv2.yml --ask-vault-pass

