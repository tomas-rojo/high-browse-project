from bs4 import BeautifulSoup
from db import db
import time

start_time = time.time()

# Opens and reads the xml file
with open('files/sample_dev.xml', 'r') as f:
    file = f.read()

# Initializing soup variable
soup = BeautifulSoup(file, 'xml')

# Initializing DB 
db.create_table()   

print("Parsing data... This may take a moment...")

# Finding <VALUE> tags and getting the value and its parent tag
values = soup.find_all('VALUE')
#for value in values:
#    db.insert_data(value.parent.name, value.text)

print("--- %s seconds ---" % (time.time() - start_time))
