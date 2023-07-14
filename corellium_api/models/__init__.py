# coding: utf-8

# flake8: noqa
"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 5.2.0-17368
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from corellium_api.models.address import Address
from corellium_api.models.agent_app import AgentApp
from corellium_api.models.agent_app_ready_response import AgentAppReadyResponse
from corellium_api.models.agent_app_status import AgentAppStatus
from corellium_api.models.agent_apps_list import AgentAppsList
from corellium_api.models.agent_apps_status_list import AgentAppsStatusList
from corellium_api.models.agent_error import AgentError
from corellium_api.models.agent_icons import AgentIcons
from corellium_api.models.agent_install_body import AgentInstallBody
from corellium_api.models.agent_profiles_return import AgentProfilesReturn
from corellium_api.models.agent_system_adb_auth import AgentSystemAdbAuth
from corellium_api.models.agent_system_get_prop_body import AgentSystemGetPropBody
from corellium_api.models.agent_value_return import AgentValueReturn
from corellium_api.models.agreed_ack import AgreedAck
from corellium_api.models.api_conflict_error import ApiConflictError
from corellium_api.models.api_error import ApiError
from corellium_api.models.api_internal_consistency_error import ApiInternalConsistencyError
from corellium_api.models.api_not_found_error import ApiNotFoundError
from corellium_api.models.api_token import ApiToken
from corellium_api.models.bit import Bit
from corellium_api.models.btrace_enable_options import BtraceEnableOptions
from corellium_api.models.button import Button
from corellium_api.models.coupon_options import CouponOptions
from corellium_api.models.create_team import CreateTeam
from corellium_api.models.created_by import CreatedBy
from corellium_api.models.credentials import Credentials
from corellium_api.models.domain_options import DomainOptions
from corellium_api.models.extension import Extension
from corellium_api.models.features import Features
from corellium_api.models.file_changes import FileChanges
from corellium_api.models.firmware import Firmware
from corellium_api.models.gpio_state_definition import GpioStateDefinition
from corellium_api.models.gpios_state import GpiosState
from corellium_api.models.grant_trial_request_response import GrantTrialRequestResponse
from corellium_api.models.hook import Hook
from corellium_api.models.image import Image
from corellium_api.models.instance import Instance
from corellium_api.models.instance_agent_state import InstanceAgentState
from corellium_api.models.instance_boot_options import InstanceBootOptions
from corellium_api.models.instance_boot_options_additional_tag import InstanceBootOptionsAdditionalTag
from corellium_api.models.instance_console_endpoint import InstanceConsoleEndpoint
from corellium_api.models.instance_create_options import InstanceCreateOptions
from corellium_api.models.instance_input import InstanceInput
from corellium_api.models.instance_netdump_state import InstanceNetdumpState
from corellium_api.models.instance_netmon_state import InstanceNetmonState
from corellium_api.models.instance_return import InstanceReturn
from corellium_api.models.instance_services import InstanceServices
from corellium_api.models.instance_start_options import InstanceStartOptions
from corellium_api.models.instance_state import InstanceState
from corellium_api.models.instance_stop_options import InstanceStopOptions
from corellium_api.models.instance_upgrade_body import InstanceUpgradeBody
from corellium_api.models.invitation import Invitation
from corellium_api.models.invite_revoke_params import InviteRevokeParams
from corellium_api.models.invite_revoke_params_ids import InviteRevokeParamsIds
from corellium_api.models.kcrange import Kcrange
from corellium_api.models.kernel_task import KernelTask
from corellium_api.models.kernel_thread import KernelThread
from corellium_api.models.media_play_body import MediaPlayBody
from corellium_api.models.model import Model
from corellium_api.models.model_software import ModelSoftware
from corellium_api.models.netdump_filter import NetdumpFilter
from corellium_api.models.password_change_body import PasswordChangeBody
from corellium_api.models.password_reset_body import PasswordResetBody
from corellium_api.models.patch_instance_options import PatchInstanceOptions
from corellium_api.models.peripherals_data import PeripheralsData
from corellium_api.models.plan import Plan
from corellium_api.models.project import Project
from corellium_api.models.project_key import ProjectKey
from corellium_api.models.project_quota import ProjectQuota
from corellium_api.models.project_settings import ProjectSettings
from corellium_api.models.project_usage import ProjectUsage
from corellium_api.models.proxy_config import ProxyConfig
from corellium_api.models.rate_info import RateInfo
from corellium_api.models.reset_link_body import ResetLinkBody
from corellium_api.models.role import Role
from corellium_api.models.rotate_body import RotateBody
from corellium_api.models.snapshot import Snapshot
from corellium_api.models.snapshot_creation_options import SnapshotCreationOptions
from corellium_api.models.snapshot_status import SnapshotStatus
from corellium_api.models.subscriber_invite import SubscriberInvite
from corellium_api.models.team import Team
from corellium_api.models.team_create import TeamCreate
from corellium_api.models.text_input import TextInput
from corellium_api.models.token import Token
from corellium_api.models.touch_curve_input import TouchCurveInput
from corellium_api.models.touch_input import TouchInput
from corellium_api.models.trial import Trial
from corellium_api.models.trial_extension import TrialExtension
from corellium_api.models.trial_request_metadata import TrialRequestMetadata
from corellium_api.models.trial_request_options import TrialRequestOptions
from corellium_api.models.update_extension import UpdateExtension
from corellium_api.models.user import User
from corellium_api.models.user_error import UserError
from corellium_api.models.v1_create_hook_parameters import V1CreateHookParameters
from corellium_api.models.v1_load_extension_parameters import V1LoadExtensionParameters
from corellium_api.models.v1_set_state_body import V1SetStateBody
from corellium_api.models.validation_error import ValidationError
from corellium_api.models.volume_options import VolumeOptions
from corellium_api.models.vpn_definition import VpnDefinition
from corellium_api.models.web_player_create_session_request import WebPlayerCreateSessionRequest
from corellium_api.models.web_player_session import WebPlayerSession
