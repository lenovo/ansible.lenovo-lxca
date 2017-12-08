Example for calling Playbook from command line
----------------------------------------------

Example Sending Solution Manifest to LXCA
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 sol_id=1 manifest_path=/tmp/test.manifest" playbooks/uhm/manifests.yml -vvvv

Example Executung Compliance Validation in LXCA
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/compliance.yml  --tag gather_server_facts,validate_basic_server_facts -vvvv
ansible-playbook -e "plugin_name=test_plugin plugin_location=/home/prashant/git/ansible.lenovo-lxca/files/compliance_plugins" playbooks/uhm/compliance.yml  --tag validate_plugin_compliance -vvvv

Example Collect inventory in LXCA
----------------

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv

ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv --tag users

Example Manage / Unmanage endpoint in LXCA
----------------

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.217 endpoint_ip=10.240.72.172 user=USERID password=CME44ibm recovery_password=CME55ibm force=True" playbooks/config/config.yml -vvvv --tag manage
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
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/config/config.yml -vvvv --tag get_configpatterns

Get specified config pattern with id
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 id=52" playbooks/config/config.yml -vvvv --tag get_particular_configpattern

Get specified config pattern for id with includeSettings
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 id=52 includeSettings=True" playbooks/config/config.yml -vvvv --tag get_particular_configpattern

Apply pattern to endpoint
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 id=65 endpoint=B918EDCA1B5F11E2803EBECB82710ADE restart=pending type=node" playbooks/config/config.yml -vvvv --tag apply_configpatterns
using name
----------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 name=From_abcdef endpoint=B918EDCA1B5F11E2803EBECB82710ADE restart=pending type=node" playbooks/config/config.yml -vvvv --tag apply_configpatterns
Import SystemInfo pattern
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 pattern_update_dict={'template_type':'SystemInfo','template':{'contact':'contact','description':'Pattern created by test API ','location':'location','name':'Learned-System_Info-99','systemName':{'autogen':'Disable','hyphenChecked':False},'type':'SystemInfo','uri':'\/config\/template\/61','userDefined':True}}" playbooks/config/config.yml -vvvv --tag import_configpatterns

Import Pattern from file
------------------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 pattern_from_file=true" playbooks/config/config.yml -vvvv --tag import_configpatterns

Create Resource Groups
----------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 name='TEST2' description='TestGroup' type='solution' solutionVPD={'id':'59A54997C18DCF0594A8CCD0','machineType':'TESTMTM','model':'TESTMODEL','serialNumber':'TESTSERIAL','manufacturer':'LENOVO'} members=[] criteria=[]" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups

Create Resource Groups extra_vars as JSON
---------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217', 'name':'TEST3', 'description':'TestGroup', 'type':'solution', 'solutionVPD':{'id':'59A54997C18DCF0594A8CCD1','machineType':'TESTMTM','model':'TESTMODEL','serialNumber':'TESTSERIAL','manufacturer':'LENOVO'}, 'members':[], 'criteria':[]}" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups


Create Resource Groups extra_vars as JSON file
---------------------------
ansible-playbook -e "@files/resource_groups.json" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups

osimages
==========
get all osimages
-----------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217'}" playbooks/config/config.yml -vvvv --tag osimages

get globalSetting for osimages
-----------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','osimages_info':'globalSettings'}" playbooks/config/config.yml -vvvv --tag osimages

import osimage file from remote server
-------------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217', 'osimages_imagetype_dict':{'imageType':'OS'}, 'import_dict':{'imageType':'OS','os':'rhels','imageName':'fixed','path':'iso/rhel73.iso','serverId':'1'}}" playbooks/config/config.yml -vvvv --tag import_osimages

get hostplatforms detail for osimages
------------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','osimages_info':'hostPlatforms'}" playbooks/config/config.yml -vvvv --tag osimages


