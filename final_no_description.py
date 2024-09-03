import subprocess
import sys

# Function to install a package if not already installed
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Package '{package}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    else:
        print(f"Package '{package}' is already installed.")

# Check and install necessary packages
install_package('requests')
install_package('bs4')

# Now that packages are installed, we can safely import them
import requests
from bs4 import BeautifulSoup
import csv

# Prompt user for the website URL
url = input("Enter the URL of the webpage you want to scrape: ")

# Send a request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table by its id (assuming the id is known and remains the same)
table = soup.find('table', id='psicdata')

# Check if the table was found
if not table:
    print("Table with id 'psicdata' not found.")
    exit()

# Prompt user for the filename to save the data
filename = input("Enter the filename to save the scraped data (with .csv extension): ")

# Open a new CSV file in write mode
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['Group Description Title', 'Group Code'])
    
    # Loop through all rows in the table body
    for row in table.find('tbody').find_all('tr'):
        # Extract columns
        cols = row.find_all('td')
        
        # Safely extract the title from the <a> tag inside the first column
        title = cols[0].find('a').text.strip() if cols[0].find('a') else "No title found"
        
        # Get the Group Code from the second column
        group_code = cols[1].text.strip()
        
        # Write the title and group code to the CSV file
        writer.writerow([title, group_code])

print(f"Data has been successfully saved to {filename}")
