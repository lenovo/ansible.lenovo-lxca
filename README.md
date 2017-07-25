Example for calling Playbook from command line
----------------------------------------------

Example Sending Solution Manifest to LXCA
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 sol_id=1 manifest_path=/tmp/test.manifest" playbooks/uhm/manifests.yml -vvvv

Example Executung Compliance Validation in LXCA
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 server_uuid=AAA" playbooks/uhm/compliance.yml -vvvv --tag gather_server_facts

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 server_uuid=909145e6dc9411e4a97b6eae8b4bd9a3" playbooks/compliance.yml  --tag gather_server_facts

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 server_uuid=909145e6dc9411e4a97b6eae8b4bd9a3" property="machineType" condition="is_equal" ref_val="6241" playbooks/compliance.yml  --tag validate_server_facts

Example Collect inventory in LXCA
----------------

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv --tag users

Example Manage / Unmanage endpoint in LXCA
----------------

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 endpoint_ip=10.240.72.172 user=USERID password=CME44ibm recovery_password=CME55ibm force=True" playbooks/config/config.yml -vvvv --tag manage
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 endpoint_ip=10.240.72.172;46920C143355486F97C19A34ABC7D746;Chassis force=True" playbooks/config/config.yml -vvvv --tag unmanage

Example Update Operations in LXCA
============
Get List of policies
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag updatepolicy

Assign policy to Endpoint
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 update_policy_name=x220_imm2 update_policy_type=SERVER uuid=7C5E041E3CCA11E18B715CF3FC112D8A" playbooks/config/config.yml -vvvv --tag updatepolicy
