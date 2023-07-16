from flask import Flask, render_template, request
from scraper import scrape_website

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        scraped_data = scrape_website(url)
        return render_template('result.html', data=scraped_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
