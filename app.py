from flask import Flask, render_template

app = Flask(__name__)

# 🏠 Homepage
@app.route('/')
def home():
    return render_template('index.html')

# 🖼️ Gallery page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# 🔗 Links page
@app.route('/links')
def links():
    return render_template('links.html')

# 👤 About page
@app.route('/about')
def about():
    return render_template('about.html')

# 🚀 Run the app
if __name__ == '__main__':
    app.run(debug=True)