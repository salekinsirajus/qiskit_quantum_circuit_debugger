from qiskit import Aer, execute, transpile
from qiskit import QuantumCircuit


def run_circuit(circ, simulator='qasm_simulator'):
    backend = Aer.get_backend(simulator)
    job = execute(circ, backend, shots=1000)
    result = job.result()

    return result


class QCDebugger:

    def __init__(self, qc):
        """Debugger object that acts as a runner, similar to the GDB interface"""
        self.qc = qc 
        self.re_qc = None

        self._last_breakpoint = None
        self._next_breakpoint = None
        self._unitary_for_next_bp = None
        self._circuit_for_next_bp = None
        # TODO: options will be added later
    
        if self._validate_circuit() == False:
            raise Exception("Circuit provided is cannot be used with a debugger")
            

    def _validate_circuit(self):
        """ensure there is no invalid instructions in the circuit"""
        # circuits with measurements cannot produce unitary matrix

        return True
    
    def resynthesize_circuit(self, unitary):
        """Create, transpile and ready to run"""
        nqubits = self.qc.num_qubits
        re_qc = QuantumCircuit(nqubits)
        re_qc.unitary(unitary, range(nqubits)) 
        re_qc = transpile(re_qc, basis_gates = ['cx', 'u3'])

        return re_qc


    def get_unitary_from_run(self):
        return

    def _continue(self):
        """do a simultaneous run on simulator"""
        # find the next barrier
       
        # run unitary simulation till that point
        # FIXME: this self.qc will change it will be only b/w this and next bp
        unitary_run = run_circuit(self.qc, 'unitary_simulator')
        unitary = unitary_run.get_unitary()
        self.re_qc = self.resynthesize_circuit(unitary)

        self.qc.measure_all() #FIXME: Measurement should be removed
        probability_run_result = run_circuit(self.qc, 'qasm_simulator')
        print(probability_run_result.get_counts())

    def c(self):
        """c(ontinue): run until the next breakpoint"""
        return self._continue()

