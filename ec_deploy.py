import subprocess

import sys
from time import sleep

cp = subprocess.Popen(['ssh', '-i', '/Users/eugenm/Desktop/frankfurt_key.pem', 'ubuntu@18.194.213.34'], stdin=subprocess.PIPE)
sleep(1)
cp.stdin.write(bytes('cd apps/automation-blog\n', encoding='utf-8'))

cp.stdin.write(bytes('git reset --hard\n', encoding='utf-8'))

cp.stdin.write(bytes('git checkout develop\n', encoding='utf-8'))

cp.stdin.write(bytes('git pull\n', encoding='utf-8'))

cp.stdin.write(bytes('cd ../..\n', encoding='utf-8'))

cp.stdin.write(bytes('sudo venvs/automation-blog/bin/python apps/automation-blog/automation_blog/manage.py runserver 0:80&\n', encoding='utf-8'))


out = cp.communicate()[0]
print(out)
