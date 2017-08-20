clear
sudo python /etc/ansible/user.py /etc/ansible/roles/ios/vars/main.yml
echo
echo "Now to run the playbook:"
echo
ansible-playbook /etc/ansible/ios.yml
echo
echo "Deleting username and password details...."
sudo rm /etc/ansible/roles/ios/vars/main.yml
echo
echo
