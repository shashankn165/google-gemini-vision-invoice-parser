# Gemini Vision Invoice Parser

An open-source application that uses Google Gemini Vision Pro API to extract invoice details from images and generate an Excel file with the extracted data. The application is built using Streamlit for the user interface.

## Features

- Upload invoice images in various formats (JPG, JPEG, PNG)
- Extract invoice details using Google Gemini Vision Pro API
- Generate an Excel file with extracted invoice data
- Easy-to-use Streamlit interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gemini-vision-invoice-parser.git
   cd gemini-vision-invoice-parser

2. Create a virtual environment and activate it:
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install the required packages:
   pip install -r requirements.txt
   
4. Set up environment variables:
   Create a ".env" file in the root directory of the project.
   Add your Google API key to the ".env" file
   GOOGLE_API_KEY=your_google_api_key

## USAGE

1. Run the Streamlit application:
   streamlit run app.py
Open your web browser and go to http://localhost:8501.

2. Upload an image of the invoice.

3. Modify the prompt if needed and click the "Tell me about the invoice" button.

4. View the extracted invoice details and download the generated Excel file.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.
   

