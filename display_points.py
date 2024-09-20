import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=argparse.FileType("r"), default='./points.csv')
args = parser.parse_args()

points = np.genfromtxt(args.file, delimiter=',', skip_header=1 )
x, y = points.T

plt.scatter(x, y, s=0.1)
plt.show()