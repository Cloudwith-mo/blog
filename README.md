# Blog App with Flask

This guide explains how to set up and build a blog app using Flask, a lightweight web framework for Python.

---

## **Step 1: Set Up Your Project Folder**

Create a new directory for your project. This directory will hold all the files related to your blog app, including your Python code, templates, and Markdown posts.

### Commands:
```bash
mkdir blog
cd blog
```
Inside the blog directory, set up a virtual environment. A virtual environment ensures that your project dependencies don’t interfere with other Python projects.

Command:
```bash
python -m venv .venv
```
Directory Structure:
```bash
Copy code
blog/
├── .venv/  # Virtual environment folder
```

**Step 2: Activate the Virtual Environment**
Activate the virtual environment to use the isolated Python environment.

Command (Windows PowerShell):
```bash
.venv\Scripts\Activate.ps1
```
Once activated, your terminal prompt will show `(.venv)` to indicate you’re working inside the virtual environment.

**Step 3: Install Required Packages**
Use pip (Python’s package installer) to install Flask and Markdown.

Command:
bash
Copy code
pip install flask markdown
Packages Installed:
flask: A lightweight web framework for Python.
markdown: Converts Markdown content into HTML.
Directory Structure:
bash
Copy code
blog/
├── .venv/  # Virtual environment folder

**Step 4: Create Your Flask App**
In the blog directory, create a main.py file.

Command:
bash
Copy code
echo. > main.py
Open the main.py file in your code editor (e.g., VSCode) and add the following code:

Code:
python
Copy code
from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

@app.route('/')
def home():
    posts = []
    for file in os.listdir('posts'):
        if file.endswith('.md'):
            title = file[:-3]
            posts.append(title)
    return render_template('index.html', posts=posts)

@app.route('/posts/<path:path>')
def post(path):
    with open(f'posts/{path}.md', 'r') as file:
        content = file.read()
        html = markdown.markdown(content)
    return render_template('post.html', content=html)

if __name__ == '__main__':
    app.run(debug=True)
Explanation:
@app.route('/'): Maps the home page to the home() function.
os.listdir('posts'): Scans the posts folder for Markdown files.
@app.route('/posts/<path:path>'): Maps blog post URLs to the post() function, where <path> is the file name of the Markdown post.
markdown.markdown(content): Converts Markdown to HTML.
render_template(): Loads the corresponding HTML file from the templates folder.
Directory Structure:
bash
Copy code
blog/
├── .venv/  # Virtual environment folder
├── main.py  # Flask app

**Step 5: Create Templates and Posts**
Inside the blog directory, create a templates folder to store HTML templates.

Command:
bash
Copy code
mkdir templates
Inside the templates folder, create two files:

index.html: For the homepage.
post.html: For individual blog posts.
index.html Code:
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Blog</title>
</head>
<body>
    <h1>My Blog</h1>
    <ul>
        {% for post in posts %}
        <li><a href="/posts/{{ post }}">{{ post }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
post.html Code:
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ content|safe }}</title>
</head>
<body>
    <div>
        {{ content|safe }}
    </div>
</body>
</html>
Create a posts folder for storing Markdown files.

Command:
bash
Copy code
mkdir posts
Add your first post:

Create posts/hello.md with the following content:
markdown
Copy code
# Hello

This is my first blog post!
Directory Structure:
bash
Copy code
blog/
├── .venv/        # Virtual environment folder
├── main.py       # Flask app
├── templates/    # HTML templates
│   ├── index.html
│   └── post.html
├── posts/        # Blog posts
│   └── hello.md

**Step 6: Run Your Flask App**
Start the Flask server.

Command:
bash
Copy code
python main.py
Open your browser and go to http://127.0.0.1:5000.

Now you have a fully functional blog app with Flask. Happy blogging!
