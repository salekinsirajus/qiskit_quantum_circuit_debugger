# Best Effort Breakpoint Debugging on a Qunatum Circuit
Group project Qunatum Computing Fall 2022. Group memebrs: Palvit Garg, Harsh
Joshi, and Shawn Salekin

### Problem Description
- Cannot breakpoint debug
- measurement destroys superpositions, entanglements

Best-effort breakpoint debugging with execution. Rough steps:
1. Run up to breakpoint, take 1000 samples
2. Identify Hadamard positioning, entanglements/un-entangle
3. Create synthetic circuit (aka. state preparation) to resemble H/entanglements
4. Histograms of states (for classically-equivalent states)
5. Use circuit as an initalizer (aka. state preparation -> Qiskit API), run original circuit from breakpoint onward

Although the output will only examine a subset of original states. It is Still better than no breakpoint debugging. We will provide scenarios to demonstrate this point.
