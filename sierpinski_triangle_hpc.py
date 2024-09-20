import argparse
import numpy as np
import pandas as pd
from numba import njit, prange, set_num_threads, get_num_threads
import matplotlib.pyplot as plt


@njit(parallel=True)
def generate_points_parallel(vertices, num_chains, chain_length):
    total_iters = num_chains * chain_length
    x = np.empty(total_iters)
    y = np.empty(total_iters)
    for i in prange(num_chains):
        new_point = vertices[np.random.randint(0, 3)]
        idx = i * chain_length
        for j in range(chain_length):
            vertex_idx = np.random.randint(0, 3)
            new_point = (vertices[vertex_idx] + new_point) / 2.0
            x[idx + j] = new_point[0]
            y[idx + j] = new_point[1]
    return x, y


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--threads", type=int, default=get_num_threads())
parser.add_argument("-i", "--iterations", type=int, default=1_000_000)
parser.add_argument("-o", "--output", type=argparse.FileType("w"))
args = parser.parse_args()

set_num_threads(args.threads)

total_iters = args.iterations
num_chains = args.threads
chain_length = int(total_iters / num_chains)

vertices = np.array([(0.0, 10.0), (5.0, 10.0), (2.5, 15.0)])
x, y = generate_points_parallel(vertices, num_chains, chain_length)


if args.output:
    df = pd.DataFrame({"x": x, "y": y})
    df.to_csv(args.output, index=False)

else:
    plt.scatter(x, y, s=0.1)
    plt.show()
