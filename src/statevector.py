import numpy as np


class statevector:

    def __init__(self, numQubits:int):
        if numQubits > 5:
            raise ValueError('Too many qubits!')
        self.state = np.ndarray(2**numQubits, dtype=np.cdouble).reshape(np.ones(numQubits)*2)

    def isvalid(self) -> bool:
        return np.isclose(np.linalg.norm(self.state), 1)

    def ispure(self) -> bool:
        return np.isclose(np.linalg.trace(np.linalg.matrix_power(self.state.T @ self.state, 2)), 1)

