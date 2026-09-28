# Web Scraper

A simple Streamlit web app that fetches a web page and displays its title and the links found in its HTML.

## Features

- Enter a page URL in the app.
- View the page title, when one is present.
- View the `href` values from the page's anchor (`<a>`) elements.
- Peach-themed Streamlit interface.

## Requirements

- Python with `pip`
- An internet connection to fetch the page you want to inspect

## Setup

Open PowerShell in the project folder and create a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks virtual-environment activation, use the environment's Python directly instead:

```powershell
py -m pip install -r requirements.txt
```

## Run

From the project folder, run:

```powershell
streamlit run web-scraperui.py
```

Streamlit will print a local URL to open in your browser. Enter a complete URL, including `https://` or `http://`, and select **Submit**. Once the URL is verified, select **Get Details** to display the title and links.

## Notes

- The app reads the HTML returned by the web server. Content and links added later by JavaScript may not appear.
- Only anchor `href` values are shown; link text and other page content are not extracted.
- Scrape only pages you are permitted to access, and respect the site's terms and policies.