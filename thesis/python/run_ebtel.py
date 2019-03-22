"""
Function for automatically executing ebtel++ code
"""
import os
import subprocess
import tempfile

import numpy as np
import astropy.units as u
from synthesizAR.interfaces.ebtel import write_xml


def run_ebtel(config, ebtel_dir):
    with tempfile.TemporaryDirectory() as tmpdir:
        config['output_filename'] = os.path.join(tmpdir, 'ebtelplusplus.tmp')
        write_xml(config, os.path.join(tmpdir, 'ebtelplusplus.tmp.xml'))
        subprocess.call([os.path.join(ebtel_dir, 'bin', 'ebtel++.run'),
                         '-c', os.path.join(tmpdir, 'ebtelplusplus.tmp.xml')])
        data = np.loadtxt(config['output_filename'])
        terms = {}
        if config['save_terms']:
            data_terms = np.loadtxt(config['output_filename']+'.terms')
            terms['f_e'] = data_terms[:,0]
            terms['f_i'] = data_terms[:,1]
            terms['c_1'] = data_terms[:,2]
            terms['rad'] = data_terms[:,3]
    return {**{
        'time': data[:, 0]*u.s,
        'electron_temperature': data[:, 1]*u.K,
        'ion_temperature': data[:, 2]*u.K,
        'density': data[:, 3]/(u.cm**3),
        'electron_pressure': data[:, 4]*u.dyne/(u.cm**2),
        'ion_pressure': data[:, 5]*u.dyne/(u.cm**2), 
        'velocity': data[:, 6]*u.cm/u.s,
        'heat': data[:,7]*u.erg/u.s/(u.cm**3),
    }, **terms}
