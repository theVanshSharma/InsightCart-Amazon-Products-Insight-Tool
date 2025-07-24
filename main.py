from bs4 import BeautifulSoup
import requests
import streamlit as st
import pandas as pd
from io import BytesIO

def main(url):
    # file = open('out.csv', 'a')
    HEADER = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'})
    

    webpage = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(webpage.content,'lxml')

    # retrieving product title

    try:
        title = soup.find('span',attrs={'id': 'productTitle'})
        title_content = title.string
        title_name = title_content.strip().replace(',',' ')

    except AttributeError:
        title_name = 'N/A'
    print('title: ',title_name)
    # file.write(f"{title_name},")

    # retrieving product price

    try:
        # price_curr = soup.find('span', attrs={'class': 'a-price-symbol'}).string
        price_value = soup.find('span', attrs={'class': 'a-price-whole'}).text
        # price_value = price_curr + price
    except AttributeError:
        price_value = 'N/A'
    print('price: ',price_value)
    # file.write(f"{price_value},")

    # retrieving product rating

    try:
        rating = soup.find('span',attrs={'class':'a-icon-alt'}).string
        rating_value = rating.strip().replace(',',' ')
    except AttributeError:
        rating_value = 'N/A'
    print('rating: ',rating_value)
    # file.write(f"{rating_value},")


    # retrieving review count
    
    try:
        review_count = soup.find('span', attrs={'id': 'acrCustomerReviewText'}).string
    except AttributeError:
        review_count = 'N/A'
    print('review count: ',review_count)
    # file.write(f"{review_count},")

    # retrieving availability

    try:
        status = soup.find('div', attrs={'id': 'availability'})
        status_value = status.find('span').string
    except AttributeError:
        status_value = 'N/A'
    print('availability: ',status_value)
    # file.write(f"{status_value}\n")

    # file.close()

    return {
        'title': title_name,
        'price': price_value,
        'rating': rating_value,
        'review_count': review_count,
        'availability': status_value
    }


if __name__ == "__main__":
    st.title("InsightCart: Amazon Products Insight Tool")

    if 'product_list' not in st.session_state:
        st.session_state.product_list = []

    st.subheader(" What does this tool do?")
    st.write("InsightCart lets you extract and analyze essential product information from any Amazon product page — including title, price, rating, reviews, and availability. Use it to compare products, or personal decision-making. The results can be viewed instantly and downloaded as an Excel file.")

    st.write("Get smart insights before you shop – just drop the Amazon product URL.")
    url = st.text_input("Amazon Product URL")
    if url:
        if st.button("Scrape"):
            result = main(url)
            result['url'] = url
            st.session_state.product_list.append(result)
            st.success("Scraping completed!: ")
    
    if st.session_state.product_list:
            st.subheader("Scraped Products")
            df = pd.DataFrame(st.session_state.product_list)
            st.dataframe(df)
            

            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index = False, sheet_name='Amazon Product Data')
            processed_data = output.getvalue()
            
            st.download_button(
                label="Download Excel File",
                data=processed_data,
                file_name='amazon_product_data.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )


