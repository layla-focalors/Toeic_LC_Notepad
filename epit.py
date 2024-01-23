import os
import datetime
import time

while True:
    value = 'Commit For Update' + str(datetime.datetime.now().timestamp())
    os.system('git add .')
    os.system('git status')
    os.system(f'git commit -m "{value}"')
    os.system('git push')
    print(f"Last Commit : {datetime.datetime.now()}")
    time.sleep(100)