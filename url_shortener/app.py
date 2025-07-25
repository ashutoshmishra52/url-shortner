from flask import Flask, render_template, request, redirect, url_for
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        url = request.form['url']
        if url:
            s = pyshorteners.Shortener()
            try:
                short_url = s.tinyurl.short(url)
            except Exception as e:
                short_url = f"Error: {str(e)}"
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', short_url=None)

if __name__ == '__main__':
    app.run(debug=True)