from flask import Flask, render_template, session, redirect, url_for, request
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

def reset_queue_number(service_key):
    # Reset queue number and date when the day changes
    today = datetime.date.today()
    if 'date_' + service_key not in session or session['date_' + service_key] != today.strftime('%Y-%m-%d'):
        session['date_' + service_key] = today.strftime('%Y-%m-%d')
        session['queue_number_' + service_key] = 0

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('antrian/index.html')

@app.route('/service1', methods=['GET', 'POST'])
def service1():
    service_key = 'service1'
    reset_queue_number(service_key)
    if request.method == 'POST':
        session['queue_number_' + service_key] += 1
        return redirect(url_for('queue', service_key=service_key))
    return render_template('antrian/service.html', service_key=service_key, session=session['queue_number_service1'])

@app.route('/service2', methods=['GET', 'POST'])
def service2():
    service_key = 'service2'
    reset_queue_number(service_key)
    if request.method == 'POST':
        session['queue_number_' + service_key] += 1
        return redirect(url_for('queue', service_key=service_key))
    return render_template('antrian/service.html', service_key=service_key, session=session['queue_number_service2'])

@app.route('/service3', methods=['GET', 'POST'])
def service3():
    service_key = 'service3'
    reset_queue_number(service_key)
    if request.method == 'POST':
        session['queue_number_' + service_key] += 1
        return redirect(url_for('queue', service_key=service_key))
    return render_template('antrian/service.html', service_key=service_key, session=session['queue_number_service3'])

@app.route('/queue/<service_key>')
def queue(service_key):
    reset_queue_number(service_key)
    return render_template('antrian/queue.html', queue_number=session['queue_number_' + service_key])

if __name__ == '__main__':
    app.run(debug=True)
