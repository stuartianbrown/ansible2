clear
sudo python /etc/ansible/python/rancid.py /etc/ansible/roles/rancid/vars/main.yml /etc/ansible/hosts
echo
echo
echo "Now to run the playbook:"
echo
ansible-playbook /etc/ansible/rancid.yml
echo
echo
echo "Deleting username and password details...."
sudo rm /etc/ansible/roles/rancid/vars/main.yml
echo
echo
