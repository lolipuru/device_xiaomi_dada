#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm8750-common',
    'hardware/qcom-caf/sm8750',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/xiaomi/sm8750-common',
]

blob_fixups: blob_fixups_user_type = {
    (
        'odm/etc/camera/motiontuning.xml',
        'odm/etc/camera/snsc_bokeh_motiontuning.xml',
        'odm/etc/camera/snsc_enhance_motiontuning.xml',
        'odm/etc/camera/snsc_noface_motiontuning.xml',
        'odm/etc/camera/enhance_motiontuning.xml',
        'odm/etc/camera/snsc_motiontuning.xml'
    ): blob_fixup()
        .regex_replace('xml=version', 'xml version'),
    (
    'vendor/lib64/libcameraopt.so',
    ): blob_fixup().add_needed('libprocessgroup_shim.so'),
    (
        'odm/lib64/libMiEmojiEffect.so',
        'odm/lib64/libMiVideoFilter.so',
        'odm/lib64/libAncHumanPreviewBokeh.so',
        'odm/lib64/libTrueSight.so',
        'odm/lib64/libwa_widelens_undistort.so',
        'vendor/lib64/libMiPhotoFilter.so'
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_isSupported'),
    (
       'vendor/lib64/camera/components/com.qti.node.dewarp.so',
       'vendor/lib64/hw/com.qti.chi.override.so',
       'vendor/lib64/libcamximageformatutils.so',
       'vendor/lib64/libchifeature2.so',
       'vendor/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so',
    ): blob_fixup()
        .remove_needed('android.hardware.graphics.allocator-V1-ndk.so'),
    (
       'vendor/lib64/vendor.xiaomi.hardware.camera.injection-V1-ndk.so',
       'vendor/lib64/vendor.xiaomi.hardware.camera.injection-client.so',
       'vendor/lib64/vendor.xiaomi.hardware.camera.injection-service.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.camera.device-V1-ndk.so',
            'android.hardware.camera.device-V2-ndk.so'
        ),
    (
       'vendor/lib64/hw/camera.qcom.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.sensors-V2-ndk.so',
            'android.hardware.sensors-V3-ndk.so'
        ),
    'vendor/lib64/libultrahdr_dada.so': blob_fixup()
        .replace_needed(
            'libjpegencoder.so',
            'libjpegencoder_dada.so'
        )
        .replace_needed(
            'libjpegdecoder.so',
            'libjpegdecoder_dada.so'
        ),
    ('odm/lib64/camera/plugins/com.xiaomi.plugin.jpegrAggr.so', 'odm/lib64/camera/plugins/com.xiaomi.plugin.gainmap.so'): blob_fixup()
        .replace_needed(
            'libultrahdr.so',
            'libultrahdr_dada.so'
        ),
}

module = ExtractUtilsModule(
    'dada',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8750-common', module.vendor
    )
    utils.run()