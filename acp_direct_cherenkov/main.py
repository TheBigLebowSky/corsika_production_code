"""
Usage: acp_direct_cherenkov [-s=SCOOP_HOSTS] -c=CONFIG -o=OUTPUT -e=EVTIO_EXTRACTOR

Options:
    -h --help                               Prints this help message.
    -s --scoop_hosts=SCOOP_HOSTS            Path to the scoop hosts text file.
    -c --config=CONFIG                      Path to the production config json 
                                            file.
    -o --output=OUTPUT                      Path of the output directory.
    -e --evtio_extractor=EVTIO_EXTRACTOR    Path to the mctracer eventio 
                                            extractor.
"""
import docopt
import subprocess
import pkg_resources


def main():
    try:
        arguments = docopt.docopt(__doc__)
    
        production = pkg_resources.resource_filename(
                'acp_direct_cherenkov', 
                'production.py')

        command = [
            'python',
            '-m', 'scoop',
            production,
            '--config', arguments['--config'],
            '--output', arguments['--output'],
            '--evtio_extractor', arguments['--evtio_extractor']] 

        if arguments['--scoop_hosts']:
            command.insert(3, '--hostfile')
            command.insert(4, arguments['--scoop_hosts'])

        return subprocess.call(command)

    except docopt.DocoptExit as e:
        print(e)


if __name__ == '__main__':
    main()