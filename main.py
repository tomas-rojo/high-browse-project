# Imports
from bs4 import BeautifulSoup
from db import db
import time
import os
from dotenv import load_dotenv 

load_dotenv()

# Initializing DB 
db.create_table()  

start_time = time.time()

# Opens and reads the xml file depending on the APP_ENV
env = os.environ.get("APP_ENV")

if env == "prod":
    print("*** RUNNING ON PROD MODE ***")
    # Opens and reads the xml file
    with open('files/sample.xml', 'r') as f:
        file = f.read()
else:
    with open('files/sample_dev.xml', 'r') as f:
        file = f.read()

# Initializing soup variable
soup = BeautifulSoup(file, 'xml')

print("Parsing data... This might take a moment...")

# Finding <VALUE> tags and getting the value and its parent tag
values = soup.find_all('VALUE')

for value in values:

    # value.parent.name : Refers to the parent tag of the <VALUE> tag
    # value.text : Inner data from the <VALUE> tag

    db.insert_data(value.parent.name, value.text)

print("--- %s seconds ---" % (time.time() - start_time))
