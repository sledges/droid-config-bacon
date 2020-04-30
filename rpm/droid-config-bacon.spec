# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device bacon
%define vendor oneplus
%define rpm_device bacon   
%define rpm_vendor oneplus
%define vendor_pretty OnePlus
%define device_pretty One
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0
# We assume most devices will
%define have_modem 1

# Community HW adaptations need this
%define community_adaptation 1
# OTA via self-hosted repo needs to have all adaptation-community repos removed
Conflicts: community-adaptation-testing
Obsoletes: community-adaptation-testing

# For bluez5
%define ofono_enable_plugins bluez5,hfp_ag_bluez5
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

%include droid-configs-device/droid-configs.inc
