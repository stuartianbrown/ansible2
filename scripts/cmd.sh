clear
echo
sudo python /etc/ansible/python/cmd.py /etc/ansible/roles/cmd/vars/main.yml /etc/ansible/hosts /etc/ansible/roles/cmd/tasks/main.yml
echo "Now to run the playbook:"
echo
ansible-playbook /etc/ansible/cmd.yml
echo
echo "Deleting username and password details...."
sudo rm /etc/ansible/roles/cmd/vars/main.yml
echo
echo
