from app import declination_1
from app import declination_2
from app import ascension
import multiprocessing
from multiprocessing import Process

def move_to_start(start_ra_steps, start_dec_steps):

    if start_dec_steps > 0 and start_ra_steps > 0:
        Process( declination_1.forward,  ( 1, start_dec_steps,)) 
        Process( declination_2.forward,  ( 1, start_dec_steps,)) 
        Process( ascension.forward,  ( 1, start_ra_steps,)) 
    elif start_dec_steps < 0 and start_ra_steps > 0:
        Process( declination_1.backwards,  ( 1, start_dec_steps,)) 
        Process( declination_2.backwards,  ( 1, start_dec_steps,)) 
        Process( ascension.forward,  ( 1, start_ra_steps,)) 
    elif start_dec_steps > 0 and start_ra_steps < 0:
        Process( declination_1.forward,  ( 1, start_dec_steps,)) 
        Process( declination_2.forward,  ( 1, start_dec_steps,)) 
        Process( ascension.backwards,  ( 1, start_ra_steps,)) 
    else:
        p1=Process(target = declination_1.backwards, args = ( 1, start_dec_steps, ) )
        p2=Process(target = declination_2.backwards, args = ( 1, start_dec_steps, ) )
        p3=Process(target = ascension.backwards, args = ( 1, start_ra_steps, ) )
        import pdb; pdb.set_trace()
        p1.start()
        p2.start()
        p3.start()
    return "success"
