from Hopfield_Network import *
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


SPARSE_PATTERN = True
NOISE_ITERATIVE = True
THETA = [-1, 0, 0.5, 1, 2]
np.random.seed(42)


def active_patterns(size, num_patterns=1, active_num=0.1):
    positions = np.arange(0, size * num_patterns)
    np.random.shuffle(positions)
    result = np.zeros(size * num_patterns)
    for i in range(round(active_num * (size * num_patterns))):
        result[positions[i]] = 1
    return np.array(result).reshape(-1, size)


def main():
    num_units = 100
    num_patterns = 20
    patterns = active_patterns(num_units, num_patterns)  # Generating 10% active patterns

    for theta in THETA:
        counter = np.zeros(num_patterns)
        for i in tqdm(range(num_patterns)):
            w = weights(patterns[:i + 1, :].reshape(i + 1, num_units), sparse_pattern=SPARSE_PATTERN)
            for j in range(i + 1):
                counter_aux, x_current = noised_images([0.1], patterns, j, counter, w, return_data=True,
                                                       iterative_patterns=NOISE_ITERATIVE, theta=theta,
                                                       sparse_pattern=SPARSE_PATTERN, noised_iterations=50)
                counter[i] += iterative_patterns_accuracy(patterns[:i+1, :], x_current)
        plt.plot(np.linspace(start=1, stop=num_patterns, num=len(counter)), counter,
                 label=r"$\theta = {}$".format(theta))
    plt.xlabel('Training patterns')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
