# через ADB
# adb devices
# adb shell getprop ro.product.model.

import subprocess

def get_device_name():
    result = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.model'], capture_output=True, text=True)
    return result.stdout.strip()

device_name = get_device_name()
print(device_name)

# ___________________________________________________________
# ниже если библиотеку устанавливать
import android

droid = android.Android()
device_info = droid.getDeviceInfo()
model = device_info['model']
print(model)