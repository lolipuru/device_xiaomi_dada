#
# Copyright (C) 2023 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/dada

# Inherit from sm8650-common
include device/xiaomi/sm8750-common/BoardConfigCommon.mk

# Display
TARGET_SCREEN_DENSITY := 520

# Inherit from the proprietary version
include vendor/xiaomi/dada/BoardConfigVendor.mk