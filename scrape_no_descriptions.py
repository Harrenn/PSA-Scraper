import requests
from bs4 import BeautifulSoup
import csv

# Replace this URL with the actual URL of the webpage you want to scrape
url = 'https://psa.gov.ph/classification/psic/class'

# Send a request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table by its id
table = soup.find('table', id='psicdata')

# Open a new CSV file in write mode
with open('scraped_table.csv', 'w', newline='', encoding='utf-8') as csvfile:
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

print("Data has been successfully saved to scraped_table.csv")
