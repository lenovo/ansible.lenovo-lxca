#!/usr/bin/python

#---- Documentation Start ----------------------------------------------------#
ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'supported_by': 'community',
    'status': ['preview']
}


DOCUMENTATION = '''
---
version_added: "1.0"
author: Mahesh Kalge
module: pylxca_module
short_description: custom module for pylxca utility
description:
  - This module returns/displays a inventory details of chassis, cmms, nodes,
    switches, fans, powersupplies, fanmuxes etc
options:
  login_user:
    description:
      The username for use in HTTP basic authentication.
  login_password:
    description:
      The password for use in HTTP basic authentication.
  command_options:
    description:
      options are connect, chassis, cmms, switches, fans, fanmuxes
  auth_url:
    description:
      lxca https full web address
requirements:
  - pylxca
'''

EXAMPLES = '''
# get cmms info
- pylxca_module: command_options=connect login_user=USERID login_password=CME44ibm auth_url=https://10.243.15.168
'''


import os
import imp
import json
import logging
import logging.handlers
#from pylxca.pylxca_cmd.lxca_pyshell import *
from pylxca import *

ip_map = dict()


def load_compliance_plugin( location, name ):
    plugin = None
    plugins_list = os.listdir(location)

    try:
        # Find the specified plugin in plugins folder
        for plugin_name in plugins_list:
            if str(plugin_name).lower() == str(name).lower():
                plugin_dir = os.path.join(location, plugin_name)

                if not os.path.isdir(plugin_dir) or not "__init__.py" in os.listdir(plugin_dir):
                    raise Exception("Invalid Compliance Plugin")

                info = imp.find_module(name, [location])
                plugin = imp.load_module(name, *info)
    except Exception as err:
        raise err
    return plugin

def find_conn_obj ( kwargs ):
    if ip_map.get(kwargs.get('url')) is not None:
       return ip_map.get(kwargs.get('url'))
    return None
  
def _get_connect_lxca ( module, kwargs ):
    #global _conn_lxca
    _conn_lxca = None
    
    kargs = {
                'url': kwargs.get('auth_url'),
                'user': kwargs.get('login_user'),
                'pw': kwargs.get('login_password'),
                'ip': kwargs.get('discovery_ip'),
                'noverify':'True'
        }
    try:
        _conn_lxca = find_conn_obj( kwargs ) 
        if _conn_lxca is None: 
            _conn_lxca = connect(kwargs.get('auth_url'),kwargs.get('login_user'),kwargs.get('login_password'),"True")
        ip_map.update({kwargs.get('auth_url'): _conn_lxca})
#        ip_map = { kwargs.get('auth_url'): _conn_lxca }
        if _conn_lxca is None: 
        	module.fail_json(msg = "Error connecting with: %s" % kwargs.get('auth_url'))
    except Exception:
        module.fail_json(msg = "Error authenticating with provided credentials: %s" % kwargs.get('auth_url'))
    return _conn_lxca

def _get_chassis_inventory( module, kwargs ):
    result = None
    try:
       result = chassis(_get_connect_lxca(module,kwargs))
    except Exception as e:
       module.fail_json(msg = "Error getting chassis inventory" + str(e))
    return result

def _get_cmms_inventory(module, kwargs):
    result = None
    try:
        result =  cmms(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg = "Error getting cmms inventory" + str(e))
    return result

def _get_configstatus(module, kwargs):
    result = None
    try:
        result =  configpatterns(_get_connect_lxca(module,kwargs), endpoint= kwargs.get('endpoint'), status = kwargs.get('status'))
        if result.has_key('items')  and len(result['items']) and result['items'][0]:
            result = result['items'][0]
    except Exception as e:
        module.fail_json(msg = "Error in configstatus " + str(e))
    return result


def _get_configpatterns(module, kwargs):
    result = None
    try:
        result =  configpatterns(_get_connect_lxca(module,kwargs))
    except Exception as e:
        module.fail_json(msg = "Error in configpatterns " + str(e))
    return result

def _get_particular_configpattern(module, kwargs):
    result = None
    try:
        pattern_dict = {}
        pattern_dict['id'] = kwargs.get('id')
        pattern_dict['includeSettings'] = kwargs.get('includeSettings')
        result =  configpatterns(_get_connect_lxca(module,kwargs), **pattern_dict)
    except Exception as e:
        module.fail_json(msg = "Error in getting particular configpattern " + str(e))
    return result

