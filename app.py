from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello2():
    return "This is a test"

@app.route('/m')
def index():
    # Your domain webpage URL
    url = 'http://jjbird.infinityfreeapp.com'
    
    # Fetch the content from the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        return f"Failed to retrieve the webpage: {e}", 500

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data (customize as needed)
    data = {
        'title': soup.title.string if soup.title else 'No title found',
        'header': soup.h1.string if soup.h1 else 'No header found',
        'paragraphs': [p.get_text() for p in soup.find_all('p')],
        'links': [(a.get_text(), a['href']) for a in soup.find_all('a', href=True)],
    }
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
