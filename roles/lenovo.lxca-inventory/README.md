Ansible Role: Lenovo LXCA Inventory
=========

Ansible Role to collect get inventory data of managed elements from Lenovo xClarity Administratr.

Requirements
------------

- Ansible version 2.4.2 or later ([Ansible installation documentation](http://docs.ansible.com/ansible/intro_installation.html))

- Python Client for Lenovo xClarity Administratr.([LXCA Python Client v2.0.0](https://github.com/lenovo/pylxca))

   pip install pylxca


Role Variables
--------------
Available variables are listed below, along with description:

Variable | Description
--- | ---
uuid| UUID of a managed element
id| ID of a resource
endpoint_ip| IP address of Endpoint
user| user name
password| password
recovery_password| recovery password for resource
jobid| job id of background job
mode| operation mode for config action
lxca_action| operation for config
server| compute node details
switch| switch details
storage| storage details
cmm| cmm details
force| force flag for config action
policy_info| policy detail
policy_name| policy name
policy_type| policy type
repo_key| repository key
machine_type| machine type
scope| operation scope
fixids| firmware image id
file_type| type of file in config action
endpoint| target managed endpoint for config action
restart| config action
config_pattern_name| name of config patteren
config_profile_name| name of config profile
powerdown| power operation
resetimm| action reset imm
pattern_update_dict| dictionary of category pattern information
pattern_from_file| file path for pattern data
includeSettings| flag for reading config data
osimages_info| information about os images
osimages_dict| dictionary of information about os images
files| files location
update_key| key for firmware update
status| status of managed element
uuid_list| list of UUID

Dependencies
------------

Connectivity with Lenovo xClarity Administrator.

Example Playbook
----------------

To execute an Ansible playbook, use the following command:
```
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd lxca_url=https://10.240.29.217" inventory.yml -vvvv
```
-vvv is an optional verbos command that helps identify what is happening during playbook execution.

    - name: get nodes data from LXCA
      pylxca_module:
        login_user: "{{ lxca_user }}"
        login_password: "{{ lxca_password }}"
        auth_url: "{{ lxca_url }}"
        command_options: nodes
      register: rslt
      tags:
         nodes

License
-------

Copyright (C) 2018 Lenovo, Inc.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


