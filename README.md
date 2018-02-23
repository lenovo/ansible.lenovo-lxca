# TODO  Documentation

### Example for calling LXCA Playbook

###### Manage / Unmanage endpoint
```
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.217 endpoint_ip=10.240.72.172 user=USERID password=CME44ibm recovery_password=CME55ibm force=True" playbooks/config/config.yml -vvvv --tag manage
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 endpoint_ip=10.240.72.172;46920C143355486F97C19A34ABC7D746;Chassis force=True" playbooks/config/config.yml -vvvv --tag unmanage
```

###### Collect inventory in LXCA
```
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220" site.yml -vvvv --tag users
```
###### Update Firmware
```
List all  policy  
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag updatepolicy

Get List of Applicable Frimware policies
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 policy_info=FIRMWARE" playbooks/config/config.yml -vvvv --tag updatepolicy

List  the persisted compare result for servers to which a policy is assigned
----------------

ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 update_policy_info=RESULTS" playbooks/config/config.yml -vvvv --tag updatepolicy

Check compliant with the assigned compliance policy using the job or task ID that was returned when the compliance policy was assigned.  
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 update_policy_info=COMPARE_RESULTS uuid=EF362CF0FB4511E397AB40F2E9AF01D0 jobid=2" playbooks/config/config.yml -vvvv --tag updatepolicy

Assign policy to Endpoint
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 policy_name=x220_imm2 policy_type=SERVER uuid=7C5E041E3CCA11E18B715CF3FC112D8A" playbooks/config/config.yml -vvvv --tag updatepolicy
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 jobid=16" playbooks/config/config.yml -vvvv --tag updatepolicy

Update endpoint Firmware
================

Query Updatable components
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag query_update_comp

Query Firmware Update Status
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220" playbooks/config/config.yml -vvvv --tag query_update_status

Applying Firmware with policy
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 mode=immediate action=apply server='7C5E041E3CCA11E18B715CF3FC112D8A,IMM2 (Primary)'" playbooks/config/config.yml -vvvv --tag update_firmware

Applying Firmware with policy for specified updateable components
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 mode=immediate action=apply uuid_list=['38D9D7DBCB713C12A210E60C74A0E931','00000000000010008000542AA2D3CB00']" playbooks/config/config.yml -vvvv --tag update_all_firmware_withpolicy

Applying Firmware with policy for all updateable components
----------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 mode=immediate action=apply uuid_list=[]" playbooks/config/config.yml -vvvv --tag update_all_firmware_withpolicy
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 mode=immediate action=apply" playbooks/config/config.yml -vvvv --tag update_all_firmware_withpolicy
Update Repostory commands
================
Queries
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
```

###### Config Profile operations
```
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
```

###### Config Patterns operations
```
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
Read config pattern data from config_pattern_import.yml file in vars folder of config
roles
ansible-playbook -e "lxca_user=TEST lxca_password=CME44ibm lxca_url=https://10.240.29.220 pattern_file=config_pattern_import.yml pattern_from_file=true" playbooks/config/config.yml -vvvv --tag import_configpatterns

config status
------------
get config status
ansible-playbook -e "lxca_user=USERID lxca_password=CME44ibm lxca_url=https://10.240.29.217 endpoint=B918EDCA1B5F11E2803EBECB82710ADE status=True" playbooks/config/config.yml -vvvv --tag get_configstatus
```

###### osimages operations
```
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
```

###### managementserver operations
```
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

```

###### Resource Group operations
```
Sending Solution Manifest to LXCA
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.220 sol_id=1 manifest_path=/tmp/test.manifest" playbooks/uhm/manifests.yml -vvvv

Create Resource Groups
----------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 name='TEST2' description='TestGroup' type='solution' solutionVPD={'id':'59A54997C18DCF0594A8CCD0','machineType':'TESTMTM','model':'TESTMODEL','serialNumber':'TESTSERIAL','manufacturer':'LENOVO'} members=[] criteria=[]" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups

Create Resource Groups extra_vars as JSON
---------------------------
ansible-playbook -e "{'lxca_user':'USERID', 'lxca_password':'Passw0rd', 'lxca_url':'https://10.240.29.217', 'name':'TEST3', 'description':'TestGroup', 'type':'solution', 'solutionVPD':{'id':'59A54997C18DCF0594A8CCD1','machineType':'TESTMTM','model':'TESTMODEL','serialNumber':'TESTSERIAL','manufacturer':'LENOVO'}, 'members':[], 'criteria':[]}" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups


Create Resource Groups extra_vars as JSON file
---------------------------
ansible-playbook -e "@files/resource_groups.json" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups
```

###### compliance rules operations
```
get all compliance rules
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/thinkagile.yml -vvvv --tag get_compliance_rules

get specific rule
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 id=5a2a2d8df9a2f31486aa8b83" playbooks/uhm/thinkagile.yml -vvvv --tag get_compliance_rules

import compliance rules from files of compliance_rules.yaml at uhm roles vars folder
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/thinkagile.yml -vvvv --tag import_compliance_rules

Get compositeResults
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/thinkagile.yml -vvvv --tag get_compositeResults
ansible-playbook -e "lxca_user=USERID lxca_password=CME44ibm lxca_url=https://10.243.13.182 query_solutionGroups=59A54997C18DCF0594B8CCD0" playbooks/uhm/thinkagile.yml -vvvv --tag query_solutionGroup_compositeResults

get specific compositeResults
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217 id=5a0eec085ababd3b02cc04a2" playbooks/uhm/thinkagile.yml -vvvv --tag get_compositeResults

update composit results
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=CME44ibm lxca_url=https://10.243.13.182 solutionGroups=5a0eec085ababd3b02cc04a2" playbooks/uhm/thinkagile.yml -vvvv --tag update_solutionGroup_compositeResults
ansible-playbook -e "lxca_user=USERID lxca_password=CME44ibm lxca_url=https://10.243.13.182 targetResources=[u'nodes/4C7D5FD237D411E2875EE4C686742121', u'nodes/1B247BCC918311E2B0703440B5EFBAB8' ]" playbooks/uhm/thinkagile.yml -vvvv --tag update_targetResources_compositeResults
ansible-playbook -e "lxca_user=USERID lxca_password=CME44ibm lxca_url=https://10.243.13.182 all_rules=True" playbooks/uhm/thinkagile.yml -vvvv --tag process_all_rules_compositeResults

Executing Compliance Validation in LXCA
-------------------
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" playbooks/uhm/compliance.yml  --tag gather_server_facts,validate_basic_server_facts -vvvv
ansible-playbook -e "plugin_name=test_plugin plugin_location=/home/prashant/git/ansible.lenovo-lxca/files/compliance_plugins" playbooks/uhm/compliance.yml  --tag validate_plugin_compliance -vvvv
ansible-playbook -e "lxca_user=USERID lxca_password=CME44ibm lxca_url=https://10.240.29.215 RESOURCE_UUID=AB6C2B0F827811E29C8B3440B5EAB968 RESOURCE_TYPE=Server BASIC_RULES=[{'property':'powerStatus','ref_value':8}]" playbooks/uhm/compliance.yml  --tag gather_server_facts,validate_basic_server_facts -vvvv

```

###### unittest cases
```
It uses mock and nose modules. For coverage it uses coverage module.
run unittest from root folder of this repo 

nosetests -v -s  test/test_pylxca_module.py
nosetests -v -s  test/test_pylxca_module.py --with-coverage
nosetests -v -s  test/test_pylxca_module.py --with-coverage --cover-package=pylxca
```
