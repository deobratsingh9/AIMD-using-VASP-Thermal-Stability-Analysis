#!/bin/bash
#SBATCH -J 2D_CP
#SBATCH -N 4 --exclusive
#SBATCH --ntasks-per-node=32
#SBATCH -t 024:00:00
#SBATCH -A xxx

module load VASP/5.4.4.16052018-nsc1-intel-2018a-eb
mpprun vasp_gam
