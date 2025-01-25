import subprocess

# subprocess.run(['adb', 'shell', 'input keyevent 4'])
#
#
# img_raw = subprocess.run(['C:\\platform-tools\\adb.exe', 'exec-out', 'screencap',
#                                   '-p'], stdout=subprocess.PIPE).stdout  # получаем файл



x, y = 230, 240
x, y = 410, 40

subprocess.run(['adb', 'shell', f'input tap {x} {y}'])