from bs4 import BeautifulSoup
import os

# Function to calculate total sales for "Gold" ticket type
def calculate_total_sales(directory):
    total_sales = 0.0
    
    # Loop through all HTML files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r') as file:
                # Parse the HTML content
                soup = BeautifulSoup(file, 'html.parser')
                
                # Find all tables
                tables = soup.find_all('table')
                
                for table in tables:
                    # Find all rows in the table
                    rows = table.find_all('tr')
                    
                    for row in rows[1:]:  # Skip header row
                        cells = row.find_all('td')
                        
                        if len(cells) >= 3:
                            ticket_type = cells[0].text.strip().lower()  # Normalize case for 'Type'
                            units = float(cells[1].text.strip())
                            price = float(cells[2].text.strip())
                            
                            # Check if the type is 'gold' (case-insensitive)
                            if ticket_type == 'gold':
                                total_sales += units * price
    
    return round(total_sales, 2)

# Path to the directory containing the HTML files
directory_path = r'C:\Users\Varshith Chowdary\Desktop\STR\uz'

# Calculate total sales for "Gold" ticket type
total_sales = calculate_total_sales(directory_path)

# Output the total sales
print(f'Total sales for "Gold" ticket type: ${total_sales}')
