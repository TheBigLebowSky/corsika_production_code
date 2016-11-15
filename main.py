"""
Produces hadronic shower for DC light studies

Usage: hadronic_production  -o=OUTPUT_PATH --number_of_runs=NUMBER_OF_RUNS --number_of_events=NUMBER_EVENTS_PER_PRIMARY --primary_charge=PRIMARY_CHARGE --Emax=MAX_ENERGY --Emin=MIN_ENERGY 

Options:
    -o --output_path=OUTPUT_PATH                Overwrites the output path in 
                                                the steering card.
    --number_of_runs=NUMBER_OF_RUNS             Select the number of runs.
    --number_of_events=NUMBER_EVENTS_PER_PRIMARY   Select number of events per primary particle.
    
    --primary_charge=PRIMARY_CHARGE             Choose primary charge.
    
    --Emax=MAX_ENERGY                           Specify energy range.
    --Emin=MIN_ENERGY   
"""
import os
import scoop as sc
from scoop import futures
import docopt
import corsika_production_tools
import corsika_wrapper as cw


def output_path():
    return sc.shared.getConst('output_path', timeout=5)


def make_corsika_run(steering):
    cw.corsika(
        steering_card=steering['steering_card'],
        output_path=os.path.join(output_path(), 'my_file_run_number_%d.dat' %(steering['run_number'])),
        save_stdout=True)

    return True
            
            
            
def corsika_id(charge):

    primaries = [
        {'charge':0 },
        {'charge':1, 'mass':1, 'corsika_id':14, 'name':'Hydrogen'},
        {'charge':2, 'mass':4, 'corsika_id':402, 'name':'Helium'},
        {'charge':3, 'mass':6, 'corsika_id':603, 'name':'Lithium'},
        {'charge':4, 'mass':9, 'corsika_id':904, 'name':'Beryllium'},
        {'charge':5, 'mass':10, 'corsika_id':1005, 'name':'Boron'},
        {'charge':6, 'mass':12, 'corsika_id':1206, 'name':'Carbon'},
        {'charge':7, 'mass':14, 'corsika_id':1407, 'name':'Nitrogen'},
        {'charge':8, 'mass':16, 'corsika_id':1608, 'name':'Oxygen'},
        {'charge':9, 'mass':19, 'corsika_id':1909, 'name':'Fluorine'},
        {'charge':10, 'mass':20, 'corsika_id':2010, 'name':'Neon'},
        {'charge':11, 'mass':23, 'corsika_id':2311, 'name':'Sodium'},
        {'charge':12, 'mass':24, 'corsika_id':2412, 'name':'Magnesium'},
        {'charge':13, 'mass':27, 'corsika_id':2713, 'name':'Aluminium'},
        {'charge':14, 'mass':28, 'corsika_id':2814, 'name':'Silicon'},
        {'charge':15, 'mass':31, 'corsika_id':3115, 'name':'Phosphorus'},
        {'charge':16, 'mass':32, 'corsika_id':3216, 'name':'Sulfur'},
        {'charge':17, 'mass':35, 'corsika_id':3517, 'name':'Chlorine'},
        {'charge':18, 'mass':40, 'corsika_id':4018, 'name':'Argon'},
        {'charge':19, 'mass':39, 'corsika_id':3919, 'name':'Potassium'},
        {'charge':20, 'mass':40, 'corsika_id':4020, 'name':'Calcium'},
        {'charge':21, 'mass':45, 'corsika_id':4521, 'name':'Scandium'},
        {'charge':22, 'mass':48, 'corsika_id':4822, 'name':'Titanium'},
        {'charge':23, 'mass':51, 'corsika_id':5123, 'name':'Vanadium'},
        {'charge':24, 'mass':52, 'corsika_id':5224, 'name':'Chromium'},
        {'charge':25, 'mass':55, 'corsika_id':5525, 'name':'Manganese'},
        {'charge':26, 'mass':56, 'corsika_id':5626, 'name':'Iron'}
        ]
        
    corsika_id=primaries[charge]['corsika_id']
        
    return corsika_id


def main():
    
    
    try:
        arguments = docopt.docopt(__doc__)
        
        
        sc.shared.setConst(output_path=os.path.abspath(arguments['--output_path']))
        
        
        charge = int(arguments['--primary_charge'])
        particle_id = corsika_id(charge)
        
        energy_range = [int(arguments['--Emin']),int(arguments['--Emax'])]
    
        number_of_runs = int(arguments['--number_of_runs'])
        number_of_events = int(arguments['--number_of_events'])
    

        #Make steering cards based on the given template
        steering_cards = corsika_production_tools.make_corsika_steering_cards(
                    prmpar=particle_id, 
                    number_of_runs=number_of_runs,
                    number_of_events=number_of_events, 
                    energy_range=energy_range)


        #Run corsika
        result = list(sc.futures.map(make_corsika_run, steering_cards))            


    except docopt.DocoptExit as e:        
        print(e)
  
if __name__ == '__main__':    
    main()


