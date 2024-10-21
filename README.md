# PDF Scraper Web App

### Overview
This is a simple web application built with **Flask** that allows users to scrape PDF documents from a given URL. The app extracts the first specified number of words from the document (skipping any content that might typically be presented beforehand; in this case, header text that is capitalised) and presents both the raw extracted text and a cleaned version.

### Features
- Users can specify a URL for a PDF file to scrape.
- Users can input how many words they want extracted from the PDF.
- The app displays both the raw scraped text and a cleaned version, starting from the first non-capitalized word.
- Built using **Flask** with a **Bootstrap** frontend for styling.
- Supports adjustable text extraction via a word limit input.
- Provides an API for external tools (such as Alteryx) to interact with the application.

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

## API Integration for External Tools

The web application exposes an API endpoint at /api/scrape that can be called by external tools like Alteryx to scrape PDFs and extract the desired number of words. The API supports both GET and POST requests.

## API Usage
GET Request: You can pass the url and word_limit as query parameters. Here is an example request:

    http://yourdomain.com/api/scrape?url=https://example.com/somefile.pdf&word_limit=100
