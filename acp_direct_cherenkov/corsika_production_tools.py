import numpy as np
from collections import OrderedDict


def make_all_corsika_steering_cards(config):

    max_scatter_radius = config['config']['max_scatter_radius']
    max_zenith_distance = config['config']['max_zenith_distance']
    NSHOW = config['config']['NSHOW']

    all_corsika_steering_cards = []

    for nucleus in steering['nuclei']:
        for run_index in range(nucleus['NRUN']):

            seed = nucleus['PRMPAR'] + run_index
            run_number = run_index + 1

            card = OrderedDict()
            card['RUNNR'] = [str(run_number)]
            card['EVTNR'] = [str(1)]
            card['NSHOW'] = [str(NSHOW)]
            card['PRMPAR'] = [str(nucleus['PRMPAR'])]
            card['ESLOPE'] = [str(nucleus['ESLOPE'])]            
            card['ERANGE'] = [str(nucleus['Emin'])+' '+str(nucleus['Emax'])]
            card['THETAP'] = [str(0.)+' '+str(max_zenith_distance)]
            card['PHIP'] = [str(0.)+' '+str(360.)]
            card['SEED'] = [str(seed)+' 0 0', str(seed+1)+' 0 0']            
            card['OBSLEV'] = [str(5000e2)]
            card['FIXCHI'] = [str(0.)]
            card['MAGNET'] = [str(1e-99)+' '+str(1e-99)]
            card['ELMFLG'] = ['T T']
            card['MAXPRT'] = [str(1)]
            card['PAROUT'] = ['F F']
            card['TELESCOPE'] = [str(0.)+' '+str(0.)+' '+str(0.)+' '+str(75e2)]
            card['ATMOSPHERE'] = [str(6)+' T']
            card['CSCAT'] = [str(1)+' '+str(max_scatter_radius)+' '+str(0.)]
            card['CERQEF'] = ['F T F'] # pde, atmo, mirror
            card['CWAVLG'] = [str(290)+' '+str(700)]
            card['CERSIZ'] = [str(1)]
            card['CERFIL'] = ['F']
            card['TSTART'] = ['T']
            card['EXIT'] = ['']
            all_corsika_steering_cards.append(card)
    return all_corsika_steering_cards


























def make_corsika_steering_cards(prmpar=1, number_of_runs=1, number_of_events=1, energy_range=[10000,90000], cscat_x=75000, cscat_y=0):
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
            card['TELESCOPE'] = [str(0.)+' '+str(0.)+' '+str(0.)+' '+str(7500.0)]
            card['ATMOSPHERE'] = [str(6)+' T']
            card['CSCAT'] = [str(1)+' '+str(cscat_x)+' '+str(cscat_y)]
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

