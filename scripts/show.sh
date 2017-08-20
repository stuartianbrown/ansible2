#!/bin/bash
clear
sudo python /etc/ansible/python/show.py /etc/ansible/roles/show/vars/main.yml /etc/ansible/hosts /etc/ansible/roles/show/tasks/main.yml
echo
echo
echo "Now to run the playbook:"
echo
ansible-playbook /etc/ansible/show.yml
echo
echo
echo -e "\033[1mDeleting username and password details....\033[0m"
#sudo rm /etc/ansible/roles/show/vars/main.yml
echo
echo
