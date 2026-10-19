import random

import numpy as np


class statevector:

    def __init__(self, numQubits:int):
        if numQubits > 5:
            raise ValueError('Too many qubits!')
        self.dimension = numQubits
        self.state = np.full((2,) * numQubits, 1 / (2**(numQubits / 2)), dtype=np.cdouble)
        self.rng = np.random.default_rng(42)

    def is_valid(self) -> bool:
        return np.isclose(np.linalg.norm(self.state), 1)

    def is_pure(self) -> bool:
        return np.isclose(np.linalg.trace(np.linalg.matrix_power(self.density_matrix(), 2)), 1)

    def density_matrix(self):
        flat = self.state.flatten()
        return np.outer(flat, flat.conj())

    def measure(self, qubit: int = 0) -> int:
        # Pick a cutoff
        r = self.rng.random()

        # Get probability of each outcome
        prob_zero = np.sum(np.abs(self.state[(slice(None),) * qubit + (0,)]) ** 2)


        if r < prob_zero:
            # We measure zero

            # Renormalize

            # Zero out all states which have a 1 in this qubit
            self.state[(slice(None),) * qubit  + (1,)] = 0

            # Renormalize remaining amplitudes: divide by sqrt(p_zero)
            self.state[(slice(None),) * qubit + (0,)] /= np.sqrt(prob_zero)

            # Return the measurement
            return 0
        else:
            # We measure one
            # Renormalize

            # Zero out all states which have a 0 in this qubit
            self.state[(slice(None),) * qubit  + (0,)] = 0

            # Renormalize remaining amplitudes: divide by sqrt(p_one)
            prob_one = np.sum(np.abs(self.state[(slice(None),) * qubit + (1,)]) ** 2)

            self.state[(slice(None),) * qubit + (1,)] /= np.sqrt(prob_one)

            return 1



    def singleQubitGate(self, gateMat:np.ndarray, targetQubit = 0):
        if not gateMat.shape == [2, 2]:
            raise ValueError("Single Qubit Gate must be 2x2")

        if not np.allclose(gateMat.T.conj() @ gateMat, np.identity(2)):
            raise ValueError("Nonunitary gate passed")


