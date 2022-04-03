from flask import Flask, render_template, request

from datetime import date

app = Flask(__name__)
posts = [{'author': 'Bob',
          'title': 'Post1',
          'content': 'Post1 content',
          'date_posted': date.today()
         },
         {'author': 'Alice',
          'title': 'Post2',
          'content': 'Post2 content',
          'date_posted': date.today()
          }] 

@app.route('/')
@app.route('/main.html')

def main():
    return render_template("main.html", posts=posts)

@app.route("/post/<title>")
def post(title):
    return render_template('posts.html', post=posts)


@app.route("/post/newPost", methods=['POST', 'GET'])
def newPost():
    if request.method == 'POST':
        request.form['title']
        request.form['content']
        request.form['author']
        return render_template('main.html')
    else:
        return render_template('posts.html')


if __name__ == "__main__":
    app.run(debug=False)