def _apply_configpatterns(module, kwargs):
    result = None
    try:
        pattern_dict = {}
        pattern_dict['id'] = kwargs.get('id')
        pattern_dict['name'] = kwargs.get('name')
        pattern_dict['endpoint'] = kwargs.get('endpoint')
        pattern_dict['restart'] = kwargs.get('restart')
        pattern_dict['type'] = kwargs.get('type')
        result =  configpatterns(_get_connect_lxca(module,kwargs),
                                      **pattern_dict
                                )
    except Exception as e:
        module.fail_json(msg = "Error in applying configpatterns" + str(e))
    return result

def _import_configpatterns(module, kwargs):
    result = None
    try:
        pattern_dict = {}
        pattern_dict['pattern_update_dict'] = kwargs.get('pattern_update_dict')
        result =  configpatterns(_get_connect_lxca(module,kwargs),
                                      **pattern_dict
                                )
    except Exception as e:
        module.fail_json(msg = "Error in import configpatterns" + str(e))
    return result

def _get_configprofiles(module, kwargs):
    result = None
    delete_profile = None
    unassign_profile = None
    try:
        action = kwargs.get("action")
        if action:
            if action.lower() in ['delete']:
                delete_profile = 'True'
            elif action.lower() in ['unassign']:
               unassign_profile = 'True'
        result = configprofiles( _get_connect_lxca(module,kwargs),
                                 kwargs.get('id'),
                                 kwargs.get('name'),
                                 kwargs.get('endpoint'),
                                 kwargs.get('restart'),
                                 delete_profile,
                                 unassign_profile,
                                 kwargs.get('powerdown'),
                                 kwargs.get('resetimm'),
                                 kwargs.get('force'),)
# kwargs.get('delete_profile'), kwargs.get('unassign') )
    except Exception as e:
        module.fail_json(msg = "Error getting configprofiles" + str(e))
    return result

def _get_configtargets(module, kwargs):
    result = None
    try:
        result =  configtargets(_get_connect_lxca(module,kwargs), kwargs.get('id'))
    except Exception as e:
        module.fail_json(msg = "Error getting configtargets" + str(e))
    return result


def _get_discover(module, kwargs):
    result = None
    try:
        result =  discover(_get_connect_lxca(module,kwargs),kwargs.get('discovery_ip'))
    except Exception as e:
        module.fail_json(msg = "Error discovery " + str(e))
    return result

def _get_fans(module, kwargs):
    result = None
    try:
        result =  fans(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg = "Error getting fans inventory " + str(e))
    return result

def _get_fanmuxes(module, kwargs):
    result = None
    try:
        result =  fanmuxes(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg = "Error getting fanmuxes inventory " + str(e))
    return result

def _get_ffdc(module, kwargs):
    result = None
    try:
        result =  ffdc(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg = "Error getting ffdc inventory " + str(e))
    return result

def _get_jobs(module, kwargs):
    result = None
    try:
        result =  jobs(_get_connect_lxca(module,kwargs), kwargs.get('id'))
    except Exception as e:
        module.fail_json(msg = "Error getting jobs inventory " + str(e))
    return result

# TODO filter
def _get_lxcalog(module, kwargs):
    result = None
    try:
        result = lxcalog(_get_connect_lxca(module,kwargs))
    except Exception as e:
        module.fail_json(msg = "Error getting lxcalog " + str(e))
    return result

def _manage_endpoint(module, kwargs):
    result = None

    try:
       result = manage(_get_connect_lxca(module,kwargs),kwargs.get('endpoint_ip'),kwargs.get('user'),kwargs.get('password'),kwargs.get('recovery_password'), None, kwargs.get('force'))
    except Exception as e:
        module.fail_json(msg = " Fail to manage the endpoint" + str(e))
    return result

def _manage_status(module, kwargs):
    result = None
    try:
       result = manage(_get_connect_lxca(module,kwargs), None, None, None, None, kwargs.get('jobid'))
    except Exception as e:
        module.fail_json(msg = "Error getting info abt jobid" + str(e))
    return result

def _unmanage_endpoint(module, kwargs):
    result = None

    try:
       result = unmanage(_get_connect_lxca(module,kwargs),kwargs.get('endpoint_ip'), kwargs.get('force'), None)
    except Exception as e:
        module.fail_json(msg = " Fail to unmanage the endpoint" + str(e))
    return result

