import numpy as np
import non_linearity.utils.constants as ct


class Particle:
    def __init__(self, omega, gamma, radius=147e-9, rho=2200, T=293):
        self.__omega__ = omega
        self.__gamma__ = gamma
        self.T = T
        self.A = np.array([[0, omega], [-omega, -gamma]])
        self.B = np.array([[0], [1]])
        self.C = np.array([[1, 0]])
        self.G = np.array([[0], [1]])
        self._m_ = rho * 4 * np.pi * np.power(radius, 3) / 3
        self.zp_x = np.sqrt(ct.hbar / (2 * omega * self._m_))
        self.zp_p = np.sqrt(omega * ct.hbar * self._m_ / 2)
        self.nl = ct.hbar * self.__omega__ / (ct.kb * self.T)
        self.C = np.array([[1, 0]])
        self.thermal_force_std = (
            np.sqrt(2 * self.__gamma__ * self._m_ * ct.kb * T) / self.zp_p
        )

    def step(self, states, control=0.0, delta_t=50e-2):
        if states.size > 2:
            raise ValueError(
                "States size for this specific system is equal to two \
                (position and velocity)"
            )
        thermal_force = self.thermal_force_std * np.random.normal()
        state_dot = np.matmul(self.A, states) + self.B * control
        states = states + state_dot * delta_t
        states = states + self.G * np.sqrt(delta_t) * thermal_force
        return states
