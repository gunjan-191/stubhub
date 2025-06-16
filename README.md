# StubHub Sports Events Scraper
A simple Scrapy spider to extract sports event data from [StubHub](https://www.stubhub.com)'s explore page using its internal API.
---
##  Project Purpose

This project demonstrates how to build a Scrapy spider that extracts event data like:

- Title (Event name)  
- Date and Time  
- Location  
- Event Image  
- Event Page URL
---
## Technologies Used

- Python 3.10+
- Scrapy (Web scraping framework)

---

---

## How to Run the Spider

### 1. Clone the Repository
------------------------------------------------------------------
****git clone https://github.com/<your-username>/stubhub_scraper.git
****cd stubhub_scraper
-----------------------------------------------------------------------
2. Install Dependencies
--------------------------------------------
It's recommended to use a virtual environment.
-------------------------------------------
**pip install scrapy**
-------------------------------------------
|||||||||||||||||||||||||||||||||||||||||||||
3. Run the Spider
---------------------------------------------
**scrapy crawl event**
----------------------------------------------
This will generate a file events.json with the scraped data.

||||||||||||||||||||||||||||||||||||||
Sample Output json
----------------------------------
{
  "name": "NBA Finals: Game 6",
  "image_url": "https://images.stubhub.com/event-image.jpg",
  "url": "https://www.stubhub.com/event/nba-finals-game-6",
  "location": "Chase Center, San Francisco, CA",
  "datetime": "June 14 7:00 PM"
}
--------------------------------------------------

||||||||||||||||||||||||||||||||||||||||||||||||||||
How It Works
---------------------------------------------
**The spider sends HTTP requests to StubHub's explore API endpoint.

It parses the JSON response to extract key information.

The data is yielded as structured JSON items.

Notes
----------------------------------------------
The API being used is internal and might require updates if StubHub changes its structure.

This project is for educational/demo purposes only.


Author
Gunjan Sachdeva


