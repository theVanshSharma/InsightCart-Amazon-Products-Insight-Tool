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

- Install dependencies:
  - pip install -r requirements.txt

- Run Streamlit:
  - streamlit run main.py

#Amazon Product Scraper Screenshot<img width="1014" height="562" alt="image" src="https://github.com/user-attachments/assets/d5e51309-d489-4ac1-8155-26fc07cd0944" />

#Drop the Product URL<img width="956" height="767" alt="image" src="https://github.com/user-attachments/assets/aacd7e88-25fb-42eb-b057-407e3b8a8aab" />

#Download Excel Sheet of the insights<img width="1914" height="181" alt="image" src="https://github.com/user-attachments/assets/a63ff95e-8352-4c39-be82-91461e4c06a3" />

