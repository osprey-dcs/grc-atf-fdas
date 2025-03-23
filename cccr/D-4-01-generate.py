#!/usr/bin/env python3
"""
Generate CCCR CSV file needed for D.4.1
"""

from pathlib import Path

def emit_cccr(inuse:set, out:Path):
    with out.open('w') as F:
        F.write('CHASSIS,CHANNEL,CONNECTOR,SIGNAL,CUSTNAME,USE,DESC,COUPLING,EGU,ESLO,EOFF,LOLOlim,LOlim,HIlim,HIHIlim\n')
        for chas in range(1,33):
            for chan in range(1,33):
                conn = 'DB1' if chan>=17 else 'DB2'
                signum = (chas-1)*32 + chan
                use = 'Yes' if signum in inuse else 'No'

                F.write(f'{chas},{chan},{conn},{signum},{chas:02d}-{conn}-{chan:02d}-{signum:04d},{use},NONE,DC,V,1,0,-9.99,-9.99,9.99,9.99\n')

def getargs():
    from argparse import ArgumentParser
    P = ArgumentParser()
    P.add_argument('outdir', type=Path)
    return P

def main(args=None):
    args = args or getargs().parse_args()

    outdir: Path = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    # One with all channels in USE
    emit_cccr(set(range(1,1025)), outdir / 'D-4-01-all-channels.csv')

    # Files with all channels for one chassis in USE
    for chas in range(1,33):
        sigbase = (chas-1)*32 + 1
        emit_cccr(set(range(sigbase,sigbase+32)), outdir / f'D-4-01-chassis-{chas:02d}.csv')

if __name__=='__main__':
    main()
