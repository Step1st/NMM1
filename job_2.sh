#!/bin/bash
#SBATCH -p main
#SBATCH -N1
#SBATCH -n4
mkdir work
cd ./work
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python sierpinski_triangle_hpc.py -o points.csv