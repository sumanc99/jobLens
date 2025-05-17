# jobLens
 <p>is an automated job listing scraper and notifier that collects remote job opportunities from multiple websites, filters them based on your preferences (keywords, location), and sends notifications via Email or Telegram.</p>

# Features
🌐 Scrapes remote job boards (e.g., RemoteOK, Arc.dev, We Work Remotely)

🔍 Filters jobs based on keywords and locations

📬 Sends notifications through Email and Telegram

🧠 Deduplicates repeated listings

📅 Runs automatically on a schedule

🧪 Modular and testable structure

# 🗂️ Project Structure

<pre lang="markdown">
smart_job_aggregator/
│
├── config/                  # Config files (API keys, email, Telegram tokens)
│   └── settings.yaml
│
├── data/                    # Temporary or saved data (e.g., raw and filtered job listings)
│   ├── raw/
│   └── filtered/
│
├── jobsources/             # Each job board gets its own scraping module
│   ├── __init__.py
│   ├── remoteok.py
│   ├── arc_dev.py
│   └── weworkingnomad.py
│
├── notifier/               # Notification modules
│   ├── email_notifier.py
│   └── telegram_notifier.py
│
├── core/                   # Business logic
│   ├── scraper.py          # Unified scraper that calls each job board
│   ├── filter.py           # Keyword/location filtering logic
│   ├── deduplicate.py      # Remove duplicate jobs
│   └── scheduler.py        # Automation and scheduling
│
├── utils/                  # Common helper functions
│   ├── logger.py
│   └── formatter.py
│
├── tests/                  # Unit tests
│
├── main.py                 # Entrypoint for running everything
├── requirements.txt        # Dependencies
</pre>

# ⚙️ How It Works
Scraper gathers job postings from supported sites.

Filter removes irrelevant jobs based on user-defined keywords and locations.

Deduplicator checks for and removes repeated job listings.

Notifier sends the remaining job opportunities to you via email or Telegram.

Scheduler runs the entire process automatically based on a time interval.
