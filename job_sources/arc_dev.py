# import playwright
from playwright.sync_api import sync_playwright
# pnadas 
import pandas as pd
# time
import time

url = "https://arc.dev/remote-jobs"

jobs_data = []

with sync_playwright() as playwright_handle:

    browser = playwright_handle.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(url, wait_until="networkidle")

    page.wait_for_selector("input.MuiInputBase-input")

    # page.fill("input.MuiInputBase-input", "python")
    # time.sleep(1)
    # page.press("input.MuiInputBase-input", "Enter")

    try:
        page.wait_for_selector("div.job-card")
        jobs_cards = page.locator("div.job-card").all()

        for job in jobs_cards:

            company_name = job.locator("div.company-name").inner_text()
            job_title = job.locator("a.job-title").inner_text()
            job_link = job.locator("a.job-title").get_attribute("href")
            job_date = "N/A"

            job_details ={
                "title":job_title,
                "company":company_name,
                "link":job_link,
                "date":job_date,
                "source":"arc.dev"
            }
            jobs_data.append(job_details)

    except Exception as e:
        print(e)


df = pd.DataFrame(jobs_data)
df.to_csv("../data/raw/arc_dev_jobs.csv", index=False)