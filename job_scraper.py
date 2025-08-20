import argparse
import csv
import json
import time
import requests
from bs4 import BeautifulSoup

def scrape_stackoverflow(title, location, limit):
    """
    Scrapes jobs from Stack Overflow Jobs.
    """
    url = f"https://stackoverflow.com/jobs?q={title}&l={location}"
    print(f"Scraping Stack Overflow: {url}")
    jobs = []
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', class_='-job')

        for job in job_listings[:limit]:
            title_element = job.find('a', class_='s-link')
            company_element = job.find('h3', class_='fc-black-700').find_all('span')[0]
            location_element = job.find('span', class_='fc-black-500')

            job_title = title_element.text.strip() if title_element else 'N/A'
            company_name = company_element.text.strip() if company_element else 'N/A'
            job_location = location_element.text.strip() if location_element else 'N/A'
            job_url = "https://stackoverflow.com" + title_element['href'] if title_element else 'N/A'

            job_details = {
                "title": job_title,
                "company": company_name,
                "location": job_location,
                "url": job_url,
                "source": "Stack Overflow",
                "description": "N/A",
                "years_of_experience": "N/A",
                "date_posted": "N/A",
                "work_type": "N/A",
                "annual_base": "N/A",
                "type": "N/A",
                "level": "N/A"
            }

            try:
                if job_url != 'N/A':
                    time.sleep(1)
                    detail_response = requests.get(job_url, headers={'User-Agent': 'Mozilla/5.0'})
                    detail_response.raise_for_status()
                    detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

                    description_element = detail_soup.find('section', class_='fs-body2')
                    if description_element:
                        job_details['description'] = description_element.get_text(separator='\n').strip()

                    job_tags = detail_soup.find('ul', class_='d-inline-flex').find_all('a')
                    for tag in job_tags:
                        tag_text = tag.text.lower()
                        if 'full-time' in tag_text or 'part-time' in tag_text or 'contract' in tag_text:
                            job_details['type'] = tag.text
                        if 'senior' in tag_text or 'mid-level' in tag_text or 'junior' in tag_text:
                            job_details['level'] = tag.text
                        if 'remote' in tag_text or 'hybrid' in tag_text:
                            job_details['work_type'] = tag.text

                    date_posted_element = job.find('span', class_='fc-black-500')
                    if date_posted_element:
                        job_details['date_posted'] = date_posted_element.text.strip()

            except requests.exceptions.RequestException as e:
                print(f"Error scraping job detail page {job_url}: {e}")

            jobs.append(job_details)

    except requests.exceptions.RequestException as e:
        print(f"Error scraping Stack Overflow: {e}")

    return jobs

def scrape_remoteok(title, limit):
    """
    Scrapes jobs from Remote OK.
    """
    url = f"https://remoteok.io/remote-{title}-jobs"
    print(f"Scraping Remote OK: {url}")
    jobs = []
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('tr', class_='job')

        for job in job_listings[:limit]:
            title_element = job.find('h2', itemprop='title')
            company_element = job.find('h3', itemprop='name')
            location_element = job.find('div', class_='location')
            job_url_element = job.find('a', class_='preventLink', itemprop='url')

            job_title = title_element.text.strip() if title_element else 'N/A'
            company_name = company_element.text.strip() if company_element else 'N/A'
            job_location = location_element.text.strip() if location_element else 'Remote'
            job_url = "https://remoteok.io" + job_url_element['href'] if job_url_element else 'N/A'

            job_details = {
                "title": job_title,
                "company": company_name,
                "location": job_location,
                "url": job_url,
                "source": "Remote OK",
                "description": "N/A",
                "years_of_experience": "N/A",
                "date_posted": "N/A",
                "work_type": "Remote",
                "annual_base": "N/A",
                "type": "N/A",
                "level": "N/A"
            }

            try:
                if job_url != 'N/A':
                    time.sleep(1)
                    detail_response = requests.get(job_url, headers={'User-Agent': 'Mozilla/5.0'})
                    detail_response.raise_for_status()
                    detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

                    description_element = detail_soup.find('div', class_='description')
                    if description_element:
                        job_details['description'] = description_element.get_text(separator='\n').strip()

                    date_posted_element = job.find('time')
                    if date_posted_element:
                        job_details['date_posted'] = date_posted_element.text.strip()

                    salary_element = job.find('td', class_='salary')
                    if salary_element:
                        job_details['annual_base'] = salary_element.text.strip()

            except requests.exceptions.RequestException as e:
                print(f"Error scraping job detail page {job_url}: {e}")

            jobs.append(job_details)

    except requests.exceptions.RequestException as e:
        print(f"Error scraping Remote OK: {e}")

    return jobs

def save_to_csv(jobs, title, location):
    """
    Saves the job data to a CSV file.
    """
    filename = f"{title.replace(' ', '-').lower()}-{location.replace(' ', '-').lower()}-jobs.csv"
    print(f"Saving jobs to {filename}")
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        if not jobs:
            return
        fieldnames = jobs[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)

def save_to_json(jobs, title, location):
    """
    Saves the job data to a JSON file.
    """
    filename = f"{title.replace(' ', '-').lower()}-{location.replace(' ', '-').lower()}-jobs.json"
    print(f"Saving jobs to {filename}")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(jobs, f, indent=4)

def scrape_jobs(title, location, limit):
    """
    Main function to scrape jobs from various sites.
    """
    print(f"Scraping for {title} jobs in {location} with a limit of {limit} jobs.")
    all_jobs = []

    all_jobs.extend(scrape_stackoverflow(title, location, limit))
    all_jobs.extend(scrape_remoteok(title, limit))

    if all_jobs:
        save_to_csv(all_jobs, title, location)
        save_to_json(all_jobs, title, location)

    print(f"Scraping complete. Found {len(all_jobs)} jobs.")
    return all_jobs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape job listings from various websites.")
    parser.add_argument("title", type=str, help="Job title to search for (e.g., 'Data Engineer').")
    parser.add_argument("location", type=str, help="Location for the job search (e.g., 'San Francisco').")
    parser.add_argument("--limit", type=int, default=20, help="Maximum number of jobs to scrape.")

    args = parser.parse_args()
    scrape_jobs(args.title, args.location, args.limit)
