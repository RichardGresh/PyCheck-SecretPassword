#!/usr/bin/env python3
# Richard Gresham
# CPSC 386-01
# 2021-09-05
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab 00-00
#

""" pycheck.py generates a secret code when executed on Linux """

import codecs
import subprocess
import sys
import time
import urllib.parse

def main():
    """ A crazy main function that will test a few things. """
    blob = '%23%21%2Fhfe%2Fova%2Frai+clguba3%0A%0A%23vzcbeg+gvzr'\
    '%2C+flf%2C+fhocebprff%0A%0Aqrs+znva%28%29%3A%0A++++vs+flf.cy'\
    'ngsbez.fgnegfjvgu%28%27jva32%27%29+be+flf.cyngsbez.fgnegfjvg'\
    'u%28%27pltjva%27%29+be+flf.cyngsbez.fgnegfjvgu%28%27qnejva%2'\
    '7%29%3A%0A++++++++cevag%28%27Cyrnfr+hfr+Yvahk.+Ab+frperg+pbq'\
    'r+sbe+lbh+hagvy+lbh+hfr+Yvahk.%27%29%0A++++++++rkvg%281%29%0'\
    'A++++ryvs+flf.cyngsbez.fgnegfjvgu%28%27yvahk%27%29%3A%0A++++'\
    '++++cevag%28%27Lnl+Yvahk%21%27%29%0A++++ryvs+flf.cyngsbez.fg'\
    'negfjvgu%28%27serrofq%27%29%3A%0A++++++++cevag%28%27Lnl+Serr'\
    'OFQ%21%21%27%29%0A++++ryfr%3A%0A++++++++cevag%28%27Pbhyq+abg'\
    '+qrgrezvar+cyngsbez.+Cyrnfr+gryy+gur+vafgehpgbe.+Ab+frperg+p'\
    'bqr+trarengrq.%27%29%0A++++++++rkvg%280%29%0A%0A++++a+%3D+fg'\
    'e%28gvzr.pybpx_trggvzr_af%28gvzr.PYBPX_ZBABGBAVP%29%29%0A%0A'\
    '++++gel%3A%0A++++++++cevag%28%22Lbhe+frperg+pbqr+vf%3A%22%29'\
    '%0A++++++++pc+%3D+fhocebprff.eha%28%5B%27rpub+%22PCFP+386+fv'\
    'ghngvba+abezny+%7B%7D%22+%7C+o2fhz+%7C+phg+-s+1+-q%5C+%27.sb'\
    'ezng%28a%29%5D%2C+pncgher_bhgchg%3DGehr%2C+furyy%3DGehr%2C+g'\
    'vzrbhg%3D3%2C+purpx%3DGehr%2C+grkg%3DGehr%29%0A++++++++vs+pc'\
    '.ergheapbqr+%3D%3D+0%3A%0A++++++++++++cevag%28%27%7B%7D%25%7'\
    'B%7D%27.sbezng%28fge%28pc.fgqbhg%29.efgevc%28%22%5Ca%5Ce%22%'\
    '29%2C+a%29%29%0A++++++++ryfr%3A%0A++++++++++++cevag%28%27Fbz'\
    'rguvat+jrag+jebat.+Gryy+lbhe+vafgehpgbe.%27%29%0A++++rkprcg+'\
    'fhocebprff.PnyyrqCebprffReebe%3A%0A++++++++cevag%28%27Gelvat'\
    '+gb+or+gevpxl%3F+Cyrnfr+hfr+Yvahk.+Ab+frperg+pbqr+trarengrq.'\
    '%27%29%0A%0Avs+__anzr__+%3D%3D+%27__znva__%27%3A%0A++++znva%'\
    '28%29%0A%0A'
    exec(codecs.decode(urllib.parse.unquote(blob).replace('+', ' '), 'rot_13'))

if __name__ == '__main__':
    main()

