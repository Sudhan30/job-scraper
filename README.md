# Job Scraper

A simple and customizable job scraper to find job listings from various mainstream sites.

## Features

- **Multiple Sources**: Scrapes from Stack Overflow and Remote OK. Note: Sites like LinkedIn, Indeed, and Glassdoor are not included in this version due to their strong anti-scraping measures and terms of service.
- **Customizable Search**: Filter jobs by title and location.
- **Multiple Output Formats**: Saves results in both CSV and JSON formats.
- **Detailed Information**: Extracts job title, description, location, type, and more.

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scraper from your terminal with the job title and location you want to search for.

```bash
python job_scraper.py "Software Engineer" "New York" --limit 10
```

### Arguments

- `title`: The job title to search for (e.g., "Data Scientist").
- `location`: The location to search in (e.g., "London").
- `--limit`: (Optional) The maximum number of jobs to scrape per site. Defaults to 20.

## Output Files

The scraper generates CSV and JSON files with the scraped job data, named according to the search query. For example:

- `software-engineer-new-york-jobs.csv`
- `software-engineer-new-york-jobs.json`

## Sample Output (JSON)

```json
[
    {
        "title": "Senior Software Engineer",
        "company": "Tech Solutions Inc.",
        "location": "New York, NY",
        "url": "https://stackoverflow.com/jobs/12345/senior-software-engineer-tech-solutions-inc",
        "source": "Stack Overflow",
        "description": "We are looking for a Senior Software Engineer to join our team...",
        "years_of_experience": "N/A",
        "date_posted": "2 days ago",
        "work_type": "Full-Time",
        "annual_base": "N/A",
        "type": "Full-Time",
        "level": "Senior"
    }
]
```

## Legal and Ethical Considerations

- **Respectful Scraping**: The scraper includes delays to avoid overwhelming job site servers.
- **Terms of Service**: Please be aware of the terms of service of the websites you are scraping. This tool is intended for personal and educational use only.
- **No Commercial Use**: Do not use this tool for commercial purposes without permission from the website owners.

## Disclaimer

This tool is provided as-is. The user is responsible for complying with all applicable laws and website terms of service.
