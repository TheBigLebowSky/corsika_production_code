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