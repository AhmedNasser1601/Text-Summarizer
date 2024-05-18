# [Text Summarizer](https://ahmednasser1601.github.io/Text-Summarizer)
This project is a web application that provides text summarization functionality. It allows users to input text and receive a summarized version of the input text. The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. It uses the Hugging Face Transformers library for text summarization.

## Features
- Summarizes input text using a pre-trained model from Hugging Face.
- Allows users to specify minimum and maximum lengths for the summary.
- Provides a user-friendly interface with a loading indicator.
- Ensures that the maximum length is greater than the minimum length.

## Installation

### Requirements
```plaintext
flask
flask-cors
transformers
torch
```

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/AhmedNasser1601/Text-Summarizer.git
    cd Text-Summarizer
    ```
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the application:
    ```sh
    python main.py
    ```
4. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
1. Enter the text you want to summarize in the text area.
2. Adjust the minimum and maximum lengths using the plus and minus buttons.
3. Click the "Summarize" button.
4. Wait for the summary to be generated. The summary will be displayed below the form.

## Example
<img src="https://github.com/AhmedNasser1601/Text-Summarizer/blob/e7390af03016561dfe10a986845e808673a96a69/example.png?raw=true" />

## File Structure
- `main.py`: The backend Flask application that handles requests and performs text summarization.
- `templates/index.html`: The main HTML file that contains the structure of the web page.
- `static/main.css`: The CSS file for styling the web page.
- `static/main.js`: The JavaScript file that handles form submission and interacts with the backend.

## Acknowledgements
- Hugging Face for the Transformers library
- Flask framework

> ### Feel free to contribute to this project by creating issues or submitting pull requests.
