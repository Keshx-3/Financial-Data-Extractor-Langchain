import streamlit as st
import pandas as pd
from data_extractor import extract

# 1. Title
st.title("Financial Data Extractor")

# 2. Input box
text_input = st.text_area("Enter financial paragraph:")

# 3. Extract button
if st.button("Extract"):

    if text_input.strip() == "":
        st.warning("Please enter some text to extract data.")
    else:
        result = extract(text_input)

        # 4. Create table
        data = {
            "Measure": ["Revenue", "EPS"],
            "Estimated": [
                result.get("revenue_expected", ""),
                result.get("eps_expected", "")
            ],
            "Actual": [
                result.get("revenue_actual", ""),
                result.get("eps_actual", "")
            ]
        }

        df = pd.DataFrame(data)

        st.subheader("Extracted Financial Data")
        st.table(df)
