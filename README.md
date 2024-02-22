# Google Maps Scraper
## Description

This Python script allows you to scrape Google Maps for a given query. It utilizes Selenium to interact with the Google Maps web interface.

## Requirements

Ensure you have the following installed:

- Python 3
- Selenium
- Google Chrome

You can install the necessary Python packages by running:
```bash
pip install -r requirements.txt
```
## Usage
Clone the repository:
```bash
git clone https://github.com/Jainam2806/Gmaps-Scraper.git
```

Navigate to the repository directory:
```bash
cd Gmaps-Scraper\webScrapper
```

Run the script:
```bash
python scraper.py
```

Enter your search query when prompted.

## Functionality
The script scrapes Google Maps for the given query and prints out the search results.

Example:
```bash
Search query: restaurants near me
```
Output:
```bash
Name: The Grand Thakar
Address: Opp. Nagri Hospital, Ellisbridge, Ahmedabad, Gujarat 380006, India
Rating: 4.2
Phone: +91 79 2640 3333
______________________________________________________________________________________________________
Name: Agashiye
Address: The House of MG, Sidi Saiyad Jali, Lal Darwaja, Ahmedabad, Gujarat 380001, India
Rating: 4.5
Phone: +91 79 2550 6946
______________________________________________________________________________________________________
Name: Toran Dining Hall
Address: Opposite Sales India, Ashram Rd, Ahmedabad, Gujarat 380009, India
Rating: 4.1
Phone: +91 79 2658 8080
______________________________________________________________________________________________________
...

```
