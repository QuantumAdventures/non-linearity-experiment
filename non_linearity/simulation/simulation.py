import numpy as np
from numba import jit


@jit(nopython=True)
def simulation(omega, gamma, noise_std, dt, N_time, G):
    state = np.zeros(shape=(N_time, 2))
    p = 0
    x = 0
    for k in range(N_time):
        p = (
            p
            - gamma * p * dt
            - omega * x * dt
            + G * (x**3) * dt
            + noise_std * np.sqrt(dt) * np.random.normal()
        )
        x = x + omega * p * dt
        state[k, 1] = p
        state[k, 0] = x
    return state[:, 0]
