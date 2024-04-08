# Google Maps Scraper
## Description

This script scrapes Google Maps for a user-provided query and retrieves information about the search results. It mimics user interactions on the Google Maps website to perform the search and extracts relevant information from the search results.

## Requirements

Ensure you have the following installed:

- Python 3
- Selenium
- Google Chrome

## Usage
Clone the repository:
```bash
git clone https://github.com/Jainam2806/Gmaps-Scraper.git
```

Navigate to the repository directory:
```bash
cd .\Gmaps-Scraper\
git checkout version-1
cd .\webScrapper\
```

You can install the necessary Python packages by running:
```bash
pip install -r requirements.txt
```

Run the script:
```bash
python scraper.py
```

Enter your search query when prompted.

## Functionality
The script scrapes Google Maps for the given query and prints out the search results.

Search Query:
```bash
Restaurants near me
```
Output:
```bash
{
    1: {
        'shop_name': 'Honest', 
        'shop_address': 'Indian · White House Panchvati Circle, Chimanlal Girdharlal Rd', 
        'shop_phone': None}, 
    2: {
        'shop_name': 'Chinese Wok - CG Road', 
        'shop_address': 'Chinese · Shop No.1, Ground Floor, Opp: Tomato Restaurant, Gold Leaf, Chimanlal Girdharlal Rd, near Maradia Plaza, near Associated Petrol Pump', 
        'shop_phone': None}, 
    3: {
        'shop_name': 'Cafe Mocha', 
        'shop_address': 'Restaurant · 10, Vasantbaug society, Gulbai Tekra Rd, opp. IDBI Bank, near CA Circle', 
        'shop_phone': None}, 
    4: {
        'shop_name': 'Hocco Eatery, Law Garden', 
        'shop_address': 'Restaurant · Ground floor, shri balaji alpha bazar law garden', 
        'shop_phone': None}, 
    5: {
        'shop_name': 'The Great Kabab Factory', 
        'shop_address': 'Mughlai · Radisson Blu Hotel, Ambawadi, Panchavati Road, Ellisbridge', 
        'shop_phone': None},
    ...
}
```