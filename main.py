from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = {
            "title": request.form['title'],
            "author": request.form['author'],
            "rating": request.form['rating'],
        }
        all_books.append(book)
        print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

