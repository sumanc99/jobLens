# import the playwright library specifically working with in sync form
from playwright.sync_api import sync_playwright
# importing pandas for data saving and manipulation
import pandas as pd
# importing time to slow the script down
import time

# url of the site 
url = "https://remoteok.com/"

jobs_data = []

# handles infinity scroll base on new image load every time
def scroll_by_image_count(page,scroll_pause=2, max_scroll=30):
    # current image count
    current_image_count = 0

    # scroll the page down to the bottom for some range
    for _ in range(max_scroll):
        page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(scroll_pause)
    
        new_image_count = len(page.locator("td.image").all())

        if current_image_count == new_image_count:
            break
        current_image_count = new_image_count


# using the playwright in context 
with sync_playwright() as playwright_handle:

    # Launching a Chromium Browser instance (not headless mode)
    browser = playwright_handle.chromium.launch(headless=False)

    # opening a new browser page
    page = browser.new_page()

    # navigating to the desired URL
    page.goto(url)

    # scroll_by_image_count(page)

    scroll_by_image_count(page,5)

    # wait till the class .job is loaded
    page.wait_for_selector(".job",timeout=15000)
    # wait again just to be safe
    time.sleep(2)



    # locating the container for each in the site
    jobs = page.locator(".job").all()

    # looping through the jobs to extract it details
    for job in jobs:
        job_title = job.locator("h2").inner_text()
        job_company = job.locator("span.companyLink    h3").inner_text()
        job_link = job.locator("a.preventLink").all()
        job_date = job.locator("td.time time").get_attribute("datetime")

        job_details ={
            "title":job_title,
            "company":job_company,
            "link":f"{[job.get_attribute("href") for job in job_link][0]}",
            "date":job_date,
            "source":"RemoteOK"
        }
        jobs_data.append(job_details)


df = pd.DataFrame(jobs_data)

print(df.info())

df.to_csv("../data/raw/romote_ok_jobs.csv", index=False)
