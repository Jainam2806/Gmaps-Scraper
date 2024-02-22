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
