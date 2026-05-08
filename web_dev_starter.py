# Python Web Development Starter - Beginner Level
# Using Flask - A lightweight web framework for Python

# Step 1: Import Flask
from flask import Flask, render_template, request

# Step 2: Create a Flask application
app = Flask(__name__)

# Step 3: Define routes (URLs) and their corresponding functions

# Home page route
@app.route('/')
def home():
    """This is the home page"""
    return '''
    <html>
        <head>
            <title>Welcome to My Website</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 50px;
                    background-color: #f0f0f0;
                }
                h1 {
                    color: #333;
                }
                a {
                    color: #007bff;
                    text-decoration: none;
                    margin: 10px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to My Python Web App!</h1>
            <p>Hello! This is my first web application using Flask.</p>
            <h2>Navigation:</h2>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/greet/Alhassane">Greet Me</a></li>
                <li><a href="/form">Contact Form</a></li>
            </ul>
        </body>
    </html>
    '''

# About page route
@app.route('/about')
def about():
    """This is the about page"""
    return '''
    <html>
        <head>
            <title>About Me</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 50px;
                    background-color: #f0f0f0;
                }
            </style>
        </head>
        <body>
            <h1>About Me</h1>
            <p>Hi! I'm Sow Alhassane, learning Python web development.</p>
            <p>I'm interested in Android Development and Python!</p>
            <a href="/">Back to Home</a>
        </body>
    </html>
    '''

# Dynamic route with parameters
@app.route('/greet/<name>')
def greet(name):
    """This route takes a name parameter and greets the user"""
    return f'''
    <html>
        <head>
            <title>Greeting</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 50px;
                    background-color: #f0f0f0;
                }}
                h1 {{
                    color: #28a745;
                }}
            </style>
        </head>
        <body>
            <h1>Hello, {name}! 👋</h1>
            <p>Welcome to my web application!</p>
            <a href="/">Back to Home</a>
        </body>
    </html>
    '''

# Form page route
@app.route('/form', methods=['GET', 'POST'])
def form():
    """This route handles a contact form"""
    message = ""
    
    # Check if form was submitted
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = f"Thank you, {name}! We received your message. We'll contact you at {email}"
    
    return f'''
    <html>
        <head>
            <title>Contact Form</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 50px;
                    background-color: #f0f0f0;
                }}
                input, textarea {{
                    padding: 10px;
                    margin: 5px 0;
                    width: 300px;
                }}
                button {{
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    cursor: pointer;
                }}
                button:hover {{
                    background-color: #0056b3;
                }}
                .success {{
                    color: green;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>Contact Me</h1>
            <form method="POST">
                <label>Your Name:</label><br>
                <input type="text" name="name" required><br><br>
                
                <label>Your Email:</label><br>
                <input type="email" name="email" required><br><br>
                
                <label>Your Message:</label><br>
                <textarea name="message" rows="5" cols="40"></textarea><br><br>
                
                <button type="submit">Send Message</button>
            </form>
            
            {f'<p class="success">{message}</p>' if message else ''}
            
            <a href="/">Back to Home</a>
        </body>
    </html>
    '''

# Step 4: Run the application
if __name__ == '__main__':
    # debug=True allows auto-reload when you change code
    app.run(debug=True, host='0.0.0.0', port=5000)
