#
# Copyright (C) 2024 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from dada device.
$(call inherit-product, device/xiaomi/dada/device.mk)

## Device identifier
PRODUCT_DEVICE := dada
PRODUCT_NAME := lineage_dada
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := 24129PN74C
PRODUCT_MANUFACTURER := xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc=$(call normalize-path-list, "dada dada 15 AQ3A.240812.002 OS2.0.206.0.VOCCNXM:user release-keys")

BUILD_FINGERPRINT := Xiaomi/dada/dada:15/AQ3A.240812.002/OS2.0.206.0.VOCCNXM:user/release-keys

# GMS
PRODUCT_GMS_CLIENTID_BASE := android-xiaomi