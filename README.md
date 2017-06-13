Example for calling Playbook from command line
----------------------------------------------

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" playbooks/cmms.yml -vvvv

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 sol_id=1 manifest_path=/tmp/test.manifest" playbooks/manifests.yml -vvvv

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv
