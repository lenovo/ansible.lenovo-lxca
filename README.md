
Lenovo Ansible 
--------------
This project contains Ansible Playbooks, Roles and Modules for LXCA and can be used collectively to implement various use cases.
Project cotains following Ansible Roles
- Inventory : Role to get all inventory from LXCA. 
- Configuration i: Role to do config operation, firmware update, apply patterns, os deploy.

Dependencies
------------
 -python3 version 3.10.4
 -pip version 22.0.2
 -ansible [core 2.12.5]

Installation
------------
ansible-galaxy install lenovo.lxca-inventory
ansible-galaxy install lenovo.lxca-config

Pre-requisite
Ansible Role requires LXCA Python Client and LXCA Ansible module installed.

### Example for calling LXCA Playbook
###### Stored Credentials
```
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL " playbooks/config/config.yml -vvvv --tag get_all_storedcredentials
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL storedcredential_id=402" playbooks/config/config.yml -vvvv --tag get_particular_storedcredentials
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL description='desc of user' user=USER password=PASSWORD" playbooks/config/config.yml -vvvv --tag create_storedcredentials
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL storedcredential_id=412 user=USER password=PASSWORD" playbooks/config/config.yml -vvvv --tag update_storedcredentials
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL storedcredential_id=407" playbooks/config/config.yml -vvvv --tag delete_particular_storedcredentials

```


###### Manage / Unmanage endpoint
```
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL endpoint_ip=ENDPOINT_IP user=USER password=PASSWORD recovery_password=RECOVERY_PASSWORD force=True" playbooks/config/config.yml -vvvv --tag manage
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL endpoint_ip=ENDPOINT_IP storedcredential_id=STORED_CREDENTIAL_ID force=True" playbooks/config/config.yml -vvvv --tag
manage
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL endpoint_ip=ENDPOINT_IP;UUID;Chassis force=True" playbooks/config/config.yml -v --tag unmanage
```

###### Collect inventory in LXCA
```
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" site.yml -vvvv
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" site.yml -vvvv --tag users
```
###### Update Firmware
```
List all  policy  
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=list" playbooks/config/config.yml -vvvv --tag updatepolicy

Get List of Applicable Frimware policies
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query policy_info=FIRMWARE" playbooks/config/config.yml -vvvv --tag updatepolicy

List  the persisted compare result for servers to which a policy is assigned
----------------

ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query update_policy_info=RESULTS" playbooks/config/config.yml -vvvv --tag updatepolicy

Check compliant with the assigned compliance policy using the job or task ID that was returned when the compliance policy was assigned.  
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=status uuid=EF362CF0FB4511E397AB40F2E9AF01D0 jobid=2" playbooks/config/config.yml -vvvv --tag updatepolicy

Assign policy to Endpoint
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=assign policy_name=x220_imm2 policy_type=SERVER uuid=UUID" playbooks/config/config.yml -vvvv --tag updatepolicy
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=status jobid=16" playbooks/config/config.yml -vvvv --tag updatepolicy

Update endpoint Firmware
================

Query Updatable components
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" playbooks/config/config.yml -v --tag query_update_comp

Query Firmware Update Status
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" playbooks/config/config.yml -vvvv --tag query_update_status

Applying Firmware with policy
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL mode=immediate lxca_action=apply server='UUID,IMM2 (Primary)'" playbooks/config/config.yml -vvvv --tag update_firmware

Applying Firmware with policy for specified updateable components
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL mode=immediate lxca_action=apply uuid_list=['UUID1','UUID2']" playbooks/config/config.yml -vvvv --tag update_all_firmware_withpolicy

Applying Firmware with policy for all updateable components
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL mode=immediate lxca_action=apply uuid_list=[]" playbooks/config/config.yml -vvvv --tag update_all_firmware_withpolicy
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL mode=immediate lxca_action=apply" playbooks/config/config.yml -vvvv --tag update_all_firmware_withpolicy

Update Repostory commands
================
Queries
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=importDir" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=lastRefreshed" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=publicKeys" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=size" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=supportedMts" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=updates" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=updatesByMt" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=query repo_key=updatesByMtByComp" playbooks/config/config.yml -vvvv --tag updaterepo

Action
----------------
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=read lxca_action=read" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=refresh lxca_action=refresh machine_type=7903" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=delete lxca_action=delete machine_type=7903 file_type=payloads fixids=ibm_fw_imm2_1aoo78j-6.20_anyos_noarch" playbooks/config/config.yml -vvvv --tag updaterepo
ansible-playbook -e "lxca_user=TEST lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=acquire lxca_action=acquire machine_type=7903 scope=payloads fixids=ibm_fw_imm2_1aoo78j-6.20_anyos_noarch" playbooks/config/config.yml -vvvv --tag updaterepo
```

###### Config Profile operations
```
get all profiles
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=list" playbooks/config/config.yml -v --tag configprofiles

get specified profile with id
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL  subcmd=list id=69 " playbooks/config/config.yml -vvvv --tag configprofiles

Change profile name of id
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=rename id=69 config_profile_name='changed name 3' " playbooks/config/config.yml -vvvv --tag configprofiles

Activate profile for endpoint
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=activate id=69 endpoint=UUID restart=immediate " playbooks/config/config.yml -vvvv --tag configprofiles

Unassign profile
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL subcmd=unassign id=69" playbooks/config/config.yml -vvvv --tag configprofiles

Delete profile
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL id=69 subcmd=delete" playbooks/config/config.yml -vvvv --tag configprofiles
```

###### Config Patterns operations
```
Get All config patterns
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" playbooks/config/config.yml -vvvv --tag get_configpatterns

Get specified config pattern with id
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL id=52" playbooks/config/config.yml -vvvv --tag get_particular_configpattern

Get specified config pattern for id with includeSettings
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL id=52 includeSettings=True" playbooks/config/config.yml -vvvv --tag get_particular_configpattern

Apply pattern to endpoint
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL id=65 endpoint=UUID restart=pending type=node" playbooks/config/config.yml -vvvv --tag apply_configpatterns
using name
----------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL config_pattern_name=From_abcdef endpoint=UUID restart=pending type=node" playbooks/config/config.yml -vvvv --tag apply_configpatterns
Import SystemInfo pattern
----------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL pattern_update_dict={'template_type':'SystemInfo','template':{'contact':'contact','description':'Pattern created by test API ','location':'location','name':'Learned-System_Info-99','systemName':{'autogen':'Disable','hyphenChecked':False},'type':'SystemInfo','uri':'\/config\/template\/61','userDefined':True}}" playbooks/config/config.yml -vvvv --tag import_configpatterns

Import Pattern from file
------------------------
Read config pattern data from config_pattern_import.yml file in vars folder of config
roles
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL pattern_file=config_pattern_import.yml pattern_from_file=true" playbooks/config/config.yml -vvvv --tag import_configpatterns

config status
------------
get config status
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL endpoint=UUID" playbooks/config/config.yml -vvvv --tag get_configstatus
```

