#!/usr/bin/env python

import os
import glob


psps = ['esp','gbrv']
xcs = ['RPBE','BEEF','PBE']
pws = ['400','450','500','550','600','650','700']
#gases = ['CO','CO2','NH3','CH3OH','CH2O','N2','H2S','Cl2','O3']
gases = ['CO','CO2','NH3','CH3OH','N2','H2S','Cl2']
#gases = ['O3']

#test
#psps = ['esp']
#pws = ['400']
#xcs = ['RPBE']
#gases=['CH2O']



for gas in gases:
    for psp in psps:
        for xc in xcs:
            for pw in pws:
               traj_loc='/home/users/alatimer/work_dir/gases/%s/%s/%s/%s'%(gas,psp,xc,pw)
               lines = ' '.join(open(traj_loc+'/myjob.out','rb').readlines())
               if 'Zero-point energy' in lines:
                   #print "no rem: ",traj_loc
                   continue
               print "rem: ",traj_loc
               #print lines
               #print traj_loc
               #os.system('mkdir -p %s'%(traj_loc))
               #os.system('cp gas_opt.py %s'%(traj_loc))
               #os.system('cp trajs_gas/%s.traj %s/init.traj'%(gas,traj_loc))
               os.chdir(traj_loc)
               os.system('rm -r vib* calcdirv_* uniq* node*')

               print os.getcwd()
               #for pkl in glob.glob('vib.???.pckl'):
                #   if os.stat(pkl).st_size == 0:
                 #      os.system('echo rm %s'%(pkl))
               os.system(' sbatch --job-name=$(pwd) gas_opt.py %s %s /home/users/alatimer/bin/psp/%s/'%(xc, pw, psp))
               os.chdir('/home/users/alatimer/src/Delta/')