def _unmanage_status(module, kwargs):
    result = None
    try:
       result = unmanage(_get_connect_lxca(module,kwargs), None,None, kwargs.get('jobid'))
    except Exception as e:
        module.fail_json(msg = "Error getting info abt jobid" + str(e))
    return result

def _get_manifests(module, kwargs):
    result = None
    try:
        dict = {'id':kwargs.get('sol_id'),'file':kwargs.get('manifest_path')}
        conn = _get_connect_lxca(module,kwargs)
        result =  manifests(conn,dict)
    except Exception as e:
        module.fail_json(msg = "Error getting manifest " + str(e))
    return result

#TODO chassis , status
def _get_nodes(module, kwargs):
    result = None
    try:
        result =  nodes(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg = "Error getting nodes inventory " + str(e))
    return result

def _get_powersupplies(module, kwargs):
    result = None
    try:
        result =  powersupplies(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg = "Error getting powersupplies inventory " + str(e))
    return result

#TODO type
def _get_scalablesystem(module, kwargs):
    result = None
    try:
        result =  scalablesystem(_get_connect_lxca(module,kwargs), kwargs.get('id'))
    except Exception as e:
        module.fail_json(msg = "Error getting scalablesystem inventory " + str(e))
    return result

# TODO chassis, ports, action
def _get_switches_inventory( module, kwargs):
    result = None
    try:
        result = switches(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg="Error getting switches " + str(e))
    return result

def _get_tasks(module, kwargs):
    result = None
    tasks_dict = {}
    jobUID = kwargs.get("id")
    action = kwargs.get("action")
    if action in ['cancel', 'delete']:
        tasks_dict['jobUID'] = jobUID
        tasks_dict['action'] = action
    elif action in ['update']:
        tasks_dict['action'] = action
        updateList = kwargs.get("update_list")
        tasks_dict['updateList'] = updateList
    else:
        tasks_dict['jobUID'] = jobUID
    try:
        result = tasks(_get_connect_lxca(module,kwargs),**tasks_dict)
    except Exception as e:
        module.fail_json(msg = "Error getting tasks " + str(e))
    return result

def _get_updaterepo_info(module, kwargs):
    result = None
    try:
        result =  updaterepo(_get_connect_lxca(module,kwargs),
                             kwargs.get('repo_key'),
                             kwargs.get('action'),
                             kwargs.get('machine_type'),
                             kwargs.get('scope'),
                             kwargs.get('fixids'),
                             kwargs.get('file_type'))
    except Exception as e:
        module.fail_json(msg = "Error retriving firmware info." + str(e) )
    return result

def _update_firmware(module, kwargs):
    result = None
    try:
        result =  updatecomp(_get_connect_lxca(module,kwargs),mode=kwargs.get('mode'),action=kwargs.get('action'),cmm=kwargs.get('cmm'),switch=kwargs.get('switch'),server=kwargs.get('server'),storage=kwargs.get('storage'))
#        result =  updatecomp(_get_connect_lxca(module,kwargs),"immediate","apply","A155A9581FB711E397C2000AF72569C4,lnvgy_fw_imm2_tcoo18q-3.20_anyos_noarch,IMM2")
    except Exception as e:
        module.fail_json(msg = "Error updating firmware " + str(e))
    return result

def transform_devicelist( devicelist, uuid_list):
    ret_device_list = []
    for dev in devicelist:
        new_dict = {}
        for dev_type in dev.keys(): #SwitchList
            new_list = []
            for sw in dev[dev_type]:
                if not sw['UUID'] in uuid_list:
                    continue
                cm_list = []
                for cm in sw['Components']:
                    cm_list.append({'Component': cm})
                sw['Components'] = cm_list
                new_list.append(sw)
            if len(new_list) > 0:
                new_dict[dev_type] = new_list
        if len(new_dict) > 0:
            ret_device_list.append(new_dict)
    return ret_device_list

def valid_compliance_policies( policy_list):
    uuid_list = []
    for cp in policy_list:
        if 'uuid' in cp.keys():
            if 'currentPolicy' in cp.keys() and  len(cp['currentPolicy']) > 0:
                uuid_list.append(cp['uuid'])

    return uuid_list


