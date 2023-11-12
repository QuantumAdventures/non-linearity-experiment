import numpy as np
from numba import jit


@jit(nopython=True)
def simulation(omega, gamma, noise_std, dt, N_time, G, delay):
    state = np.zeros(shape=(N_time, 2))
    p = 1
    x = 0
    for k in range(N_time):
        if k > delay:
            p = (
                p
                - gamma * p * dt
                - omega * x * dt
                + G * (state[k - delay - 1, 0] ** 3) * dt
                + noise_std * np.sqrt(dt) * np.random.normal()
            )
        else:
            p = (
                p
                - gamma * p * dt
                - omega * x * dt
                + noise_std * np.sqrt(dt) * np.random.normal()
            )
        x = x + omega * p * dt
        state[k, 1] = p
        state[k, 0] = x
    return state[:, 0]
