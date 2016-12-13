"""
Browse through the simulated events

Usage: Browse simulated events  -i=INPUT_PATH_TO_SIMULATED_NUCLEI_DIR -n=RUN_NUMBER -e=EVENT_NUMBER

Options:
    -i --input_path=INPUT_PATH_TO_SIMULATED_NUCLEI_DIR      Input path to the
                                                            simulated nuclei 
                                                            directory.
    
    -n --run_number=RUN_NUMBER                              Give run number.
    
    -e --event_number=EVENT_NUMBER                            Give event number.                                               
"""


import plenopy as plp
import os
import numpy as np
import docopt



def main():
    
    try:
        
        arguments = docopt.docopt(__doc__)
        
        path_to_sim_nuclei = arguments['--input_path']
        run_number = arguments['--run_number']
        event_number = arguments['--event_number']
        event_index = event_number-1 
        
        run = plp.IdealizedPlenoscope.Run(os.path.join(path_to_sim_nuclei,'run%i/'%run_number))
            
        event=run[event_index]
    
        
        header=plp.Corsika.EventHeader(os.path.join(event.path, 'corsika_event_header.bin'))
        event_header=header.raw
            
        print ('Event number:', event_header[1])
        print ('Particle id:', event_header[2])
        print ('Energy [GeV]:', event_header[3])
        print ('First interaction height [m]:', -event_header[6]*1e-2)
        print ('Zenith angle [degree]:', np.rad2deg(event_header[10]))
        print ('Azimuth angle [degree]:', event_header[11])
        print ('x coordinate of the core location [m]:', -event_header[98]*1e-2)
        print ('y coordinate of the core location [m]:', -event_header[118]*1e-2)
    
    except StopIteration:    
        print ('Please enter a valid event number')
    
    except NotADirectoryError:
        print ('Please enter a valid run number')
    
    except docopt.DocoptExit as e:        
        print(e)
    
if __name__ == '__main__':    
    main()
