from flask import Flask, render_template, request, redirect, flash
from services import ContactService

app = Flask(__name__)
app.secret_key = 'abc123'

@app.route('/')
def home():
    """
    Home page - displays all contacts
    """
    contacts = ContactService.get_all_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    """
    Add new contact - handles form submission
    """
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

@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit_contact(name):
    """
    Edit existing contact
    """
    if request.method == 'POST':
        new_phone = request.form['phone']
        
        success, message = ContactService.update_contact(name, new_phone)
        
        if success:
            flash(message, 'success')
            return redirect('/')
        else:
            flash(message, 'error')
    
    # GET request - show current data
    contact_phone = ContactService.get_contact(name)
    if contact_phone:
        return render_template('edit.html', name=name, phone=contact_phone)
    else:
        flash('Contact not found!', 'error')
        return redirect('/')

@app.route('/delete/<name>')
def delete_contact(name):
    """
    Delete contact
    """
    success, message = ContactService.delete_contact(name)
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)