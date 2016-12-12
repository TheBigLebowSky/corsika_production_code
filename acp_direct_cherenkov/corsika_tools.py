import corsika_wrapper as cw
import os

def PRMPAR_2_human_readable(prmpar):
    """
    Only for atomic nuclei.
    """
    if prmpar == 14:
        return 'A1_Z1'
    elif prmpar > 100:
        charge = prmpar%100
        mass = (prmpar - charge)/100

        return 'A'+str(int(mass))+'_'+'Z'+str(int(charge))
    else:
        return 'PRMPRAR_'+str(prmpar)


def corsika_directory():
    corsika_executable_path = cw.get_corsika_executable_from_config()
    run_dir = os.path.split(corsika_executable_path)[0]
    corsika_dir = os.path.split(run_dir)[0]
    return corsika_dir