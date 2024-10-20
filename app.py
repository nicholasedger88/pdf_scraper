from flask import Flask, render_template, request
import requests
import PyPDF2
from io import BytesIO

app = Flask(__name__)

# Function to remove the all-uppercase intro by finding the first non-capitalized word
def clean_intro_by_case(text):
    words = text.split()
    cleaned_text = []
    
    # Find the first word that is not entirely capitalized
    found_non_capitalized = False
    for word in words:
        if not word.isupper():
            found_non_capitalized = True
        if found_non_capitalized:
            cleaned_text.append(word)
    
    # Return the cleaned text as a string
    return ' '.join(cleaned_text).strip()

# Function to extract the specified number of words, stopping at the end of a sentence
def extract_intro_by_word_count(text, word_limit):
    sentences = text.split('. ')  # Split text by periods to get sentence-like chunks
    word_count = 0
    intro_chunk = []

    for sentence in sentences:
        words_in_sentence = len(sentence.split())  # Count words in the current sentence
        if word_count + words_in_sentence > word_limit:
            break  # Stop if adding this sentence would exceed the word limit
        intro_chunk.append(sentence.strip())  # Add the sentence to the chunk
        word_count += words_in_sentence

    return '. '.join(intro_chunk) + '.'  # Ensure we end with a period

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    cleaned_text = ""
    word_limit = 100  # Default word limit if none is provided by the user
    
    if request.method == 'POST':
        url = request.form['url']
        try:
            # Check if the user has specified a word limit
            if 'word_limit' in request.form and request.form['word_limit'].isdigit():
                word_limit = int(request.form['word_limit'])

            # Make a request to fetch the PDF
            response = requests.get(url)
            if response.status_code == 200:
                # Load the PDF content into a BytesIO object
                pdf_file = BytesIO(response.content)
                # Create a PDF reader object
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                all_text = ""
                # Iterate through each page and extract text
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    all_text += text + ' '  # Add a space after each page's text for clean formatting
                # Remove any extra whitespace from the extracted text
                all_text = all_text.strip()
                
                # Extract the cleaned intro by removing the uppercase fund name
                extracted_text = all_text  # Raw scraped text
                cleaned_text = clean_intro_by_case(extracted_text)  # Cleaned text without uppercase fund name
                
                # Now, extract the specified number of words from the cleaned text
                cleaned_text = extract_intro_by_word_count(cleaned_text, word_limit)
                
            else:
                extracted_text = "Failed to download PDF. Status code: {}".format(response.status_code)
        except Exception as e:
            extracted_text = "Error: {}".format(str(e))

    return render_template('index.html', extracted_text=extracted_text, cleaned_text=cleaned_text, word_limit=word_limit)

if __name__ == '__main__':
    app.run(debug=True)