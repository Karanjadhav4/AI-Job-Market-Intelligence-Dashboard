import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

def scrape_linkedin_jobs(keyword="data scientist", location="India", pages=3):

    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    jobs = []

    for page in range(pages):

        url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&location={location}&start={page*25}"

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        job_cards = soup.find_all("li")

        for job in job_cards:
            title = job.find("h3")
            company = job.find("h4")
            location = job.find("span", class_="job-search-card__location")
            link = job.find("a")

            jobs.append({
                "title": title.text.strip() if title else None,
                "company": company.text.strip() if company else None,
                "location": location.text.strip() if location else None,
                "link": link["href"] if link else None
            })

    df = pd.DataFrame(jobs)

    return df