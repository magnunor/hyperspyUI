# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 18:47:05 2014

@author: vidarton
"""



def lstrip(string, prefix):
    if string is not None:
        if string.startswith(prefix):
            return string[len(prefix):]
            
def fig2win(fig, windows):
    # Each figure has FigureCanvas as widget, canvas has figure property
    matches = [w for w in windows if w.widget().figure == fig]
    return matches[0]
    
def win2fig(window):
    # Each figure has FigureCanvas as widget, canvas has figure property
    return window.widget().figure
    
    
import hyperspy.components
from functools import partial
from python_qt_binding import QtGui, QtCore

def create_add_component_actions(parent, callback, prefix="", postfix=""):
    actions = {}
    compnames = ['Arctan', 'Bleasdale', 'DoubleOffset', 'DoublePowerLaw', 
                 'Erf', 'Exponential', 'Gaussian', 'Logistic', 'Lorentzian', 
                 'Offset', 'PowerLaw', 'SEE', 'RC', 'Vignetting', 'Voigt', 
                 'Polynomial', 'PESCoreLineShape', 'VolumePlasmonDrude']
    for name in compnames:
        t = getattr(hyperspy.components, name)
        ac_name = 'add_component_' + name
        f = partial(callback, t)
        ac = QtGui.QAction(prefix + name + postfix, parent)
        ac.setStatusTip("Add a component of type " + name)
        ac.connect(ac, QtCore.SIGNAL('triggered()'), f)
        actions[ac_name] = ac
    return actions