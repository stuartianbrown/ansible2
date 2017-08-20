clear
sudo python /etc/ansible/user.py /etc/ansible/roles/temp/vars/main.yml
echo
echo "Now to run the playbook:"
echo
ansible-playbook /etc/ansible/temp.yml
echo
echo "Deleting username and password details...."
sudo rm /etc/ansible/roles/temp/vars/main.yml
echo
echo
