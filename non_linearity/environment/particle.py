import numpy as np
from single_photons.utils.constants import *


class Particle:
    def __init__(self, omega, gamma, radius=147e-9, rho=2200):  
        self.__omega__ = omega
        self.__gamma__ = gamma
        self.A = np.array([[0, self.__omega__],
                           [-self.__omega__, -self.__gamma__]])
        self.B = np.array([[0], [1]])
        self.C = np.array([[1, 0]])
        self.G = np.array([[0], [1]])
        self._m_ = rho*4*np.pi*np.power(radius, 3)/3
    def step(self, states, control=0.0, delta_t=50e-2):
        if states.size > 2:
            raise ValueError('States size for this specific system is equal to two \
                (position and velocity)')
        thermal_force = np.sqrt(2*self.__gamma__)*np.random.normal()
        state_dot = np.matmul(self.A,states) + self.B*control
        states = states + state_dot*delta_t + self.G*np.sqrt(delta_t)*(thermal_force)
        return states