###### osimages operations
```
get all osimages
-----------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'subcmd':'list'}" playbooks/config/config.yml -v --tag osimages

delete  osimages with id
-----------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'delete','id':'20190227190109_trail.py'}" playbooks/config/config.yml -vvvv --tag osimages

get globalSetting for osimages
-----------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'globalsettings'}" playbooks/config/config.yml -vvvv --tag osimages

set globalSetting for osimages
-----------------
for setting globalSetting get detail from get golbalSetting and change the
parameter you want to change. This example set LINUX default password.
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'subcmd':'globalsettings', 'osimages_dict':{'activeDirectory':{'allDomains': [],'defaultDomain':None}, 'credentials':[{'name': 'root', 'password':'Test1234', 'passwordChanged':True, 'type': 'LINUX'}, {'type': "WINDOWS", 'name': 'Administrator', password: None, 'passwordChanged': False}],'ipAssignment':'dhcpv4', 'isVLANMode': 'false', 'licenseKeys': {'win2012r1': {'dataCenterLicenseKey': '','standardLicenseKey': '',},'win2012r2':{'dataCenterLicenseKey': '', 'standardLicenseKey': ''}, 'win2016r1': {'dataCenterLicenseKey': '', 'standardLicenseKey': ''}, 'win2019r1': {'dataCenterLicenseKey': '','standardLicenseKey': ''}}}}" playbooks/config/config.yml -vvvv --tag osimages

get hostSetting for osimages
-----------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'hostsettings'}" playbooks/config/config.yml -vvvv --tag osimages

create hostSetting for osimages
-----------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'hostsettings', 'osimages_dict':{\"action\": \"create\", \"hosts\": [{\"storageSettings\": {\"targetDevice\": \"localdisk\"}, \"uuid\": \"UUID\", \"networkSettings\": {\"dns2\": \"\", \"dns1\": \"DNS1\", \"hostname\": \"nodeundefined\", \"vlanId\": 0, \"selectedMAC\": \"AUTO\", \"gateway\": \"GATEWAY_IP\", \"subnetMask\": \"255.255.240.0\", \"mtu\": 1500, \"prefixLength\": 64, \"ipAddress\": \"10.243.9.79\"}}, {\"storageSettings\": {\"targetDevice\": \"localdisk\"}, \"uuid\": \"UUID\", \"networkSettings\": {\"dns2\": \"\", \"dns1\": \"DNS1\", \"hostname\": \"proton1\", \"vlanId\": 0, \"selectedMAC\": \"AUTO\", \"gateway\": \"GATEWAY_IP\", \"subnetMask\": \"255.255.240.0\", \"mtu\": 1500, \"prefixLength\": 64, \"ipAddress\": \"IP_ADDRESS\"}}]}}" playbooks/config/config.yml -vvvv --tag osimages


update hostSetting for osimages
-----------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'hostsettings', 'osimages_dict':{'action': 'update', 'hosts': [{'storageSettings': {'targetDevice': 'localdisk'}, 'uuid': 'UUID', 'networkSettings': {'dns2': '', 'dns1': 'DNS1', 'hostname': 'nodeundefined', 'vlanId': 0, 'selectedMAC': 'AUTO', 'gateway': 'GATEWAY_IP', 'subnetMask': '255.255.240.0', 'mt': 1500, 'prefixLength': 64, 'ipAddress': '10.243.9.79'}}, {'storageSettings': {'targetDevice': 'localdisk'}, 'uuid': 'UUID', 'networkSettings': {'dns2': '', 'dns1': 'DNS1', 'hostname': 'proton1', 'vlanId': 0, 'selectedMAC': 'AUTO', 'gateway': 'GATEWAY_IP', 'subnetMask': '255.255.240.0', 'mt': 1500, 'prefixLength': 64, 'ipAddress': 'IP_ADDRESS'}}]}}" playbooks/config/config.yml -vvvv --tag osimages


delete hostSetting for osimages
-----------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'hostsettings', 'osimages_dict':{'action': 'delete', 'uuid': 'UUID'}}" playbooks/config/config.yml -vvvv --tag osimages

import osimage file from remote server
-------------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'osimages_imagetype_dict':{'imageType':'OS'}, 'import_dict':{'imageType':'OS','os':'rhels','imageName':'fixed','path':'iso/rhel73.iso','serverId':'1'}}" playbooks/config/config.yml -vvvv --tag import_osimages


import osimage script file from local
-------------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'osimages_imagetype_dict':{'imageType':'SCRIPT'}, 'import_dict':{'imageType':'SCRIPT', "imageName":"trail.py", "os":"rhels", "description":"test_python_file", "file": "/home/naval/trail.py" }}" playbooks/config/config.yml -vvvv --tag import_osimages

get hostplatforms detail for osimages
------------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'hostplatforms'}" playbooks/config/config.yml -vvvv --tag osimages

deploy osimage to node
----------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'hostplatforms','osimages_dict':{'networkSettings':{'dns1': 'DNS1','dns2':'10.240.0.11','gateway':'10.240.28.1','ipAddress':'10.240.29.226','mtu':1500,'prefixLength':64,'selectedMac':'AUTO','subnetMask':'255.255.252.0','vlanId':521},'selectedImage':'rhels7.3|rhels7.3-x86_64-install-Minimal','storageSettings':{'targetDevice':'localdisk'},'uuid':'UUID'}}" playbooks/config/config.yml -vvvv --tag osimages

get all remoteFileServers
-------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'remotefileservers'}" playbooks/config/config.yml -vvvv --tag osimages

Get Specific remoteFileServers
------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'remotefileservers', 'osimages_dict':{'id':'1'}}" playbooks/config/config.yml -vvvv --tag osimages

Delete Specific Remote File Server
---------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'remotefileservers', 'osimages_dict':{'deleteid':'2'}}" playbooks/config/config.yml -vvvv --tag osimages

Add Remote File Server
----------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'remotefileservers', 'osimages_dict':{'displayName':'TEST99','address': '192.168.1.10','keyPassphrase': 'KEY_PASSPHRASE','keyType': 'RSA-2048','port': 8080,'protocol': 'HTTPS'}}" playbooks/config/config.yml -vvvv --tag osimages
```

