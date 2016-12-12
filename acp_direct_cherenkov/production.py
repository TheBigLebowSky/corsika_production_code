"""
Usage: acp_direct_cherenkov -c=CONFIG -o=OUTPUT -e=EVTIO_EXTRACTOR

Options:
    -h --help                               Prints this help message.
    -c --config=CONFIG                      Path to the production config json 
                                            file.
    -o --output=OUTPUT                      Path of the output directory.
    -e --evtio_extractor=EVTIO_EXTRACTOR    Path to the mctracer eventio 
                                            extractor.
"""
import os
import scoop
import docopt
import corsika_production_tools
import corsika_wrapper as cw

"""
def keep_stdout(text_path, cfg):
    shutil.copyfile(
        text_path, 
        os.path.join(
            cfg['output']['stdout'], 
            str(cfg['run']['number'])+'_'+os.path.basename(text_path)))



def event_io_converter(eventio_path, output_path, cfg):
    with open(output_path+'.stdout', 'w') as out, open(output_path+'.stderr', 'w') as err:
        subprocess.call([
            cfg['mctracer_eventio_converter_path'],
            '-i', eventio_path,
            '-o', output_path],
            stdout=out,
            stderr=err)   


def make_corsika_run(steering):
    
    with tempfile.TemporaryDirectory(prefix='dc_production_') as tmp_dir:
        eventio_path = os.path.join(tmp_dir, 'corsika_run.evtio')

        cw.corsika(
            steering_card=steering['corsika_steering_card'],
            output_path=eventio_path,
            save_stdout=True)

        keep_stdout()

        os.path.join(output_path(), 'corsika_75600_%d_run_%d.evtio' %(int(steering['steering_card']['PRMPAR'][0]),steering['run_number'])),
        
        event_io_converter(
            eventio_path=eventio_path,
            output_path=s.path.join()
        )
    return True
"""           

def main():
    try:
        arguments = docopt.docopt(__doc__)

        print('production main')

        """
        production_steering = read_steering(arguments['--steering_path'])
        corsika_steering_cards = make_all_corsika_steering_cards(production_steering)

        cfg = {}
        cfg['output_path'] = {}
        cfg['output']['directory'] = arguments['--output_path']
        os.mkdir(cfg['output']['directory'])




        #Make steering cards based on the given template
        steering_cards = corsika_production_tools.make_corsika_steering_cards(
                    prmpar=particle_id, 
                    number_of_runs=number_of_runs,
                    number_of_events=number_of_events, 
                    energy_range=energy_range,
                    cscat_x=cscat_x, cscat_y=cscat_y)


        #Run corsika
        result = list(scoop.futures.map(make_corsika_run, steering_cards))            
        """

    except docopt.DocoptExit as e:        
        print(e)
  
if __name__ == '__main__':    
    main()


