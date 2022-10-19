# Breakpoint Debugging on a Physical Qunatum Circuit

## Group Members
- Palvit Garg (pgarg5)
- Harshwardhan Joshi (hjoshi2)
- Shawn Salekin (ssaleki)

## Problem Description
In classical computing, debugging with breakpoint means halting the program
execution at any given point and freezing the program state. This allows
programmers to examine the program internals mid-execution (as in, what
variables contain which values, analyze control flow etc.) Unfortunately, in
quantum computing, doing this is not possible. Qubits in a quantum circuit have
probabilistic values (in superposition), and the act of measuring collapses the
qubits to a deterministic state.

Breakpoint debugging is still needed for quantum computing, so our problem boils
down to measuring at the breakpoint and preserving enough information to
“recreate” that state and continue execution from that point.

## Solution Approaches 
Let’s assume we have a circuit with multiple qubits, and it has a breakpoint
brk. The circuit before the breakpoint is called A, and after is called B. The
target is to measure the state of qubits at point brk.

To “recreate”, i.e., synthesize an equivalent circuit right after it is
measured, we thought of two possible methods. 

1. **Approach 1**:
We make two circuits of varying length: one ends at the breakpoint, and the
other stops at the original end without stopping at the breakpoint. Then we run
both of these circuits.

2. **Approach 2**:
Create a custom gate using the unitary matrix that results from running circuit
part A, save it somewhere. Then create a custom gate using the saved unitary
matrix to circuit part B.This custom gate is equivalent to the circuit part A.
Now run this custom gate and then part B.


## Project Timeline 
- 11/01/2022: Implement approach 1
- 11/10/2022: Analyze the feasibility of implementing approach 2.
- 11/26/2022: Implement approach 2 (or a better one)

## References
- https://qiskit.org/documentation/tutorials/circuits_advanced/02_operators_overview.html
- https://qiskit.org/documentation/stubs/qiskit.converters.circuit_to_instruction.html
- https://github.ncsu.edu/fmuelle/qc19/tree/master/hw/hw6/m3/csc591-quantum-debugging
- https://quantumcomputing.stackexchange.com/questions/27064/how-to-get-statevector-of-qubits-after-running-quantum-circuits-on-ibmq-real-har