def _update_firmware_all(module, kwargs):
    result = None
    try:
        rep = updatepolicy(_get_connect_lxca(module,kwargs), info="NAMELIST")
        uuid_list = valid_compliance_policies(rep['policies'])
        if len(uuid_list) == 0:
            module.fail_json(msg="No policy assigned to any device")
            return result

        dev_uuid_list = []
        if 'uuid_list' in kwargs:
            dev_uuid_list = kwargs.get('uuid_list')
            if len(dev_uuid_list) > 0:
                # getting common uuid of two list
                uuid_list = list(set(dev_uuid_list).intersection(uuid_list))

        rep = updatecomp(_get_connect_lxca(module,kwargs), query='components')
        ret_dev_list = rep['DeviceList']
        mod_dev_list = transform_devicelist(ret_dev_list, uuid_list)
        if len(mod_dev_list) == 0:
            module.fail_json(msg="No updateable component with assigned policy found")
            return result

        result =  updatecomp(_get_connect_lxca(module,kwargs),mode=kwargs.get('mode'),action=kwargs.get('action'), dev_list=mod_dev_list)
    except Exception as e:
        module.fail_json(msg = "Error updating all device firmware " + str(e))
    return result

def _update_firmware_query_status(module, kwargs):
    result = None
    try:
        result =  updatecomp(_get_connect_lxca(module,kwargs),query='status')
#        result =  updatecomp(_get_connect_lxca(module,kwargs),"immediate","apply","A155A9581FB711E397C2000AF72569C4,lnvgy_fw_imm2_tcoo18q-3.20_anyos_noarch,IMM2")
    except Exception as e:
        module.fail_json(msg = "Error updating firmware " + str(e))
    return result

def _update_firmware_query_comp(module, kwargs):
    result = None
    try:
        result =  updatecomp(_get_connect_lxca(module,kwargs),query='components')
    except Exception as e:
        module.fail_json(msg = "Error updating firmware " + str(e))
    return result


def _get_managementserver_pkg(module, kwargs):
    result = None
    try:
        result =  managementserver(_get_connect_lxca(module,kwargs),
                             kwargs.get('update_key'),
                             kwargs.get('fixids'),
                             kwargs.get('type')
                             )
    except Exception as e:
        module.fail_json(msg = "Error retriving managementserver info." + str(e))
    return result

def _update_managementserver_pkg(module, kwargs):
    result = None
    try:
        result =  managementserver(_get_connect_lxca(module,kwargs),
                             kwargs.get('update_key'),
                             kwargs.get('fixids'),
                             kwargs.get('type'),
                             kwargs.get('action'),
                       )
    except Exception as e:
        module.fail_json(msg = "Error retriving update managementserver." + str(e))
    return result

def _import_managementserver_pkg(module, kwargs):
    result = None
    try:
        result =  managementserver(_get_connect_lxca(module,kwargs),
                             kwargs.get('update_key'),
                             kwargs.get('fixids'),
                             kwargs.get('type'),
                             kwargs.get('action'),
                             kwargs.get('files'),
                             kwargs.get('jobid')
                             )
    except Exception as e:
        module.fail_json(msg = "Error import managementserver ." + str(e))
    return result


def _get_updatepolicy(module, kwargs):
    result = None
    try:
        result =  updatepolicy(_get_connect_lxca(module,kwargs),
                               kwargs.get('policy_info'),
                               kwargs.get('jobid'),
                               kwargs.get('uuid'),
                               kwargs.get('policy_name'),
                               kwargs.get('policy_type')
                               )
    except Exception as e:
        module.fail_json(msg = "Error getting updatepolicy " + str(e))
    return result

def _get_osimages(module, kwargs):
    result = None
    try:
        osimages_info = kwargs.get('osimages_info')
        osimages_dict = kwargs.get('osimages_dict')
        if osimages_info and osimages_dict:
            result =  osimages(_get_connect_lxca(module,kwargs),
                               osimages_info,
                               **osimages_dict
                        )
        elif osimages_dict:
            result = osimages(_get_connect_lxca(module, kwargs),
                              **osimages_dict
                              )

        elif osimages_info:
            result = osimages(_get_connect_lxca(module, kwargs),
                              osimages_info
                              )
        else:
            result = osimages(_get_connect_lxca(module,kwargs))

    except Exception as e:
        module.fail_json(msg = "Error processing osimages " + str(e))
    return result

