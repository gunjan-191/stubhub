import scrapy
import json

class EventSpider(scrapy.Spider):
    # Unique name for the spider, used to run it via CLI
    name = 'event'

    # Restricts the crawler to this domain
    allowed_domains = ['stubhub.com']

    # Initial URL (not directly used for scraping, just a placeholder)
    start_urls = ["https://www.stubhub.com"]

    def start_requests(self):
        """
        This function overrides the default start_requests.
        It constructs URLs for the first 5 pages of StubHub's Explore API.
        """
        for page in range(1, 6):  # Scrape first 5 pages
            url = f'https://www.stubhub.com/explore?method=getExploreEvents&lat=NDAuNzEyNzc1Mw%3D%3D&lon=LTc0LjAwNTk3Mjg%3D&to=253402300799999&page={page}&tlcId=2'

            # Yield a request to each URL, calling the parse() method on response
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        """
        This function handles the response for each event page.
        It parses the JSON and extracts the required event fields.
        """
        self.logger.info(f"Status Code: {response.status}")  # Log HTTP status

        try:
            # Try to load the response body as JSON
            data = response.json()
        except Exception as e:
            # If parsing fails, log the error and skip this response
            self.logger.error(f"Failed to parse JSON: {e}")
            return

        # Get the list of events from JSON data
        events = data.get("events", [])

        # Loop through each event and extract relevant details
        for event in events:
            name = event.get("name")  # Event title
            image_url = event.get("imageUrl")  # Event image
            url = event.get("url")  # Link to event page
            location = event.get("formattedVenueLocation")  # Location string
            date = event.get("formattedDateWithoutYear")  # Date without year
            time = event.get("formattedTime")  # Event time
            datetime = f"{date} {time}"  # Combine date and time

            # Log the extracted information (optional, for debugging)
            self.logger.info(f"Event: {name}")
            self.logger.info(f"Image: {image_url}")
            self.logger.info(f"URL: {url}")
            self.logger.info(f"Location: {location}")
            self.logger.info(f"Datetime: {datetime}")

            # Yield the data as a dictionary
            yield {
                "name": name,
                "image_url": image_url,
                "url": url,
                "location": location,
                "datetime": datetime
            }
