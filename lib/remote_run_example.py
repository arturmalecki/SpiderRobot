import os
from dotenv import load_dotenv

load_dotenv()
print("---> Creating project direct if not exit: " + os.getenv("PI_SOFTWARE_DIR"))
os.system('ssh $PI_USERNAME@$PI_HOST "mkdir $PI_SOFTWARE_DIR"')
# print("---> Syncing code")
# os.system('rsync -avz ./* $PI_USERNAME@$PI_HOST:$PI_SOFTWARE_DIR')
os.system('bin/update_spider_bot_software.sh')
print("---> Starting software")
os.system('ssh $PI_USERNAME@$PI_HOST "cd $PI_SOFTWARE_DIR; python3 test_files/button_led_test.py"')
print("Done")