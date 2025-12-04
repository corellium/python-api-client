# ConfigResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_site** | **bool** | Denotes whether it&#39;s an on-site install | [optional] 
**network_types** | **list[str]** | Valid network types (e.g. \&quot;nat\&quot;, \&quot;bridged\&quot;, \&quot;routed\&quot;) | [optional] 
**network_type** | **str** | Current network type setting | [optional] 
**show_domain_settings** | **bool** | Denotes whether to show domain settings | [optional] 
**version** | **str** | Denotes the version | [optional] 
**invalid_build** | **bool** | Denotes whether the build is invalid | [optional] 
**sep_sim** | **bool** | Denotes whether sepSim is enabled | [optional] 
**installer_available** | **bool** | Denotes whether installer is available | [optional] 
**invoiced_publishable_key** | **str** | API publishable key to use for Invoiced | [optional] 
**stripe_public_key** | **str** | Stripe public key | [optional] 
**intercom_id** | **str** | Intercom app ID, also known as workspace ID | [optional] 
**aux_webhook** | **str** | Webhook URL for aux | [optional] 
**gtm_id** | **str** | Google Tag Manager | [optional] 
**zapier_feedback_webhook** | **str** | Webhook URL to send feedback into Productboard automatically | [optional] 
**zapier_bugs_webhook** | **str** | Webhook URL to send frontend errors to Jira automatically | [optional] 
**billing_backend** | **str** | Default backend billing api name for new subscriptions (e.g. \&quot;stripe\&quot;) | [optional] 
**maintenance** | [**ConfigResponseMaintenance**](ConfigResponseMaintenance.md) |  | [optional] 
**logging** | [**Logging**](Logging.md) |  | [optional] 
**cloud_admin** | **str** | URL for cloud admin login | [optional] 
**files_admin** | **str** | URL for files admin login | [optional] 
**cloud_domain** | **str** | Cloud domain name (usually corellium.com or staging.corellium.com) | [optional] 
**billing_domain** | **str** | Billing domain name | [optional] 
**app_domain** | **str** | App domain name (usually app.corellium.com or app.staging.corellium.com) | [optional] 
**max_network_monitor_file_size** | **str** | Maximum network monitor file size | [optional] 
**enable_firmware_image_upload** | **bool** | Denotes whether users can upload firmware images | [optional] 
**auth_providers** | [**list[AuthProvider]**](AuthProvider.md) | Auth providers | [optional] 
**snapshot_limit** | **float** | Maximum number of snapshots to allow | [optional] 
**max_kernel_size** | **float** | The maximum size, in bytes, (default: 100 MB) that an uploaded kernel should be | [optional] 
**max_ramdisk_size** | **float** | The maximum size, in bytes, (default: 500 MB) that an uploaded ramdisk should be | [optional] 
**charm_sdk** | **str** | Denotes whether charmSDK is enabled | [optional] 
**trial** | [**Trial**](Trial.md) |  | [optional] 
**sentry_url** | **str** | Sentry URL | [optional] 
**domain_authentication_providers** | **bool** | If enabled, adds the default providers in their current configuration | [optional] 
**default_ssid** | **str** | The configured Default SSID from /etc/corellium/setup.json | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