def _get_users(module, kwargs):
    result = None
    try:
        result =  users(_get_connect_lxca(module,kwargs), kwargs.get('id'))
    except Exception as e:
        module.fail_json(msg = "Error getting users " + str(e))
    return result

def _gather_server_facts(module, kwargs):
    rslt = _get_nodes(module, kwargs)
    if not rslt:
        module.exit_json(changed=False, msg="Fail to retrieve information", result=rslt)
    else:
        module.exit_json(changed=True, msg="Success retrieving information", ansible_facts=rslt)

def _validate_basic_rules(module, kwargs):
    rule_list = kwargs.get("BASIC_RULES")
    inv_data_dict = kwargs.get("inv_data")
    compliance_status = True

    for each_rule in rule_list:
        if inv_data_dict[each_rule["property"]] == str(each_rule["ref_value"]):
            compliance_status = True
        else:
            compliance_status = False
            break

    module.exit_json(changed=True, msg="Executed Compliance Validation", result=compliance_status)

def _validate_plugin_rules(module, kwargs):
    location = kwargs.get("plugin_location")
    name = kwargs.get("plugin_name")

    try:
        compliance_status = False
        plugin = load_compliance_plugin( location, name )
        if plugin:
            compliance_status = plugin.validate_compliance()
    except Exception as err:
        module.fail_json(msg = err.__str__())
    module.exit_json(changed=True, msg="Executed Compliance Validation through Plugin", result=compliance_status)

def _create_resourcegroups(module, kwargs):
    result = None
    param_dict = {  'name': kwargs.get('name'),
                    'description':kwargs.get('description'),
                    'type':kwargs.get('type'),
                    'solutionVPD':kwargs.get('solutionVPD'),
                    'members':kwargs.get('members'),
                    'criteria':kwargs.get('criteria')}
    try:
        result =  resourcegroups(_get_connect_lxca(module,kwargs),**param_dict)
    except Exception as e:
        module.fail_json(msg = "Error Creating Resource Group " + str(e))
    return result

def _add_resourcegroup_member(module, kwargs):
    result = None
    try:
        result =  resourcegroups(_get_connect_lxca(module,kwargs), kwargs.get('name'))
    except Exception as e:
        module.fail_json(msg = "Error getting users " + str(e))
    return result

def _get_resourcegroups(module, kwargs):
    result = None
    try:
        result =  resourcegroups(_get_connect_lxca(module,kwargs), kwargs.get('uuid'))
    except Exception as e:
        module.fail_json(msg = "Error getting users " + str(e))
    return result

def _compliance_engine(module, kwargs):
    # TODO Stub for compliance engine REST API
    return True

def _rules(module, kwargs):
    result = None
    try:
        result =  rules(_get_connect_lxca(module,kwargs), kwargs.get('id'), kwargs.get('comp_rule'))
    except Exception as e:
        module.fail_json(msg = "Error getting rules " + str(e))
    return result

def _compositeResults(module, kwargs):
    result = None
    try:
        result =  compositeResults(_get_connect_lxca(module,kwargs), kwargs.get('id'),
                                   kwargs.get('query_solutionGroups'),
                                   kwargs.get('solutionGroups'),
                                   kwargs.get('targetResources'),
                                   kwargs.get('all_rules'),)
    except Exception as e:
        module.fail_json(msg = "Error getting compositeResults " + str(e))
    return result


