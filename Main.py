from flask import Flask
import socket
import tkinter as tk
from tkinter import simpledialog

# Function to get the local IP address
def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Create a Flask application
app = Flask(__name__)

# Default route
@app.route('/')
def index():
    return "<h1>Welcome to SmallHost</h1><p>This is a simple hosting app allowing you to access your local server from the Internet.</p>"

# Function to run the Flask app on a given port
def run_server(port):
    local_ip = get_local_ip()
    app.run(host=local_ip, port=port)

# Create a simple Tkinter GUI to get the port number from the user
root = tk.Tk()
root.withdraw()  # Hide the main window

port = simpledialog.askinteger("Port Number", "Enter the port number to host the app:")

if port:
    run_server(port)
else:
    print("No port number provided. Exiting...")