###### managementserver operations
```
get managementserver with different key options
-----------------------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'subcmd':'query', 'update_key':'importDir'}" playbooks/config/config.yml -vvvv --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'subcmd':'query', 'update_key':'size'}" playbooks/config/config.yml -vvvv --tag get_managementserver_pkg

ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'subcmd':'query', 'update_key':'updates'}" playbooks/config/config.yml -vvvv --tag get_managementserver_pkg

get particular details with fixids
----------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'subcmd':'query_fixids', 'update_key':'filetypes', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch'}" playbooks/config/config.yml -vvvv --tag get_particular_managementserver_pkg

nsible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL',  'subcmd':'query_fixids', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch','type':'readme'}" playbooks/config/config.yml -vvvv --tag get_particular_managementserver_pkg

Update options for managementserver
----------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'subcmd':'refresh'}" playbooks/config/config.yml -vvvv --tag update_managementserver_pkg

ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch','subcmd':'acquire'}" playbooks/config/config.yml -vvvv --tag update_managementserver_pkg

ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch','subcmd':'apply'}" playbooks/config/config.yml -vvvv --tag update_managementserver_pkg

ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'fixids':'lnvgy_sw_lxca-fw-repository-pack_1-1.0.1_anyos_noarch','subcmd':'delete'}" playbooks/config/config.yml -vvvv --tag update_managementserver_pkg

Import local files to managementserver
--------------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'import', 'files':'/path/to/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.txt,/path/to/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.chg,/path/to/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.xml'}" playbooks/config/config.yml -vvvv --tag import_managementserver_pkg

files specified with relative to playbook file
----------------------------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL','subcmd':'import', 'files':'/path/to/lnvgy_sw_lxca_thinksystemrepo1-1.3.2_anyos_noarch.xml'}" playbooks/config/config.yml -vvvv --tag import_managementserver_pkg

```

