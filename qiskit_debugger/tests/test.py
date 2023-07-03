from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit
from qiskit_debugger import QuantumDebugCircuit, QCDebugger, run_circuit, hw_backend

qc = QuantumDebugCircuit(2)
qc.x(0)
qc.h(range(2))
qc.cx(0, 1)
qc.h(range(2))
qc.bp()      # <-- Add a breakpoint here
qc.h(range(2))
qc.x(range(2))
qc.bp()      # <-- Add a breakpoint here
qc.cx(1, 0)
qc.h(range(2))
qc.bp()

qc.draw()

qdb = QCDebugger(qc)
qdb.c()
qdb.c()
qdb.c()
qdb.c()
