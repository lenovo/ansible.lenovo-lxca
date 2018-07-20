Ansible Role: Lenovo LXCA Inventory
=========

Ansible Role to collect get inventory data of managed elements from Lenovo
xClarity Administratr.

Requirements
------------

- Ansible version 2.4.2 or later ([Ansible installation
  documentation](http://docs.ansible.com/ansible/intro_installation.html))

- Python Client for Lenovo xClarity Administratr.([LXCA Python Client
  v2.0.0](https://github.com/lenovo/pylxca))

   pip install pylxca


Role Variables
--------------
Available variables are listed below, along with description:

Variable | Description
--- | ---
uuid | uuid of device
id |  id of job 
update_list | update list for tasks
discover_ip | discover specific ip

Supported Tags
--------------
Supported tags are listed below, along with description:

tags | Description
--- | ---
chassis | chassis details
cmms | cmms details
nodes | nodes details
discover | discover using slp
fans | fans details
fanmuxes | fanmux details
jobs | job details
lxcalog | lxca log
powersupplies | powersupply details
scalablesystem | scalablesystem details
switches | switch details
tasks | task details and update 
users | user details
ffdc | ffdc for uuid


Dependencies
------------

Connectivity with Lenovo xClarity Administrator.

Example Playbook
----------------

To execute an Ansible playbook, use the following command:
```
ansible-playbook -e "lxca_user=USERID lxca_password=Passw0rd
lxca_url=https://10.240.29.217" inventory.yml -vvvv
```
-vvv is an optional verbos command that helps identify what is happening during
playbook execution.

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
Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at
http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

