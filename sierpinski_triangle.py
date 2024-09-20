import random
import matplotlib.pyplot as plt


def generate_random_point_in_triangle(vertices):
    r1 = random.uniform(0, 1)
    r2 = random.uniform(0, 1)

    if r1 + r2 > 1:
        r1 = 1 - r1
        r2 = 1 - r2
    point = (
        (1 - r1 - r2) * vertices[0][0] + r1 * vertices[1][0] + r2 * vertices[2][0],
        (1 - r1 - r2) * vertices[0][1] + r1 * vertices[1][1] + r2 * vertices[2][1],
    )
    return point


def generate_points(vertices: list[tuple[float, float]], iters: int):
    x: list[float] = []
    y: list[float] = []
    new_point = vertices[random.randint(0, 2)]
    for _ in range(0, iters):
        vertex_idx = random.randint(0, 2)
        new_point = (
            (vertices[vertex_idx][0] + new_point[0]) / 2,
            (vertices[vertex_idx][1] + new_point[1]) / 2,
        )
        x.append(new_point[0])
        y.append(new_point[1])
    return x, y


if __name__ == "__main__":
    vertices: list[tuple[float, float]] = [(0.0, 10.0), (5.0, 10.0), (2.5, 15.0)]
    x, y = generate_points(vertices, 1_000_000)

    plt.plot(vertices[0][0], vertices[0][1], marker="o")
    plt.plot(vertices[1][0], vertices[1][1], marker="o")
    plt.plot(vertices[2][0], vertices[2][1], marker="o")
    plt.scatter(x, y, s=0.1)
    plt.show()
