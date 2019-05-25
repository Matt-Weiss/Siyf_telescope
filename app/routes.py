from app import app
from app import stepper
from flask import request

@app.route('/')
def root():
    return "Welcome to the URL for telescope movement via the Space in Your Face app. please refer to the documentation for that app to learn how to use this one."

@app.route('/scopetest')
def scopetest():
    delay = int(request.args.get('delay'))
    steps = int(request.args.get('steps'))
    stepper.forward(delay, steps)
    stepper.backwards(steps)
    return "success"

#@app.route('/scopenow')


#@app.route('/scopetrack')
    
