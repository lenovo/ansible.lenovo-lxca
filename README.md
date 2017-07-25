Example for calling Playbook from command line
----------------------------------------------

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" playbooks/cmms.yml -vvvv

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 sol_id=1 manifest_path=/tmp/test.manifest" playbooks/manifests.yml -vvvv

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv --tag users

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 server_uuid=AAA" playbooks/compliance.yml -vvvv --tag gather_server_facts

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 server_uuid=909145e6dc9411e4a97b6eae8b4bd9a3" playbooks/compliance.yml  --tag gather_server_facts

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 server_uuid=909145e6dc9411e4a97b6eae8b4bd9a3" property="machineType" condition="is_equal" ref_val="6241" playbooks/compliance.yml  --tag validate_server_facts

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 discovery_ip=10.240.72.172 manage_user=USERID manage_password=CME44ibm force=True" playbooks/config/config.yml -vvvv --tag manage

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 update_policy_name=x220_imm2 update_policy_type=SERVER uuid=7C5E041E3CCA11E18B715CF3FC112D8A" playbooks/config/config.yml -vvvv --tag updatepolicy
