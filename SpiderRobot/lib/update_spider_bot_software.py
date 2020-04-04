import os
from dotenv import load_dotenv

load_dotenv()
print("---> Updating Spider Bot Software")
os.system('rsync -avzh $PI_USERNAME@$PI_HOST:~/Projects/SpiderBot ./')
print("Done")
