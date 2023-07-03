from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute
from qiskit import Aer

backend = Aer.get_backend('unitary_simulator')

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

circuit = QuantumCircuit(q,c)

circuit.h(q[0])
circuit.cx(q[0],q[1])

print(circuit)

job = execute(circuit, backend, shots=8192)
result = job.result()

print(result.get_unitary(circuit,3))
