from app import app
from app import declination_1
from app import ascension
from flask import request


@app.route('/')
def root():
    return "Welcome to the URL for telescope movement via the Space in Your Face app. please refer to the documentation for that app to learn how to use this one."

@app.route('/scopetest')
def scopetest():
    start()
    track()
    zero()
    return "success"

def start():
    start_ra_steps = int(request.args.get('move_to_start_ra' ))
    start_dec_steps = int(request.args.get('move_to_start_dec' ))
    if start_dec_steps > 0 and start_ra_steps > 0:
        declination_1.forward( 1, start_dec_steps )
        ascension.forward( 1, start_ra_steps )
    elif start_dec_steps < 0 and start_ra_steps > 0:
        declination_1.backwards( 1, abs(start_dec_steps) )
        ascension.forward( 1, start_ra_steps )
    elif start_dec_steps > 0 and start_ra_steps < 0:
        declination_1.forward( 1, start_dec_steps )
        ascension.backwards( 1, abs(start_ra_steps) )
    else:
        declination_1.backwards( 1, abs(start_dec_steps)  )
        ascension.backwards( 1, abs(start_ra_steps)  )
    return "success"

def track():
    track_dec_delay = int(request.args.get('track_dec_delay' ))
    track_dec_steps = int(request.args.get('track_dec_steps' ))
    track_ra_delay = int(request.args.get('track_ra_delay' ))
    track_ra_steps = int(request.args.get('track_ra_steps' ))
    if track_dec_steps > 0 and track_ra_steps > 0:
        declination_1.forward( track_dec_delay, track_dec_steps )
        ascension.forward( track_ra_delay, track_ra_steps )
    elif track_dec_steps < 0 and track_ra_steps > 0:
        declination_1.backwards( track_dec_delay, abs(track_dec_steps)  )
        ascension.forward( track_ra_delay, track_ra_steps )
    elif track_dec_steps > 0 and track_ra_steps < 0:
        declination_1.forward( track_dec_delay, track_dec_steps )
        ascension.backwards( track_ra_delay, abs(track_ra_steps)  )
    else:
        declination_1.backwards( track_dec_delay, abs(track_dec_steps)  )
        ascension.backwards( track_ra_delay, abs(track_ra_steps)  )
    return "success"

def zero():
    return_home_ra_steps = int(request.args.get('return_home_ra_steps' ))
    return_home_dec_steps = int(request.args.get('return_home_dec_steps' ))
    if return_home_dec_steps > 0 and return_home_dec_steps > 0:
        declination_1.forward( 1, return_home_dec_steps )
        ascension.forward( 1, return_home_dec_steps )
    elif return_home_dec_steps < 0 and return_home_dec_steps > 0:
        declination_1.backwards( 1, abs(return_home_dec_steps)  )
        ascension.forward( 1, return_home_dec_steps )
    elif return_home_dec_steps > 0 and return_home_dec_steps < 0:
        declination_1.forward( 1, return_home_dec_steps )
        ascension.backwards( 1, abs(return_home_dec_steps)  )
    else:
        declination_1.backwards( 1, abs(return_home_dec_steps)  )
        ascension.backwards( 1, abs(return_home_dec_steps)  )
    return "success"

#@app.route('/scopenow')
#def scopenow():
#    start_ra_steps = int(request.args.get('move_to_start_ra' ))
#    start_dec_steps = int(request.args.get('move_to_start_dec' ))
#    if start_dec_steps > 0 and start_ra_steps > 0:
#        declination_1.forward( 1, start_dec_steps )
#        #declination_2.forward( 1, start_dec_steps )
#        ascension.forward( 1, start_ra_steps )
#    elif start_dec_steps < 0 and start_ra_steps > 0:
#        declination_1.backwards( 1, start_dec_steps )
#        #declination_2.backwards( 1, start_dec_steps )
#        ascension.forward( 1, start_ra_steps )
#    elif start_dec_steps > 0 and start_ra_steps < 0:
#        declination_1.forward( 1, start_dec_steps )
#        #declination_2.forward( 1, start_dec_steps )
#        ascension.backwards( 1, start_ra_steps )
#    else:
#        declination_1.backwards( 1, start_dec_steps )
#        #declination_2.backwards( 1, start_dec_steps )
#        ascension.backwards( 1, start_ra_steps )
#    return "success"
#
@app.route('/scopetrack')
def scopetrack():
    start
    track
    zero
    return "success"

def start():
    start_ra_steps = int(request.args.get('move_to_start_ra' ))
    start_dec_steps = int(request.args.get('move_to_start_dec' ))
    if start_dec_steps > 0 and start_ra_steps > 0:
        declination_1.forward( 1, start_dec_steps )
        ascension.forward( 1, start_ra_steps )
    elif start_dec_steps < 0 and start_ra_steps > 0:
        declination_1.backwards( 1, start_dec_steps )
        ascension.forward( 1, start_ra_steps )
    elif start_dec_steps > 0 and start_ra_steps < 0:
        declination_1.forward( 1, start_dec_steps )
        ascension.backwards( 1, start_ra_steps )
    else:
        declination_1.backwards( 1, start_dec_steps )
        ascension.backwards( 1, start_ra_steps )
    return "success"

def track():
    track_dec_delay = int(request.args.get('track_dec_delay' ))
    track_dec_steps = int(request.args.get('track_dec_steps' ))
    track_ra_delay = int(request.args.get('track_ra_delay' ))
    track_ra_steps = int(request.args.get('track_ra_steps' ))
    if track_dec_steps > 0 and track_ra_steps > 0:
        declination_1.forward( track_dec_delay, track_dec_steps )
        ascension.forward( track_ra_delay, track_ra_steps )
    elif track_dec_steps < 0 and track_ra_steps > 0:
        declination_1.backwards( track_dec_delay, track_dec_steps )
        ascension.forward( track_ra_delay, track_ra_steps )
    elif track_dec_steps > 0 and track_ra_steps < 0:
        declination_1.forward( track_dec_delay, track_dec_steps )
        ascension.backwards( track_ra_delay, track_ra_steps )
    else:
        declination_1.backwards( track_dec_delay, track_dec_steps )
        ascension.backwards( track_ra_delay, track_ra_steps )
    return "success"

def zero():
    return_home_ra_steps = int(request.args.get('return_home_ra_steps' ))
    return_home_dec_steps = int(request.args.get('return_home_dec_steps' ))
    if return_home_dec_steps > 0 and return_home_dec_steps > 0:
        declination_1.forward( 1, return_home_dec_steps )
        ascension.forward( 1, return_home_dec_steps )
    elif return_home_dec_steps < 0 and return_home_dec_steps > 0:
        declination_1.backwards( 1, return_home_dec_steps )
        ascension.forward( 1, return_home_dec_steps )
    elif return_home_dec_steps > 0 and return_home_dec_steps < 0:
        declination_1.forward( 1, return_home_dec_steps )
        ascension.backwards( 1, return_home_dec_steps )
    else:
        declination_1.backwards( 1, return_home_dec_steps )
        ascension.backwards( 1, return_home_dec_steps )
    return "success"
    
