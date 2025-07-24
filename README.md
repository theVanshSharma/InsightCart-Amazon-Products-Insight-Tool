# InsightCart-Amazon-Products-Insight-Tool

InsightCart is a local web app built using Python and Streamlit that scrapes product information from Amazon product pages.  
It extracts key details like Title, Price, Rating, Reviews, and Availability, and allows users to download the data as an Excel file.

# Not on Deployment
**Disclaimer:** Amazon blocks scraping from cloud-hosted environments like Streamlit Community Cloud.  
This app is designed to be run locally on your machine for educational purposes.


# Features
- 🛒 Scrape product details from Amazon using just a URL
- 📊 Add multiple products in a single session
- 💾 Export product data as Excel (.xlsx)
- 💡 Built with Streamlit, BeautifulSoup, and pandas

# Tech Stack
- Python
- Streamlit
- BeautifulSoup
- Pandas
- Requests
- OpenPyXL

# Run it locally
- Clone the repo: 
  - git clone https://github.com/theVanshSharma/InsightCart-Amazon-Products-Insight-Tool.git
  - cd insightcart

- Install dependencies:
  - pip install -r requirements.txt

- Run Streamlit:
  - streamlit run main.py