deploy osimage to node
----------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','osimages_info':'hostPlatforms','osimages_dict':{'networkSettings':{'dns1': '10.240.0.10','dns2':'10.240.0.11','gateway':'10.240.28.1','ipAddress':'10.240.29.226','mtu':1500,'prefixLength':64,'selectedMac':'AUTO','subnetMask':'255.255.252.0','vlanId':521},'selectedImage':'rhels7.3|rhels7.3-x86_64-install-Minimal','storageSettings':{'targetDevice':'localdisk'},'uuid':'B918EDCA1B5F11E2803EBECB82710ADE'}}" playbooks/config/config.yml -vvvv --tag osimages

get all remoteFileServers
-------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','osimages_info':'remoteFileServers'}" playbooks/config/config.yml -vvvv --tag osimages

Get Specific remoteFileServers
------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','osimages_info':'remoteFileServers', 'osimages_dict':{'id':'1'}}" playbooks/config/config.yml -vvvv --tag osimages

Delete Specific Remote File Server
---------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','osimages_info':'remoteFileServers', 'osimages_dict':{'deleteid':'2'}}" playbooks/config/config.yml -vvvv --tag osimages

Add Remote File Server
----------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','osimages_info':'remoteFileServers', 'osimages_dict':{'displayName':'TEST99','address': '192.168.1.10','keyPassphrase': 'Passw0rd','keyType': 'RSA-2048','port': 8080,'protocol': 'HTTPS'}}" playbooks/config/config.yml -vvvv --tag osimages


managementserver
================
get managementserver with different key options
-----------------------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','update_key':'importDir'}" playbooks/config/config.yml -vvvv --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','update_key':'size'}" playbooks/config/config.yml -vvvv --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','update_key':'updates'}" playbooks/config/config.yml -vvvv --tag get_managementserver_pkg

get particular details with fixids
----------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','update_key':'filetypes', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch'}" playbooks/config/config.yml -vvvv --tag get_particular_managementserver_pkg

nsible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch','type':'readme'}" playbooks/config/config.yml -vvvv --tag get_particular_managementserver_pkg


Update options for managementserver
----------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217', 'action':'refresh'}" playbooks/config/config.yml -vvvv --tag update_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch','action':'acquire'}" playbooks/config/config.yml -vvvv --tag update_managementserver_pkg

ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch','action':'delete'}" playbooks/config/config.yml -vvvv --tag update_managementserver_pkg

Import local files to managementserver
--------------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','action':'import', 'files':'/home/naval/updates/updates/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.txt,/home/naval/updates/updates/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.chg,/home/naval/updates/updates/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.xml'}" playbooks/config/config.yml -vvvv --tag import_managementserver_pkg

files specified with relative to playbook file
----------------------------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217','action':'import', 'files':'../../files/updates/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.xml'}" playbooks/config/config.yml -vvvv --tag import_managementserver_pkg


compliance rules
-----------------
get all compliance rules
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/thinkagile.yml -vvvv --tag get_compliance_rules

get specific rule
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 id=5a2a2d8df9a2f31486aa8b83" playbooks/uhm/thinkagile.yml -vvvv --tag get_compliance_rules

import compliance rules from files of compliance_rules.yaml at uhm roles vars folder
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/thinkagile.yml -vvvv --tag import_compliance_rules

Get compositeResults
--------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/thinkagile.yml -vvvv --tag get_compositeResults

get specific compositeResults
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 id=5a0eec085ababd3b02cc04a2" playbooks/uhm/thinkagile.yml -vvvv --tag get_compositeResults

update composit results
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 solutionGroup=5a0eec085ababd3b02cc04a2" playbooks/uhm/thinkagile.yml -vvvv --tag update_compositeResults



unittest
--------

It uses mock and nose modules. For coverage it uses coverage module.
run unittest from root folder of this repo 

nosetests -v -s  test/test_pylxca_module.py
nosetests -v -s  test/test_pylxca_module.py --with-coverage
nosetests -v -s  test/test_pylxca_module.py --with-coverage --cover-package=pylxca

