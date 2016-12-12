import json


example_config = {
	'nuclei':[
    	{'PRMPAR': 5626, 'NRUN': 100, 'Emin': 50, 'Emax': 60, 'ESLOPE':-2.7},
    	{'PRMPAR': 1206, 'NRUN': 100, 'Emin': 50, 'Emax': 60, 'ESLOPE':-2.7},
    ],
    'max_scatter_radius': 75e2,
    'max_zenith_distance': 0.0,
    'NSHOW': 1
}


def write_config(config, path):
    with open(path, 'w') as outfile:
        json.dump(config, outfile)


def read_config(path):
	with open(path, 'r') as infile:
		config = json.load(infile)
	return config