###### Resource Group operations
```
Sending Solution Manifest to LXCA
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL sol_id=1 manifest_path=/tmp/test.manifest" playbooks/uhm/manifests.yml -vvvv

Create Resource Groups
----------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL resource_group_name='TEST2' description='TestGroup' resource_type='solution' solutionVPD={'id':'ID','machineType':'TESTMTM','model':'TESTMODEL','serialNumber':'TESTSERIAL','manufacturer':'LENOVO'} members=[] criteria=[]" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups

Create Resource Groups extra_vars as JSON
---------------------------
ansible-playbook -e "{'lxca_user':'LXCA_USER', 'lxca_password':'LXCA_PASSWORD', 'lxca_url':'LXCA_URL', 'resource_group_name':'TEST3', 'description':'TestGroup', 'resource_type':'solution', 'solutionVPD':{'id':'ID','machineType':'TESTMTM','model':'TESTMODEL','serialNumber':'TESTSERIAL','manufacturer':'LENOVO'}, 'members':[], 'criteria':[]}" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups

Create dynamic resource group
------------------------------
ansible-playbook -e '{"lxca_user":"LXCA_USER", "lxca_password":"LXCA_PASSWORD", "lxca_url":"LXCA_URL", "resource_group_name":"TEST3", "description":"TestGroup", "resource_type":"dynamic",  "criteria":{"parent":"root", "value":None, "criteria":[{"operator":"contains","value":"test", "property":"hostname", "id":"1001", "parent":"lxca_customUI_resourceViews_allGroupsPage_editGroupDynamicPage_2"}], "operator":"AND", "property": None, "id":"root"}}' playbooks/uhm/thinkagile.yml -vvvv --tag create_dynamic_resourcegroups

Create Resource Groups extra_vars as JSON file
---------------------------
ansible-playbook -e "@files/resource_groups.json" playbooks/uhm/thinkagile.yml -vvvv --tag create_resourcegroups

Add Resource Groups members
---------------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL uuid=ID members=['nodes/9C4D0000B22E44F1A0000A1D85B4ECD0','switches/38D9D7DBCB713C12A210E60C74A0E931']" playbooks/uhm/thinkagile.yml -vvvv --tag add_group_members

Get all Resource Groups
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL " playbooks/uhm/thinkagile.yml -vvvv --tag get_resourcegroups

Get specific Resource Groups
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL uuid=ID" playbooks/uhm/thinkagile.yml -vvvv --tag get_resourcegroups

```
###### compliance rules operations
```
get all compliance rules
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" playbooks/uhm/thinkagile.yml -vvvv --tag get_compliance_rules

get specific rule
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL id=5a2a2d8df9a2f31486aa8b83" playbooks/uhm/thinkagile.yml -vvvv --tag get_compliance_rules

import compliance rules from files of compliance_rules.yaml at uhm roles vars folder
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" playbooks/uhm/thinkagile.yml -vvvv --tag import_compliance_rules

Get compositeResults
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" playbooks/uhm/thinkagile.yml -vvvv --tag get_compositeresults

get specific compositeResults
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL id=5a0eec085ababd3b02cc04a2" playbooks/uhm/thinkagile.yml -vvvv --tag get_compositeresults

update composit results
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL solutionGroups=5a0eec085ababd3b02cc04a2" playbooks/uhm/thinkagile.yml -vvvv --tag update_solutiongroup_compositeresults
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL targetResources=[u'nodes/4C7D5FD237D411E2875EE4C686742121', u'nodes/1B247BCC918311E2B0703440B5EFBAB8' ]" playbooks/uhm/thinkagile.yml -vvvv --tag update_targetresources_compositeresults
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL all_rules=True" playbooks/uhm/thinkagile.yml -vvvv --tag process_all_rules_compositeresults

Executing Compliance Validation in LXCA
-------------------
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL" playbooks/uhm/compliance.yml  --tag gather_server_facts,validate_basic_server_facts -vvvv
ansible-playbook -e "plugin_name=test_plugin plugin_location=/home/prashant/git/ansible.lenovo-lxca/files/compliance_plugins" playbooks/uhm/compliance.yml  --tag validate_plugin_compliance -vvvv
ansible-playbook -e "lxca_user=LXCA_USER lxca_password=LXCA_PASSWORD lxca_url=LXCA_URL RESOURCE_UUID=RESOURCE_UUID RESOURCE_TYPE=Server BASIC_RULES=[{'property':'powerStatus','ref_value':8}]" playbooks/uhm/compliance.yml  --tag gather_server_facts,validate_basic_server_facts -vvvv

```

###### unittest cases
```
It uses mock and nose modules. For coverage it uses coverage module.
run unittest from root folder of this repo 

nosetests -v -s  test/test_pylxca_module.py
nosetests -v -s  test/test_pylxca_module.py --with-coverage
nosetests -v -s  test/test_pylxca_module.py --with-coverage --cover-package=pylxca
```
