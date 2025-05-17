from playwright.sync_api import sync_playwright
import pandas as pd
import time


url = "https://www.workingnomads.com/jobs"

jobs_data = []

with sync_playwright() as playwright_handle:

    browser = playwright_handle.chromium.launch(headless=False)

    page = browser.new_page()
    # time.sleep(5)
    page.goto(url, wait_until="load", timeout=30000)

    try:
        page.wait_for_selector("div.show-more")
        for i in range(6):
            page.click("div.show-more")
            time.sleep(5)
        page.wait_for_selector("div.job-desktop")
        jobs_desktops = page.locator("div.job-desktop").all()
        num = 0
        for job in jobs_desktops:
            company_name = job.locator("div.job-col div.company a").first.inner_text()
            job_title = job.locator("div.job-col h4 a").first.inner_text()
            job_link = job.locator("div.job-col h4 a") 
            job_link = "NA" if job_link.count() == 1 else job_link.all()[1].get_attribute("href")
            job_date = "NA"
            # job_source = "www.workingnomads.com"

            job_details ={
                "title":job_title,
                "company":company_name,
                "link":job_link,
                "date":job_date,
                "source":"www.workingnomads.com"
            }
            jobs_data.append(job_details)

    except Exception as e:
        print(e)


df = pd.DataFrame(jobs_data)

df.to_csv("../data/raw/workingnomads_jobs.csv", index=False)

print("done")