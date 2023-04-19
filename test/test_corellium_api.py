# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 4.5.0-16775
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import corellium_api
from corellium_api.api.corellium_api import CorelliumApi  # noqa: E501
from corellium_api.rest import ApiException


class TestCorelliumApi(unittest.TestCase):
    """CorelliumApi unit test stubs"""

    def setUp(self):
        self.api = corellium_api.api.corellium_api.CorelliumApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_add_project_key(self):
        """Test case for v1_add_project_key

        Add Project Authorized Key  # noqa: E501
        """
        pass

    def test_v1_add_team_role_to_project(self):
        """Test case for v1_add_team_role_to_project

        Add team role to project  # noqa: E501
        """
        pass

    def test_v1_add_user_role_to_project(self):
        """Test case for v1_add_user_role_to_project

        Add user role to project  # noqa: E501
        """
        pass

    def test_v1_add_user_to_team(self):
        """Test case for v1_add_user_to_team

        Add user to team  # noqa: E501
        """
        pass

    def test_v1_agent_app_ready(self):
        """Test case for v1_agent_app_ready

        Check if App subsystem is ready  # noqa: E501
        """
        pass

    def test_v1_agent_delete_file(self):
        """Test case for v1_agent_delete_file

        Delete a File on VM  # noqa: E501
        """
        pass

    def test_v1_agent_get_file(self):
        """Test case for v1_agent_get_file

        Download a File from VM  # noqa: E501
        """
        pass

    def test_v1_agent_get_temp_filename(self):
        """Test case for v1_agent_get_temp_filename

        Get the path for a new temp file  # noqa: E501
        """
        pass

    def test_v1_agent_install_app(self):
        """Test case for v1_agent_install_app

        Install App at path  # noqa: E501
        """
        pass

    def test_v1_agent_install_profile(self):
        """Test case for v1_agent_install_profile

        Install a Profile to VM  # noqa: E501
        """
        pass

    def test_v1_agent_kill_app(self):
        """Test case for v1_agent_kill_app

        Kill an App  # noqa: E501
        """
        pass

    def test_v1_agent_list_app_icons(self):
        """Test case for v1_agent_list_app_icons

        List App Icons  # noqa: E501
        """
        pass

    def test_v1_agent_list_apps(self):
        """Test case for v1_agent_list_apps

        List Apps  # noqa: E501
        """
        pass

    def test_v1_agent_list_apps_status(self):
        """Test case for v1_agent_list_apps_status

        List Apps Status  # noqa: E501
        """
        pass

    def test_v1_agent_list_profiles(self):
        """Test case for v1_agent_list_profiles

        List Profiles  # noqa: E501
        """
        pass

    def test_v1_agent_run_app(self):
        """Test case for v1_agent_run_app

        Run an App  # noqa: E501
        """
        pass

    def test_v1_agent_set_file_attributes(self):
        """Test case for v1_agent_set_file_attributes

        Change Attrs of a File on VM  # noqa: E501
        """
        pass

    def test_v1_agent_system_get_adb_auth(self):
        """Test case for v1_agent_system_get_adb_auth

        Get ADB Auth Setting (AOSP only)  # noqa: E501
        """
        pass

    def test_v1_agent_system_get_network(self):
        """Test case for v1_agent_system_get_network

        Get IP of eth0 (AOSP only)  # noqa: E501
        """
        pass

    def test_v1_agent_system_get_prop(self):
        """Test case for v1_agent_system_get_prop

        Get System Property (AOSP only)  # noqa: E501
        """
        pass

    def test_v1_agent_system_install_open_g_apps(self):
        """Test case for v1_agent_system_install_open_g_apps

        Install OpenGApps (AOSP only)  # noqa: E501
        """
        pass

    def test_v1_agent_system_lock(self):
        """Test case for v1_agent_system_lock

        Lock Device (iOS Only)  # noqa: E501
        """
        pass

    def test_v1_agent_system_set_adb_auth(self):
        """Test case for v1_agent_system_set_adb_auth

        Set ADB Auth Setting (AOSP only)  # noqa: E501
        """
        pass

    def test_v1_agent_system_shutdown(self):
        """Test case for v1_agent_system_shutdown

        Instruct VM to halt  # noqa: E501
        """
        pass

    def test_v1_agent_system_unlock(self):
        """Test case for v1_agent_system_unlock

        Unlock Device (iOS Only)  # noqa: E501
        """
        pass

    def test_v1_agent_uninstall_app(self):
        """Test case for v1_agent_uninstall_app

        Uninstall an App  # noqa: E501
        """
        pass

    def test_v1_agent_uninstall_profile(self):
        """Test case for v1_agent_uninstall_profile

        Uninstall a Profile from VM  # noqa: E501
        """
        pass

    def test_v1_agent_upload_file(self):
        """Test case for v1_agent_upload_file

        Upload a file to VM  # noqa: E501
        """
        pass

    def test_v1_auth_login(self):
        """Test case for v1_auth_login

        Log In  # noqa: E501
        """
        pass

    def test_v1_btrace_preauthorize(self):
        """Test case for v1_btrace_preauthorize

        Pre-authorize an btrace download  # noqa: E501
        """
        pass

    def test_v1_clear_core_trace(self):
        """Test case for v1_clear_core_trace

        Clear CoreTrace logs  # noqa: E501
        """
        pass

    def test_v1_clear_hyper_trace(self):
        """Test case for v1_clear_hyper_trace

        Clear HyperTrace logs  # noqa: E501
        """
        pass

    def test_v1_clear_hyper_trace_hooks(self):
        """Test case for v1_clear_hyper_trace_hooks

        Clear Hooks on an instance  # noqa: E501
        """
        pass

    def test_v1_clear_instance_panics(self):
        """Test case for v1_clear_instance_panics

        Clear Panics  # noqa: E501
        """
        pass

    def test_v1_create_hook(self):
        """Test case for v1_create_hook

        Create hypervisor hook for Instance  # noqa: E501
        """
        pass

    def test_v1_create_image(self):
        """Test case for v1_create_image

        Create a new Image  # noqa: E501
        """
        pass

    def test_v1_create_instance(self):
        """Test case for v1_create_instance

        Create Instance  # noqa: E501
        """
        pass

    def test_v1_create_project(self):
        """Test case for v1_create_project

        Create a Project  # noqa: E501
        """
        pass

    def test_v1_create_snapshot(self):
        """Test case for v1_create_snapshot

        Create Instance Snapshot  # noqa: E501
        """
        pass

    def test_v1_create_subscriber_invite(self):
        """Test case for v1_create_subscriber_invite

        Create Subscriber Invite  # noqa: E501
        """
        pass

    def test_v1_create_user(self):
        """Test case for v1_create_user

        Create User  # noqa: E501
        """
        pass

    def test_v1_delete_hook(self):
        """Test case for v1_delete_hook

        Delete an existing hypervisor hook  # noqa: E501
        """
        pass

    def test_v1_delete_image(self):
        """Test case for v1_delete_image

        Delete Image  # noqa: E501
        """
        pass

    def test_v1_delete_instance(self):
        """Test case for v1_delete_instance

        Remove Instance  # noqa: E501
        """
        pass

    def test_v1_delete_instance_snapshot(self):
        """Test case for v1_delete_instance_snapshot

        Delete a Snapshot  # noqa: E501
        """
        pass

    def test_v1_delete_project(self):
        """Test case for v1_delete_project

        Delete a Project  # noqa: E501
        """
        pass

    def test_v1_delete_snapshot(self):
        """Test case for v1_delete_snapshot

        Delete a Snapshot  # noqa: E501
        """
        pass

    def test_v1_delete_user(self):
        """Test case for v1_delete_user

        Delete User  # noqa: E501
        """
        pass

    def test_v1_disable_expose_port(self):
        """Test case for v1_disable_expose_port

        Disable an exposed port on an instance for device access.  # noqa: E501
        """
        pass

    def test_v1_enable_expose_port(self):
        """Test case for v1_enable_expose_port

        Enable an exposed port on an instance for device access.  # noqa: E501
        """
        pass

    def test_v1_execute_hyper_trace_hooks(self):
        """Test case for v1_execute_hyper_trace_hooks

        Execute Hooks on an instance  # noqa: E501
        """
        pass

    def test_v1_get_hook_by_id(self):
        """Test case for v1_get_hook_by_id

        Get hypervisor hook by id  # noqa: E501
        """
        pass

    def test_v1_get_hooks(self):
        """Test case for v1_get_hooks

        Get all hypervisor hooks for Instance  # noqa: E501
        """
        pass

    def test_v1_get_image(self):
        """Test case for v1_get_image

        Get Image Metadata  # noqa: E501
        """
        pass

    def test_v1_get_images(self):
        """Test case for v1_get_images

        Get all Images Metadata  # noqa: E501
        """
        pass

    def test_v1_get_instance(self):
        """Test case for v1_get_instance

        Get Instance  # noqa: E501
        """
        pass

    def test_v1_get_instance_console(self):
        """Test case for v1_get_instance_console

        Get console websocket URL  # noqa: E501
        """
        pass

    def test_v1_get_instance_console_log(self):
        """Test case for v1_get_instance_console_log

        Get Console Log  # noqa: E501
        """
        pass

    def test_v1_get_instance_gpios(self):
        """Test case for v1_get_instance_gpios

        Get Instance GPIOs  # noqa: E501
        """
        pass

    def test_v1_get_instance_panics(self):
        """Test case for v1_get_instance_panics

        Get Panics  # noqa: E501
        """
        pass

    def test_v1_get_instance_peripherals(self):
        """Test case for v1_get_instance_peripherals

        Get Instance Peripherals  # noqa: E501
        """
        pass

    def test_v1_get_instance_rate(self):
        """Test case for v1_get_instance_rate

        Get rate information  # noqa: E501
        """
        pass

    def test_v1_get_instance_screenshot(self):
        """Test case for v1_get_instance_screenshot

        Get Instance Screenshot  # noqa: E501
        """
        pass

    def test_v1_get_instance_snapshot(self):
        """Test case for v1_get_instance_snapshot

        Get Instance Snapshot  # noqa: E501
        """
        pass

    def test_v1_get_instance_snapshots(self):
        """Test case for v1_get_instance_snapshots

        Get Instance Snapshots  # noqa: E501
        """
        pass

    def test_v1_get_instances(self):
        """Test case for v1_get_instances

        Get Instances  # noqa: E501
        """
        pass

    def test_v1_get_model_software(self):
        """Test case for v1_get_model_software

        Get Software for Model  # noqa: E501
        """
        pass

    def test_v1_get_models(self):
        """Test case for v1_get_models

        Get Supported Models  # noqa: E501
        """
        pass

    def test_v1_get_project(self):
        """Test case for v1_get_project

        Get a Project  # noqa: E501
        """
        pass

    def test_v1_get_project_instances(self):
        """Test case for v1_get_project_instances

        Get Instances in Project  # noqa: E501
        """
        pass

    def test_v1_get_project_keys(self):
        """Test case for v1_get_project_keys

        Get Project Authorized Keys  # noqa: E501
        """
        pass

    def test_v1_get_project_vpn_config(self):
        """Test case for v1_get_project_vpn_config

        Get Project VPN Configuration  # noqa: E501
        """
        pass

    def test_v1_get_projects(self):
        """Test case for v1_get_projects

        Get Projects  # noqa: E501
        """
        pass

    def test_v1_get_reset_link_info(self):
        """Test case for v1_get_reset_link_info

        Send Password Reset Link Info  # noqa: E501
        """
        pass

    def test_v1_get_snapshot(self):
        """Test case for v1_get_snapshot

        Get Snapshot  # noqa: E501
        """
        pass

    def test_v1_instances_instance_id_message_post(self):
        """Test case for v1_instances_instance_id_message_post

        Receive a message on an iOS vm  # noqa: E501
        """
        pass

    def test_v1_instances_instance_id_netdump_pcap_get(self):
        """Test case for v1_instances_instance_id_netdump_pcap_get

        Download a netdump pcap file  # noqa: E501
        """
        pass

    def test_v1_instances_instance_id_network_monitor_pcap_get(self):
        """Test case for v1_instances_instance_id_network_monitor_pcap_get

        Download a Network Monitor pcap file  # noqa: E501
        """
        pass

    def test_v1_kcrange(self):
        """Test case for v1_kcrange

        Get Kernel extension ranges  # noqa: E501
        """
        pass

    def test_v1_list_threads(self):
        """Test case for v1_list_threads

        Get Running Threads (CoreTrace)  # noqa: E501
        """
        pass

    def test_v1_media_play(self):
        """Test case for v1_media_play

        Start playing media  # noqa: E501
        """
        pass

    def test_v1_media_stop(self):
        """Test case for v1_media_stop

        Stop playing media  # noqa: E501
        """
        pass

    def test_v1_patch_instance(self):
        """Test case for v1_patch_instance

        Update Instance  # noqa: E501
        """
        pass

    def test_v1_pause_instance(self):
        """Test case for v1_pause_instance

        Pause an Instance  # noqa: E501
        """
        pass

    def test_v1_post_instance_input(self):
        """Test case for v1_post_instance_input

        Provide Instance Input  # noqa: E501
        """
        pass

    def test_v1_ready(self):
        """Test case for v1_ready

        API Status  # noqa: E501
        """
        pass

    def test_v1_reboot_instance(self):
        """Test case for v1_reboot_instance

        Reboot an Instance  # noqa: E501
        """
        pass

    def test_v1_remove_project_key(self):
        """Test case for v1_remove_project_key

        Delete Project Authorized Key  # noqa: E501
        """
        pass

    def test_v1_remove_team_role_from_project(self):
        """Test case for v1_remove_team_role_from_project

        Remove team role from project  # noqa: E501
        """
        pass

    def test_v1_remove_user_from_team(self):
        """Test case for v1_remove_user_from_team

        Remove user from team  # noqa: E501
        """
        pass

    def test_v1_remove_user_role_from_project(self):
        """Test case for v1_remove_user_role_from_project

        Remove user role from project  # noqa: E501
        """
        pass

    def test_v1_rename_instance_snapshot(self):
        """Test case for v1_rename_instance_snapshot

        Rename a Snapshot  # noqa: E501
        """
        pass

    def test_v1_reset_user_password(self):
        """Test case for v1_reset_user_password

        Reset User Password  # noqa: E501
        """
        pass

    def test_v1_restore_backup(self):
        """Test case for v1_restore_backup

        Restore backup  # noqa: E501
        """
        pass

    def test_v1_restore_instance_snapshot(self):
        """Test case for v1_restore_instance_snapshot

        Restore a Snapshot  # noqa: E501
        """
        pass

    def test_v1_roles(self):
        """Test case for v1_roles

        Get all roles  # noqa: E501
        """
        pass

    def test_v1_rotate_instance(self):
        """Test case for v1_rotate_instance

        Rotate device to specified orientation  # noqa: E501
        """
        pass

    def test_v1_send_user_reset_link(self):
        """Test case for v1_send_user_reset_link

        Send Password Reset Link  # noqa: E501
        """
        pass

    def test_v1_set_instance_gpios(self):
        """Test case for v1_set_instance_gpios

        Set Instance GPIOs  # noqa: E501
        """
        pass

    def test_v1_set_instance_peripherals(self):
        """Test case for v1_set_instance_peripherals

        Set Instance Peripherals  # noqa: E501
        """
        pass

    def test_v1_set_instance_state(self):
        """Test case for v1_set_instance_state

        Set state of Instance  # noqa: E501
        """
        pass

    def test_v1_snapshot_rename(self):
        """Test case for v1_snapshot_rename

        Rename a Snapshot  # noqa: E501
        """
        pass

    def test_v1_start_core_trace(self):
        """Test case for v1_start_core_trace

        Start CoreTrace on an instance  # noqa: E501
        """
        pass

    def test_v1_start_hyper_trace(self):
        """Test case for v1_start_hyper_trace

        Start HyperTrace on an instance  # noqa: E501
        """
        pass

    def test_v1_start_instance(self):
        """Test case for v1_start_instance

        Start an Instance  # noqa: E501
        """
        pass

    def test_v1_start_netdump(self):
        """Test case for v1_start_netdump

        Start Enhanced Network Monitor on an instance.  # noqa: E501
        """
        pass

    def test_v1_start_network_monitor(self):
        """Test case for v1_start_network_monitor

        Start Network Monitor on an instance.  # noqa: E501
        """
        pass

    def test_v1_stop_core_trace(self):
        """Test case for v1_stop_core_trace

        Stop CoreTrace on an instance.  # noqa: E501
        """
        pass

    def test_v1_stop_hyper_trace(self):
        """Test case for v1_stop_hyper_trace

        Stop HyperTrace on an instance.  # noqa: E501
        """
        pass

    def test_v1_stop_instance(self):
        """Test case for v1_stop_instance

        Stop an Instance  # noqa: E501
        """
        pass

    def test_v1_stop_netdump(self):
        """Test case for v1_stop_netdump

        Stop Enhanced Network Monitor on an instance.  # noqa: E501
        """
        pass

    def test_v1_stop_network_monitor(self):
        """Test case for v1_stop_network_monitor

        Stop Network Monitor on an instance.  # noqa: E501
        """
        pass

    def test_v1_team_change(self):
        """Test case for v1_team_change

        Update team  # noqa: E501
        """
        pass

    def test_v1_team_create(self):
        """Test case for v1_team_create

        Create team  # noqa: E501
        """
        pass

    def test_v1_team_delete(self):
        """Test case for v1_team_delete

        Delete team  # noqa: E501
        """
        pass

    def test_v1_teams(self):
        """Test case for v1_teams

        Get teams  # noqa: E501
        """
        pass

    def test_v1_unpause_instance(self):
        """Test case for v1_unpause_instance

        Unpause an Instance  # noqa: E501
        """
        pass

    def test_v1_update_hook(self):
        """Test case for v1_update_hook

        Update an existing hypervisor hook  # noqa: E501
        """
        pass

    def test_v1_update_project(self):
        """Test case for v1_update_project

        Update a Project  # noqa: E501
        """
        pass

    def test_v1_update_project_settings(self):
        """Test case for v1_update_project_settings

        Change Project Settings  # noqa: E501
        """
        pass

    def test_v1_update_user(self):
        """Test case for v1_update_user

        Update User  # noqa: E501
        """
        pass

    def test_v1_upgrade_instance(self):
        """Test case for v1_upgrade_instance

        Upgrade iOS version  # noqa: E501
        """
        pass

    def test_v1_upload_image_data(self):
        """Test case for v1_upload_image_data

        Upload Image Data  # noqa: E501
        """
        pass

    def test_v1_user_agree_terms(self):
        """Test case for v1_user_agree_terms

        Consent to the current terms and conditions  # noqa: E501
        """
        pass

    def test_v1_users_change_password_post(self):
        """Test case for v1_users_change_password_post

        Change User Password  # noqa: E501
        """
        pass

    def test_v1_users_login(self):
        """Test case for v1_users_login

        Log In  # noqa: E501
        """
        pass

    def test_v2_get_instance_quick_connect_command(self):
        """Test case for v2_get_instance_quick_connect_command

        Recommended SSH Command for Quick Connect  # noqa: E501
        """
        pass

    def test_v2_get_instance_state(self):
        """Test case for v2_get_instance_state

        Get state of Instance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