func_dict = {
                'connect': _get_connect_lxca,
                'chassis': _get_chassis_inventory,
                'cmms': _get_cmms_inventory,
                'get_configpatterns': _get_configpatterns,
                'get_particular_configpattern': _get_particular_configpattern,
                'import_configpatterns': _import_configpatterns,
                'apply_configpatterns': _apply_configpatterns,
                'get_configstatus': _get_configstatus,
                'configprofiles': _get_configprofiles,
                'configtargets': _get_configtargets,
                'discover': _get_discover,
                'fans': _get_fans,
                'fanmuxes': _get_fanmuxes,
                'ffdc': _get_ffdc,
                'jobs': _get_jobs,
                'lxcalog': _get_lxcalog,
                'manage': _manage_endpoint,
                'unmanage': _unmanage_endpoint,
                'manage_status': _manage_status,
                'unmanage_status': _unmanage_status,
                'manifests': _get_manifests,
                'nodes': _get_nodes,
                'osimages': _get_osimages,
                'powersupplies': _get_powersupplies,
                'scalablesystem': _get_scalablesystem,
                'switches': _get_switches_inventory,
                'tasks': _get_tasks,
                'updaterepo': _get_updaterepo_info,
                'update_firmware': _update_firmware,
                'update_firmware_all': _update_firmware_all,
                'update_firmware_query_status':_update_firmware_query_status,
                'update_firmware_query_comp':_update_firmware_query_comp,
                'get_managementserver_pkg': _get_managementserver_pkg,
                'update_managementserver_pkg': _update_managementserver_pkg,
                'import_managementserver_pkg': _import_managementserver_pkg,
                'updatepolicy': _get_updatepolicy,
                'users': _get_users,
                'gather_server_facts': _gather_server_facts,
                'validate_basic_rules': _validate_basic_rules,
                'validate_plugin_rules': _validate_plugin_rules,
                'get_resourcegroups':_get_resourcegroups,
                'create_resourcegroups':_create_resourcegroups,
                'add_resourcegroup_member':_add_resourcegroup_member,
                'compliance_engine':_compliance_engine,
                'rules': _rules,
                'compositeResults': _compositeResults,

}


# ===========================================
# Main
#

def main():
    module = AnsibleModule(
        argument_spec=dict(
            login_user      = dict(default=None, required=False),
            login_password  = dict(default=None, required=False),
            connobject      = dict(default=None),
            command_options = dict( choises=list(func_dict) ),
            action          = dict(default=None),
            auth_url        = dict(default=None),
            uuid            = dict(default=None),
            id              = dict(default=None),
            endpoint_ip     = dict(default=None),
            jobid           = dict(default=None),
            user            = dict(default=None, required=False),
            password        = dict(default=None, required=False),
            force           = dict(default=None),
            percentage      = dict(default=None),
            state           = dict(default=None),
            sol_id          = dict(default=None),
            manifest_path   = dict(default=None),
            description      = dict(default=None),
            solutionVPD     = dict(default=None, type=('dict')),
            members   = dict(default=None, type=('list')),
            criteria  = dict(default=None, type=('list')),
            recovery_password = dict(default=None),
            repo_key        = dict(default=None),
            mode     = dict(default=None),
            server   = dict(default=None),
            storage  = dict(default=None),
            switch   = dict(default=None),
            cmm      = dict(default=None),
            policy_info = dict(default=None),
            policy_name = dict(default=None),
            policy_type = dict(default=None),
            update_list     = dict(default=None,type=('list')),
            fact_dict       = dict(default=None,type=('dict')),
            machine_type    = dict(default=None),
            fixids          = dict(default=None),
            scope           = dict(default=None),
            file_type       = dict(default=None),
            endpoint        = dict(default=None),
            restart         = dict(default=None),
            type            = dict(default=None),
            name            = dict(default=None),
            delete_profile  = dict(default=None),
            unassign        = dict(default=None),
            powerdown       = dict(default=None),
            resetimm        = dict(default=None),
            inv_data        = dict(default=None,type=('dict')),
            BASIC_RULES      = dict(default=None, type=('list')),
            comp_rule       = dict(default=None,type=('dict')),
            pattern_update_dict = dict(default=None, type=('dict')),
            includeSettings = dict(default=None),
            osimages_info   = dict(default=None),
            osimages_dict   = dict(default=None, type=('dict')),
            update_key      = dict(default=None),
            files           = dict(default=None),
            unittest        = dict(default=None),
            uuid_list       = dict(default=None, type=('list')),
            solutionGroups   = dict(default=None, type=('list')),
            query_solutionGroups = dict(default=None),
            targetResources = dict(default=None, type=('list')),
            all_rules = dict(default=None)

        ),
        check_invalid_arguments=False,
	    supports_check_mode = False,
    )
    
    conn = None
    rslt = None
    command_options = module.params['command_options']
    global ip_map

    rslt = func_dict[command_options](module,module.params)
    if module.params['unittest']:
        return rslt

    if command_options == "connect":
        if rslt:
            module.exit_json(changed=False, msg="Success %s result" % command_options, result="Connected successfully")
    if not rslt:
        module.fail_json(changed=False, msg="Fail to get %s result" %command_options, result=rslt)
    else:
        module.exit_json(changed=False, msg="Success %s result" %command_options, result=rslt)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
	main()



