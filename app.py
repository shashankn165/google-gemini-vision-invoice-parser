from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import pandas as pd
import json

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input_prompt, image, user_prompt):
    # Assuming the `generate_content` method exists and its parameters are correctly used
    response = model.generate_content([input_prompt, image[0], user_prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def json_to_excel(json_data, output_filename="output_inv_data.xlsx"):
    line_items_df = pd.json_normalize(json_data, record_path=['line_items'])
    vendor_details = {key: json_data[key] for key in json_data.keys() - {'line_items'}}
    for column, value in vendor_details.items():
        line_items_df[column] = value
        # Define the desired column order
    desired_order = [
        "vendor_name", "invoice_number", "invoice_date", "invoice_amount",
        "line_number", "line_description", "quantity", "tax_rate", "amount"
    ]
    
    # Reorder the DataFrame according to the desired column order
    line_items_df = line_items_df[desired_order]
    line_items_df.to_excel(output_filename, index=False)
    return output_filename

# Streamlit UI Code (Assuming it's correct and works as intended)
# Initialize our Streamlit app
st.set_page_config(page_title="Multi Language Invoice Parser")
st.header("Multi Language Invoice Parser")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as invoice and you will have to answer any questions based on the uploaded invoice image.

**Output Format:**
1. **JSON Output:**  Extract vendor name, invoice number, invoice date, invoice amount, Line number, Line description, quantity, amount, tax rate from this invoice image. If there are multiple lines then repeat the header information and provide output in JSON format.

"""
input = st.text_input("Modify the prompt if needed: ", value=input_prompt, key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

# Correcting the JSON parsing part:
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response)
    
    # Correctly removing Markdown code block characters
    response_cleaned = response.replace("```json\n", "").replace("```", "").strip()
    try:
        json_data = json.loads(response_cleaned)
        output_filename = json_to_excel(json_data)
        st.success(f"Excel file generated: {output_filename}")
    except json.JSONDecodeError as e:
        st.error(f"JSON decoding failed: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
