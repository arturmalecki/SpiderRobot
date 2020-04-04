import os
from dotenv import load_dotenv

load_dotenv()
print("Creating project direct if not exit: " + os.getenv("PI_SOFTWARE_DIR"))
os.system('ssh $PI_USERNAME@$PI_HOST "mkdir $PI_SOFTWARE_DIR"')
print("Syncing code")
os.system('rsync -avz ./* $PI_USERNAME@$PI_HOST:$PI_SOFTWARE_DIR')
print("Done")