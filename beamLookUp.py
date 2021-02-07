# -*- coding: utf-8 -*-
"""
===================================================
Beam number look up table
===================================================

Created on Fri Jan 06 15:06:17 2017


@author: Rillahan
"""
from bisect import bisect
<<<<<<< HEAD
import numpy as np
=======
>>>>>>> a5a1429efb1d1e1387741cfc295c3782fccfab5e
               
breakpoints128 = [-14.831,-14.596,-14.379,-14.162,-13.945,-13.728,-13.51,-13.293,-13.076,-12.852,-12.62,-12.388,
                -12.156,-11.925,-11.693,-11.461,-11.23,-10.998,-10.766,-10.535,-10.303,-10.071,-9.839,-9.608,
                -9.376,-9.144,-8.913,-8.681,-8.449,-8.218,-7.986,-7.754,-7.523,-7.291,-7.059,-6.827,-6.596,-6.364,
                -6.132,-5.901,-5.669,-5.437,-5.206,-4.974,-4.742,-4.51,-4.279,-4.047,-3.815,-3.584,-3.352,-3.12,
                -2.889,-2.657,-2.425,-2.194,-1.962,-1.723,-1.477,-1.231,-0.984,-0.738,-0.492,-0.246,0,0.246,0.492,
                0.738,0.984,1.231,1.477,1.723,1.96,2.194,2.425,2.657,2.889,3.12,3.352,3.584,3.815,4.047,4.279,
                4.51,4.742,4.974,5.206,5.437,5.669,5.901,6.132,6.364,6.596,6.827,7.059,7.291,7.523,7.754,7.986,
                8.218,8.449,8.681,8.913,9.144,9.376,9.608,9.839,10.071,10.303,10.535,10.766,10.998,11.23,11.461,
                11.693,11.925,12.156,12.388,12.62,12.852,13.076,13.293,13.51,13.728,13.945,14.162,14.379,14.596,14.832]
                
breakpoints96 = [-13.762,-13.553,-13.337,-13.112,-12.878,-12.644,-12.41,-12.176,-11.93,-11.68,-11.428,-11.176,
                 -10.924,-10.672,-10.419,-10.167,-9.906,-9.636,-9.366,-9.096,-8.825,-8.546,-8.258,-7.97,-7.682,
                 -7.393,-7.105,-6.808,-6.502,-6.196,-5.89,-5.583,-5.277,-4.971,-4.656,-4.332,-4.007,-3.683,
                 -3.359,-3.035,-2.71,-2.386,-2.053,-1.711,-1.369,-1.026,-0.684,-0.342,0,0.342,0.684,1.026,
                 1.369,1.711,2.053,2.386,2.71,3.035,3.359,3.683,4.007,4.332,4.656,4.971,5.277,5.583,5.89,
                 6.196,6.502,6.808,7.105,7.393,7.682,7.97,8.258,8.546,8.825,9.096,9.366,9.636,9.906,10.167,
                 10.419,10.672,10.924,11.176,11.428,11.68,11.932,12.176,12.41,12.644,12.878,13.112,13.337,
                 13.553,13.762]

breakpoints64 = [-14.945,-14.484,-14.046,-13.608,-13.17,-12.717,-12.25,-11.783,-11.316,-10.848,-10.381,-9.914,-9.447,
                 -8.98,-8.512,-8.045,-7.578,-7.111,-6.644,-6.176,-5.709,-5.242,-4.775,-4.308,-3.84,-3.373,-2.906,
                 -2.439,-1.972,-1.49,-0.993,-0.497,0,0.497,0.993,1.49,1.972,2.439,2.906,3.373,3.84,4.308,4.775,
                 5.242,5.709,6.176,6.644,7.111,7.578,8.045,8.512,8.98,9.447,9.914,10.381,10.848,11.316,11.783,12.25,
                 12.717,13.17,13.608,14.046,14.484, 14.484]
                 
breakpoints48 = [-13.74,-13.442,-13.051,-12.607,-12.145,-11.666,-11.169,-10.654,-10.121,-9.571,-9.002,-8.416,
                 -7.813,-7.209,-6.587,-5.948,-5.309,-4.67,-4.03,-3.373,-2.699,-2.024,-1.349,-0.674,0,0.674,
                 1.349,2.024,2.699,3.373,4.03,4.67,5.309,5.948,6.587,7.209,7.813,8.416,9.002,9.571,10.121,
                 10.654,11.169,11.666,12.145,12.607,13.051,13.442,13.740]


def BeamLookUp(beam_angle, BeamCount):
    if BeamCount == 128:
        breakpoints = breakpoints128
    if BeamCount == 96:
        breakpoints = breakpoints96
    if BeamCount == 64:
        breakpoints = breakpoints64
    if BeamCount == 48:
        breakpoints = breakpoints48
        
<<<<<<< HEAD
    beam = np.nan
=======
    beam = 999
>>>>>>> a5a1429efb1d1e1387741cfc295c3782fccfab5e
    if beam_angle > breakpoints[0]:
        if beam_angle <= breakpoints[-1]:
            beam = bisect(breakpoints, beam_angle)-1
    return beam
    
def beamAngle(beam_num, BeamCount):
    '''Returns the beam angle of the requested beam.  This may not be the true beam center,
    due to non-centric beams but it is close'''
    
    if BeamCount == 128:
        breakpoints = breakpoints128
    if BeamCount == 96:
        breakpoints = breakpoints96
    if BeamCount == 64:
        breakpoints = breakpoints64
    if BeamCount == 48:
        breakpoints = breakpoints48
        
    angle = (breakpoints[beam_num]+breakpoints[beam_num+1])/2
    return angle