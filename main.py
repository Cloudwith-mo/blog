from flask import Flask, render_template
import markdown
import os  # Add this for directory listing

app = Flask(__name__)

@app.route('/')
def home():
    posts = []
    # List all markdown files in the "posts" directory
    for file in os.listdir('posts'):
        if file.endswith('.md'):
            title = file[:-3]  # Remove .md extension
            posts.append(title)
    return render_template('index.html', posts=posts)

@app.route('/posts/<path:path>')
def post(path):
    try:
        with open(f'posts/{path}.md', 'r') as file:
            content = file.read()
            html = markdown.markdown(content)
            return render_template('post.html', title=path, content=html)
    except FileNotFoundError:
        return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True)
