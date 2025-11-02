from flask import Flask, render_template, request, redirect, flash
from services import ContactService

app = Flask(__name__)
app.secret_key = 'abc123'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    contacts = ContactService.get_all_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        
        success, message = ContactService.create_contact(name, phone)
        
        if success:
            flash(message, 'success')
            return redirect('/')
        else:
            flash(message, 'error')
    
    return render_template('add.html')