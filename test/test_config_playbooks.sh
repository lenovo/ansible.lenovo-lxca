rm -rf  playbooks/config/pylxca.log
ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=importDir" playbooks/config/config.yml -v --tag query_update_comp

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=lastRefreshed" playbooks/config/config.yml -v --tag query_update_status

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=publicKeys update_policy_info=RESULTS" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=importDir" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=lastRefreshed policy_info=FIRMWARE" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=publicKeys update_policy_info=RESULTS" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=importDir" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=lastRefreshed" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=publicKeys" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=size" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=supportedMts" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=updates" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=updatesByMt" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=updatesByMtByComp" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=updatesByMtByComp" playbooks/config/config.yml -v --tag configprofiles

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=updatesByMtByComp" playbooks/config/config.yml -v --tag get_configpatterns

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=updatesByMtByComp" playbooks/config/config.yml -v --tag get_configstatus

ansible-playbook -e "lxca_user=TEST lxca_password=Passw0rd lxca_url=https://10.240.29.217 repo_key=updatesByMtByComp" playbooks/config/config.yml -v --tag osimages

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','update_key':'importDir'}" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','update_key':'size'}" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','update_key':'updates'}" playbooks/config/config.yml -v --tag get_managementserver_pkg

grep -rni "error" playbooks/config/pylxca.log