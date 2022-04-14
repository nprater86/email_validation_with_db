from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=["POST"])
def create():
    if not Email.validate(request.form):
        return redirect('/')

    data = {
        "email": request.form['email']
    }
    Email.create(data)
    return redirect('/emails')

@app.route('/emails')
def emails():
    emails = Email.get_all()
    return render_template('emails.html', emails = emails)

@app.route('/delete/<email_id>')
def delete(email_id):
    data = {"id":email_id}
    Email.delete(data)
    return redirect('/emails')