import random

import numpy as np


class statevector:

    def __init__(self, numQubits:int):
        if numQubits > 5:
            raise ValueError('Too many qubits!')
        self.dimension = numQubits
        self.state = np.ndarray(2**numQubits, dtype=np.cdouble).reshape(np.ones(numQubits)*2)
        (self.state(tuple(np.ones(numQubits))))

    def isvalid(self) -> bool:
        return np.isclose(np.linalg.norm(self.state), 1)

    def ispure(self) -> bool:
        return np.isclose(np.linalg.trace(np.linalg.matrix_power(self.state.T @ self.state, 2)), 1)

    def densityMatrix(self):
        return self.state.T @ self.state

    def measure(self, qubit: int) -> int:
        # Pick a cutoff
        r = random.uniform(0, 1)
        # Get the desired qubit
        amplitudes = np.take(self.state, [0, 1], qubit)

        idx = [slice(None)] * self.dimension
        idx[qubit] = (0, 1)

        # Collapse the state and return the measurement
        if r < abs(amplitudes[0]):
            self.state[idx] = [1, 0]
            return 0
        else:
            self.state[idx] = [0, 1]
            return 1


