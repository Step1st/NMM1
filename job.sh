#!/bin/bash
#SBATCH -p main
#SBATCH -N1
#SBATCH -n6
source .venv/bin/activate
python sierpinski_triangle_hpc.py -o points.csv