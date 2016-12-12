import json


example_steering = {
	'nuclei':[
    	{'PRMPAR': 5626, 'NRUN': 100, 'Emin': 50, 'Emax': 60, 'ESLOPE':-2.7},
    	{'PRMPAR': 1206, 'NRUN': 100, 'Emin': 50, 'Emax': 60, 'ESLOPE':-2.7},
    ],
    'max_scatter_radius': 75e2,
    'max_zenith_distance': 0.0,
    'NSHOW': 1
}


def write_steering(steering, path):
    with open(path, 'w') as outfile:
        json.dump(steering, outfile)


def read_steering(path):
	with open(path, 'r') as infile:
		steering = json.load(infile)
	return steering