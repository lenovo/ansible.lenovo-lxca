rm -rf  playbooks/config/pylxca.log
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 repo_key=importDir" playbooks/config/config.yml -v --tag query_update_comp

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 repo_key=lastRefreshed" playbooks/config/config.yml -v --tag query_update_status

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=publicKeys update_policy_info=RESULTS" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=importDir" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=lastRefreshed policy_info=FIRMWARE" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=publicKeys update_policy_info=RESULTS" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=importDir" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=lastRefreshed" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=publicKeys" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=size" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=supportedMts" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=updates" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=updatesByMt" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=query repo_key=updatesByMtByComp" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=list" playbooks/config/config.yml -v --tag configprofiles

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=list" playbooks/config/config.yml -v --tag get_configpatterns

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.197.119', 'subcmd':'query', 'update_key':'importDir'}" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.197.119', 'subcmd':'query', 'update_key':'size'}" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.197.119', 'subcmd':'query', 'update_key':'updates'}" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.197.119 subcmd=list" playbooks/config/config.yml -v --tag osimages

grep -rni "error" playbooks/config/pylxca.log
