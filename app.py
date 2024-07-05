from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Routes for main navigation
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cyberpsychosis')
def cyberpsychosis():
    return render_template('cyberpsychosis.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

# Additional routes for threats and cure
@app.route('/threats')
def threats():
    return render_template('threats.html')

@app.route('/cure')
def cure():
    return render_template('cure.html')

def check_cyberpsychosis(chip_number):
    # Implement the logic to check for cyberpsychosis here
    # For example:
    if chip_number == '12345':
        return 'You are at risk of cyberpsychosis!'
    else:
        return 'You are not at risk of cyberpsychosis.'

if __name__ == '__main__':
    app.run(debug=True)