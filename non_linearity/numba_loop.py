import numpy as np
from tqdm import tqdm
from scipy import signal as sn
from numba import jit
import matplotlib.pyplot as plt


radius = 75e-9
presure = 1e3
m_gas = 2.325e-26
T = 293.0
kb = 1.38064852e-23
v_gas = np.sqrt(3 * kb * T / m_gas)
gamma = 15.8 * radius**2 * presure / (v_gas)
rho = 2200
massa = rho * 4 * np.pi * radius**3 / 3
freq = 8e4
omega = 2 * np.pi * freq
spring = massa * omega**2
t_period = 1 / freq

max_time = 1600 * t_period
dt = t_period / 100

N_time = int(max_time / dt)

# psd_stamps = int(N_time / 2 + 1)
t = np.linspace(0, max_time, int(N_time)) / t_period


@jit(nopython=True)
def simulation(eee):
    state = np.zeros(shape=(N_time, 2))
    v = 0
    x = 0
    for k in range(N_time):
        v = (
            v
            - (gamma / massa) * v * dt
            - (spring / massa) * x * dt
            - 5e6 * (x**3) * dt / massa
            + np.sqrt(2.0 * kb * gamma * massa * T * dt) * np.random.normal() / massa
        )
        x = x + v * dt
        state[k, 1] = v
        state[k, 0] = x
    return state[:, 0]


def psd(traces, delta_t):
    pxxs = []
    for i in range(traces.shape[0]):
        freq, pxx = sn.welch(
            traces[i, :],
            fs=1 / delta_t,
            window="hamming",
            nperseg=int(traces.shape[0] / 2),
        )
        pxxs.append(pxx)
    return freq, np.array(pxxs).mean(axis=0)


def main():
    M = 100
    storage = np.zeros(shape=(M, N_time))

    for i in tqdm(range(M)):
        data = simulation(None)
        data = np.array(data)
        storage[i, :] = data
    print(dt)
    plt.plot(storage[0, :])
    plt.show()


#    freq, power = psd(storage, dt)
#    plt.semilogy(freq, power)
#    plt.show()


if __name__ == "__main__":
    main()
