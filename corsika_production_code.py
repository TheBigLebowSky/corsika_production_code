# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:22:53 2016

@author: cherenkov
"""
import os
import copy
import numpy as np
import corsika_wrapper as cw

def make_corsika_run(steering_cards):
    for run_number in range(len(steering_cards)):
        cw.corsika(
            steering_card=steering_cards[run_number]['steering_card'],
            output_path=None,
            save_stdout=False
            )


def make_corsika_steering_cards(steering_card_template, output_path, prmpar=1608, number_of_runs=1, number_of_shower=1, energy_range=[10000,90000]):
        steering = []
        for run_index in range(number_of_runs):

            run_number = run_index + 1
            
            card = copy.deepcopy(steering_card_template)
            assert len(card['RUNNR']) == 1
            card['RUNNR'][0] = str(run_number)
            assert len(card['SEED']) == 2
            card['NSHOW'][0] = str(number_of_shower)
            card['PRMPAR'][0] = str(prmpar)
            card['ERANGE'][0] = str(energy_range[0])+' '+str(energy_range[1])
            card['SEED'][0] = str(run_number)+' 0 0'
            card['SEED'][1] = str(run_number+1)+' 0 0'
            card['OBSLEV'][0] = str(5000e2)
            card['MAGNET'][0] = str(1e-99)+' '+str(1e-99)
            card['TELFIL'][0] = '"/home/cherenkov/Documents/master_thesis/my_file_run_number_%d.dat"' %run_number
            card['TELESCOPE'][0] = str(0.)+' '+str(0.)+' '+str(0.)+' '+str(6000.0)
            card['ATMOSPHERE'][0] = str(6)+' T'
            card['CSCAT'][0] = str(1)+' '+str(6000.0)+' '+str(0.0)
            card['CERSIZ'][0] = str(1)
            card['CERFIL'][0] = 'F'
            card['TSTART'][0] = 'T'
            steering.append({
                'steering_card': card,
                'run_number': run_number,
                'mctracer_seed': run_number
            })
        return steering


#Choose and read template steering card
steering_card_template_path='/home/cherenkov/Documents/master_thesis/corsika_input_cards/corsika_template_input.txt'
steering_card_template= cw.tools.read_steering_card(steering_card_template_path)

#Choose output pass
output_path='/home/cherenkov/Documents/master_thesis/'

#Make steering cards based on the given template
steering_cards=make_corsika_steering_cards(steering_card_template, output_path, prmpar=1, number_of_runs=1, number_of_shower=1, energy_range=[1,9])


#Run corsika
make_corsika_run(steering_cards)
