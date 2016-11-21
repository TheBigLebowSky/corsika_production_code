# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:22:53 2016

@author: cherenkov
"""


import numpy as np
import corsika_wrapper as cw
from collections import OrderedDict

def make_corsika_steering_cards(prmpar=1, number_of_runs=1, number_of_events=1, energy_range=[10000,90000]):
        steering = []
        for run_index in range(number_of_runs):

            run_number = run_index + 1
            
            card = OrderedDict()
            card['RUNNR'] = [str(run_number)]
            card['EVTNR'] = [str(1)]
            card['NSHOW'] = [str(number_of_events)]
            card['PRMPAR'] = [str(prmpar)]
            card['ESLOPE'] = [str(0.0)]            
            card['ERANGE'] = [str(energy_range[0])+' '+str(energy_range[1])]
            card['THETAP'] = [str(0.)+' '+str(0.)]
            card['PHIP'] = [str(0.)+' '+str(360.)]
            card['SEED'] = [str(run_number)+' 0 0', str(run_number+1)+' 0 0']            
            card['OBSLEV'] = [str(5000e2)]
            card['FIXCHI'] = [str(0.)]
            card['MAGNET'] = [str(1e-99)+' '+str(1e-99)]
            card['ELMFLG'] = ['T T']
            card['MAXPRT'] = [str(1)]
            card['PAROUT'] = ['F F']
            card['TELESCOPE'] = [str(0.)+' '+str(0.)+' '+str(0.)+' '+str(6000.0)]
            card['ATMOSPHERE'] = [str(6)+' T']
            card['CSCAT'] = [str(1)+' '+str(6000.0)+' '+str(0.0)]
            card['CERQEF'] = ['F T F'] # pde, atmo, mirror
            card['CWAVLG'] = [str(290)+' '+str(700)]
            card['CERSIZ'] = [str(1)]
            card['CERFIL'] = ['F']
            card['TSTART'] = ['T']
            card['EXIT'] = ['']
            steering.append({
                'steering_card': card,
                'run_number': run_number
            })
        return steering

