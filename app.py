import streamlit as st
import pandas as pd
from scraper import scrape_linkedin_jobs
from preprocess import clean_jobs

st.title("Real-Time Data Science Job Market Analyzer")

keyword = st.text_input("Job Role", "Data Scientist")
location = st.text_input("Location", "India")

if st.button("Scrape Jobs"):

    with st.spinner("Scraping LinkedIn Jobs..."):

        df = scrape_linkedin_jobs(keyword, location)
        df = clean_jobs(df)

        df.to_csv("data/jobs.csv", index=False)

        st.success("Data Collected Successfully!")

        st.dataframe(df)

        st.subheader("Top Companies Hiring")

        company_counts = df["company"].value_counts().head(10)

        st.bar_chart(company_counts)

        st.subheader("Top Locations")

        location_counts = df["location"].value_counts().head(10)

        st.bar_chart(location_counts)