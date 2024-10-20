# PDF Scraper Web App

### Overview
This is a simple web application built with **Flask** that allows users to scrape PDF documents from a given URL. The app extracts the first specified number of words from the document (skipping any content that might typically be presented beforehand; in this case, header text that is capitalised) and presents both the raw extracted text and a cleaned version.

### Features
- Users can specify a URL for a PDF file to scrape.
- Users can input how many words they want extracted from the PDF.
- The app displays both the raw scraped text and a cleaned version, starting from the first non-capitalized word.
- Built using **Flask** with a **Bootstrap** frontend for styling.
- Supports adjustable text extraction via a word limit input.

### Requirements
- Python 3.x
- Flask
- PyPDF2
- Requests

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Run the Flask app:**
    ````bash
    python app.py

4. **Open your browser and visit:**
    ````arduino
    http://127.0.0.1:5000/