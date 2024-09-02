import requests
from bs4 import BeautifulSoup
import csv

# Replace this URL with the actual URL of the webpage you want to scrape
url = 'https://psa.gov.ph/classification/psic/group'

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
    writer.writerow(['Group Description', 'Group Code'])
    
    # Loop through all rows in the table body
    for row in table.find('tbody').find_all('tr'):
        # Extract columns
        cols = row.find_all('td')
        
        # Initialize an empty string for the Group Description
        description = ""

        # Iterate through the contents of the first <td> element
        for content in cols[0].contents:
            # Add text and line breaks where appropriate
            if content.name == 'a':
                description += content.text.strip()
            elif content.name == 'p':
                description += "\n\n" + content.text.strip()
            elif isinstance(content, str):
                description += content.strip()

        # Get the Group Code from the second column
        group_code = cols[1].text.strip()
        
        # Write the formatted row to the CSV file
        writer.writerow([description.strip(), group_code])

print("Data has been successfully saved to scraped_table.csv")
