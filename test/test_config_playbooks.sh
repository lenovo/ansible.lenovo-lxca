rm -rf playbooks/config/pylxca.log

: "${LXCA_USER:?LXCA_USER must be set}"
: "${LXCA_PASSWORD:?LXCA_PASSWORD must be set}"
: "${LXCA_URL:?LXCA_URL must be set}"

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL repo_key=importDir" playbooks/config/config.yml -v --tag query_update_comp

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL repo_key=lastRefreshed" playbooks/config/config.yml -v --tag query_update_status

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=publicKeys update_policy_info=RESULTS" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=importDir" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=lastRefreshed policy_info=FIRMWARE" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=publicKeys update_policy_info=RESULTS" playbooks/config/config.yml -v --tag updatepolicy

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=importDir" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=lastRefreshed" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=publicKeys" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=size" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=supportedMts" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=updates" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=updatesByMt" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query repo_key=updatesByMtByComp" playbooks/config/config.yml -v --tag updaterepo

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=list" playbooks/config/config.yml -v --tag configprofiles

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=list" playbooks/config/config.yml -v --tag get_configpatterns

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query update_key=importDir" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query update_key=size" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=query update_key=updates" playbooks/config/config.yml -v --tag get_managementserver_pkg

ansible-playbook -e "lxca_user=$LXCA_USER lxca_password=$LXCA_PASSWORD lxca_url=$LXCA_URL subcmd=list" playbooks/config/config.yml -v --tag osimages

grep -rni "error" playbooks/config/pylxca.log
