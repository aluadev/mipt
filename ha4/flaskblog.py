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
    idt = [post['title'] for post in posts].index(title)
    return render_template('posts.html', post=posts[idt])


@app.route("/post/newPost", methods=['POST', 'GET'])
def newPost():
    d = {}
    if request.method == 'POST':
        d['title'] = request.form['title']
        d['written by'] = request.form['author']
        d['content'] = request.form['content']
        d['date_posted'] = request.form['date_posted']
        posts.append(d)
        return render_template('main.html')
    else:
        return render_template('posts.html')



if __name__ == "__main__":
    app.run(debug=True)
