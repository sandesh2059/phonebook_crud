from flask import Flask, render_template, request, redirect, flash
from services import ContactService

app = Flask(__name__)
app.secret_key = 'abc123'

if __name__ == '__main__':
    app.run(debug=True)
    