Example for calling Playbook from command line
----------------------------------------------

Example Sending Solution Manifest to LXCA
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 sol_id=1 manifest_path=/tmp/test.manifest" playbooks/uhm/manifests.yml -vvvv

Example Executung Compliance Validation in LXCA
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/uhm/compliance.yml  --tag gather_server_facts,validate_server_facts

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
List all  policy  
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag updatepolicy

Get List of Applicable Frimware policies
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 policy_info=FIRMWARE" playbooks/config/config.yml -vvvv --tag updatepolicy

List  the persisted compare result for servers to which a compliance policy is assigned
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 update_policy_info=RESULTS" playbooks/config/config.yml -vvvv --tag updatepolicy

Check compliant with the assigned compliance policy using the job or task ID that was returned when the compliance policy was assigned.  
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 update_policy_info=COMPARE_RESULTS uuid=EF362CF0FB4511E397AB40F2E9AF01D0 jobid=2" playbooks/config/config.yml -vvvv --tag updatepolicy

List all update policies
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag updatepolicy

Get List of Applicable Frimware policies
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 policy_info=FIRMWARE" playbooks/config/config.yml -vvvv --tag updatepolicy

Assign policy to Endpoint
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 policy_name=x220_imm2 policy_type=SERVER uuid=7C5E041E3CCA11E18B715CF3FC112D8A" playbooks/config/config.yml -vvvv --tag updatepolicy
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 jobid=16" playbooks/config/config.yml -vvvv --tag updatepolicy

Update Firmware commands
----------------

Query Updatable components
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag query_update_comp

Query Firmware Update Status
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag query_update_status

Applying Firmware with policy
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 mode=immediate action=apply server='7C5E041E3CCA11E18B715CF3FC112D8A,IMM2 (Primary)'" playbooks/config/config.yml -vvvv --tag update_firmware

Update Repostory commands
============
Querys
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=importDir" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=lastRefreshed" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=publicKeys" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=size" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=supportedMts" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=updates" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=updatesByMt" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 repo_key=updatesByMtByComp" playbooks/config/config.yml -vvvv --tag updaterepo

Action
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 action=read" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 action=refresh machine_type=7903" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 action=delete machine_type=7903 file_type=payloads fixids=ibm_fw_imm2_1aoo78j-6.20_anyos_noarch" playbooks/config/config.yml -vvvv --tag updaterepo

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 action=acquire machine_type=7903 scope=payloads fixids=ibm_fw_imm2_1aoo78j-6.20_anyos_noarch" playbooks/config/config.yml -vvvv --tag updaterepo


Config Profiles
============
get all profiles
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 " playbooks/config/config.yml -vvvv --tag configprofiles

get specified profile with id
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=69 " playbooks/config/config.yml -vvvv --tag configprofiles

Change profile name of id
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=69 name='changed name 3' " playbooks/config/config.yml -vvvv --tag configprofiles

Activate profile for endpoint
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=69 endpoint=B918EDCA1B5F11E2803EBECB82710ADE restart=immediate " playbooks/config/config.yml -vvvv --tag configprofiles

Unassign profile
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=69 action=unassign " playbooks/config/config.yml -vvvv --tag configprofiles

Delete profile
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=69 action=delete" playbooks/config/config.yml -vvvv --tag configprofiles


Config Patterns
============
Get All config patterns
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag configpatterns

Get specified config pattern with id
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=65" playbooks/config/config.yml -vvvv --tag configpatterns

Apply pattern to endpoint
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=65 endpoint=B918EDCA1B5F11E2803EBECB82710ADE restart=pending type=node" playbooks/config/config.yml -vvvv --tag configpatterns

Import SystemInfo pattern
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 pattern_update_dict={'template_type':'SystemInfo','template':{'contact':'contact','description':'Pattern created by test API ','location':'location','name':'Learned-System_Info-99','systemName':{'autogen':'Disable','hyphenChecked':False},'type':'SystemInfo','uri':'\/config\/template\/61','userDefined':True}}" playbooks/config/config.yml -vvvv --tag configpatterns

Import Pattern from file
------------------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 pattern_from_file=true" playbooks/config/config.yml -vvvv --tag configpatterns
