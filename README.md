# Bay Area Data Engineer Job Scraper

A comprehensive job scraper designed to find data engineer positions in the San Francisco Bay Area, California. This tool scrapes multiple job sites and APIs to gather the most relevant job listings.

## Features

- **Multiple Sources**: Scrapes from LinkedIn, Indeed, Glassdoor, Dice, GitHub Jobs, Stack Overflow, Remote OK, and more
- **Bay Area Focus**: Specifically targets San Francisco Bay Area locations
- **Duplicate Removal**: Automatically removes duplicate job listings
- **Multiple Output Formats**: Saves results in both CSV and JSON formats
- **API and Web Scraping**: Supports both API-based and web scraping approaches
- **Rate Limiting**: Respects website rate limits to avoid being blocked

## Bay Area Locations Covered

- San Francisco
- San Jose
- Oakland
- Palo Alto
- Mountain View
- Redwood City
- Sunnyvale
- Santa Clara
- Fremont
- Berkeley
- San Mateo
- Menlo Park
- Cupertino
- Milpitas
- Hayward

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Chrome/Chromium** (for Selenium-based scraping):
   - macOS: `brew install --cask google-chrome`
   - Ubuntu: `sudo apt-get install chromium-browser`
   - Windows: Download from https://www.google.com/chrome/

## Usage

### Option 1: Simple Scraper (Recommended for beginners)

The simple scraper uses basic web scraping and doesn't require API keys:

```bash
python simple_job_scraper.py
```

This will scrape:
- GitHub Jobs (API)
- Stack Overflow Jobs
- Remote OK
- AngelList
- Work at a Startup

### Option 2: API-Based Scraper (More reliable)

For better results, you can use the API-based scraper. You'll need to sign up for free API keys:

```bash
python api_job_scraper.py
```

**Required API Keys** (optional - the scraper will skip sources without keys):
- Adzuna: https://developer.adzuna.com/
- Reed: https://www.reed.co.uk/developers/
- USAJobs: https://developer.usajobs.gov/
- ZipRecruiter: https://www.ziprecruiter.com/developers

Set environment variables:
```bash
export ADZUNA_APP_ID="your_app_id"
export ADZUNA_APP_KEY="your_app_key"
export REED_API_KEY="your_api_key"
export USAJOBS_API_KEY="your_api_key"
export ZIPRECRUITER_API_KEY="your_api_key"
```

### Option 3: Full Selenium Scraper (Advanced)

For maximum coverage, use the full Selenium-based scraper:

```bash
python job_scraper.py
```

**Note**: This requires Chrome/Chromium and may be slower due to browser automation.

## Output Files

The scraper generates the following output files:

- `bay_area_data_engineer_jobs_simple.csv` - CSV format (Simple scraper)
- `bay_area_data_engineer_jobs_simple.json` - JSON format (Simple scraper)
- `bay_area_data_engineer_jobs_api.csv` - CSV format (API scraper)
- `bay_area_data_engineer_jobs_api.json` - JSON format (API scraper)
- `bay_area_data_engineer_jobs.csv` - CSV format (Full scraper)
- `bay_area_data_engineer_jobs.json` - JSON format (Full scraper)

## Sample Output

```json
{
  "title": "Senior Data Engineer",
  "company": "Tech Company Inc",
  "location": "San Francisco, CA",
  "type": "Full-time",
  "url": "https://example.com/job/123",
  "created_at": "2024-01-15T10:30:00Z",
  "source": "GitHub Jobs",
  "scraped_date": "2024-01-15 15:30:45"
}
```

## Configuration

You can modify the scraper behavior by editing the following parameters in the script files:

- `max_pages`: Number of pages to scrape per source
- `bay_area_locations`: List of Bay Area cities to include
- `time.sleep()` delays: Rate limiting between requests

## Troubleshooting

### Common Issues

1. **Chrome/Chromium not found**:
   - Install Chrome or update the ChromeDriver path
   - Use the simple scraper instead

2. **Rate limiting/Blocking**:
   - Increase delays between requests
   - Use API-based scraper instead of web scraping
   - Use a VPN or proxy

3. **No jobs found**:
   - Check your internet connection
   - Verify the target websites are accessible
   - Try different scraper options

4. **API errors**:
   - Verify API keys are correct
   - Check API rate limits
   - Ensure API keys have proper permissions

### Error Messages

- `"API credentials not found"`: Set the required environment variables
- `"Error scraping [source]"`: Network or parsing issue with that source
- `"No jobs data to save"`: No jobs were found or all sources failed

## Legal and Ethical Considerations

- **Respect robots.txt**: The scraper respects website robots.txt files
- **Rate limiting**: Built-in delays to avoid overwhelming servers
- **Terms of service**: Check each website's terms before scraping
- **Personal use**: Intended for personal job search only
- **No commercial use**: Do not use for commercial purposes without permission

## Contributing

Feel free to contribute by:
- Adding new job sources
- Improving error handling
- Optimizing performance
- Adding new output formats

## License

This project is for educational and personal use only. Please respect the terms of service of the websites being scraped.

## Disclaimer

This tool is provided as-is for educational purposes. Users are responsible for complying with website terms of service and applicable laws. The authors are not responsible for any misuse of this tool.
