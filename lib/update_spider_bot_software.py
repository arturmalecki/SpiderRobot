import os
from dotenv import load_dotenv

load_dotenv()
print("---> Updating Spider Bot Software")
os.system('rsync -avz ./* $PI_USERNAME@$PI_HOST:~/Projects/SpiderRobot')
print("Done")
