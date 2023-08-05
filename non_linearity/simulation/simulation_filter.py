import numpy as np
from numba import jit


@jit(nopython=True)
def simulation_filter(omega, gamma, noise_std, dt, N_time, G, delay, a, b):
    state = np.zeros(shape=(N_time, 2))
    x_window = np.zeros(b.shape)
    y_window = np.zeros((a.shape[0] - 1))
    y_i = 0
    p = 0
    x = 0
    for k in range(N_time):
        x_window[1:] = x_window[:-1]
        x_window[0] = x
        y_i = (b * x_window).sum() - (a[1:] * y_window).sum()
        y_window[1:] = y_window[:-1]
        y_window[0] = y_i

        p = (
            p
            - gamma * p * dt
            - omega * x * dt
            + G * (y_i**3) * dt
            + noise_std * np.sqrt(dt) * np.random.normal()
        )
        x = x + omega * p * dt
        state[k, 1] = p
        state[k, 0] = x
    return state[:, 0]
