# Breakpoint Debugging on a Physical Qunatum Circuit

## Group Members
- Palvit Garg (pgarg5)
- Harshwardhan Joshi (hjoshi2)
- Shawn Salekin (ssaleki)

#### Presentation
[URL](https://docs.google.com/presentation/d/1SCwHKmPCc7U0Hl_CVZLNMto9HAEyD_zuz_fqGwnIzuc/edit?usp=sharing)

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

## How To Test
We are assuming you are faimilar with Qiskit and git. We'd also assume you have
jupyter notebook installed on your system. Ensure the following python libraries
are installed in either a) python virtual environment, or b) jupyter notebook kernel.

```
qiskit-ibm-runtime==0.6.2
qiskit-aer==0.11.0
matplotlib==3.6.0
```

## Solution Approaches 
Let’s assume we have a circuit with multiple qubits, and it has a breakpoint
brk. The circuit before the breakpoint is called A, and after is called B. The
target is to measure the state of qubits at point brk.

To “recreate”, i.e., synthesize an equivalent circuit right after it is
measured, we thought of two possible methods. 

~~1. **Approach 1**:
We make two circuits of varying length: one ends at the breakpoint, and the
other stops at the original end without stopping at the breakpoint. Then we run
both of these circuits.~~

(update 11/05/22): since this is a trivial and inefficient implementation, we
will focus our attention to approach 2.

2. **Approach 2**:
Create a custom gate using the unitary matrix that results from running circuit
part A, save it somewhere. Then create a custom gate using the saved unitary
matrix to circuit part B.This custom gate is equivalent to the circuit part A.
Now run this custom gate and then part B.

## Final Result
We implemented a hybrid approach that uses both a simulator and a hardware

## Open Problems
Some of them

## Contributions During the Final Round
- Research and experiments with pure hawrdware approach - Palvit
- Experiments and implementation with simulator approach - Shawn
- Benchmakring, experiments, and final reports - Harsh

## Progress Made (Round 2)
- Synthesized a new circuit based on a unitary matrix and run it on a real
  hardware.
- Assessed the importance of phase date in synthesizing a circuit from breakpoint
- Investigated different methods of generating unitary matrices

## Timeline (Detailed & Revised) 
- Confirm whether and under what condition we can generate a unitary from a
  hardware run (11/12/2022)
- Decide whether to use simulation or hardware based on the outcome of
  generating unitary from the hardware runs (11/12/2022)
- Validate whether the phase data obtained from simulation(s) can be used in
  synthesizing an equivalent circuit after a breakpoint 
- Figure out a method to extract phase data from parallel simulation runs (11/19/2022) 
- Implement a qiskit module/extension that would allow qiskit users to add
  breakpoint(s) to their circuit.(11/26/2022)
- Add tests and run a number of experiments to validate the correctness of our
  implementation.(11/26/2022)

## Project Timeline (Original)
- 11/01/2022: Implement approach 1
- 11/10/2022: Analyze the feasibility of implementing approach 2.
- 11/26/2022: Implement approach 2 (or a better one)

## Future Readings
- https://dl.acm.org/doi/abs/10.1145/3373376.3378488
- https://arxiv.org/pdf/2103.09172.pdf

## References
- https://qiskit.org/documentation/tutorials/circuits_advanced/02_operators_overview.html
- https://qiskit.org/documentation/stubs/qiskit.converters.circuit_to_instruction.html
- https://github.ncsu.edu/fmuelle/qc19/tree/master/hw/hw6/m3/csc591-quantum-debugging
- https://quantumcomputing.stackexchange.com/questions/27064/how-to-get-statevector-of-qubits-after-running-quantum-circuits-on-ibmq-real-har

