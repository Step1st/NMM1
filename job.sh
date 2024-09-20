#!/bin/bash
#SBATCH -p main
#SBATCH -N1
#SBATCH -n4
cd ./nmm
source ./.venv/bin/activate
python sierpinski_triangle_hpc.py -o test1.csv