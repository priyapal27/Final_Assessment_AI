
from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Static Flask Page</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(120deg, #0078d7, #00c6ff);
            color: white;
            text-align: center;
            margin-top: 100px;
        }
        h1 {
            font-size: 3em;
        }
        p {
            font-size: 1.2em;
        }
        button {
            background: white;
            color: #0078d7;
            border: none;
            padding: 10px 20px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #f0f0f0;
        }
    </style>
</head>
<body>
    <h1>Priya Pal</h1>
    <p>This is a simple static webpage served by Flask and Docker.</p>
    <button onclick="alert('Hello World from Priya !')">Click Me</button>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


