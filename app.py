from flask import Flask 

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
    url = 'https://jjbird.infinityfreeapp.com'
    
    # Fetch the content from the URL
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve the webpage", 500

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data (customize as needed)
    data = {
        'title': soup.title.string,
        'header': soup.h1.string if soup.h1 else 'No header found',
        'paragraphs': [p.get_text() for p in soup.find_all('p')],
        'links': [(a.get_text(), a['href']) for a in soup.find_all('a', href=True)],
    }
    
    return render_template('index.html', data=data)

        
        # Add more data extraction as needed
    }
    
    return render_template('index.html', data=data)
