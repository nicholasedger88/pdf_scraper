#PDF Scraper Web App
Overview
This is a simple web application built with Flask that allows users to scrape PDF documents from a given URL. The app extracts the first specified number of words from the document (skipping fund name headers and dates) and presents both the raw extracted text and a cleaned version.

Features
Users can specify a URL for a PDF file to scrape.
Users can input how many words they want extracted from the PDF.
The app displays both the raw scraped text and a cleaned version, starting from the first non-capitalized word.
Built using Flask with a Bootstrap frontend for styling.
Supports adjustable text extraction via a word limit input.
Requirements
Python 3.x
Flask
PyPDF2
Requests
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Open your browser and visit:

arduino
Copy code
http://127.0.0.1:5000/
Date
Updated on: October 20, 2024