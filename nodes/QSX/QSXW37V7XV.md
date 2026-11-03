---
tag: QSXW37V7XV
kind: statement
role: theorem
name: Quantum threshold theorem
msc: [81P73, 68Q12, 81P68]
uses: [S82TXJB05T, M4BSARXSCC, P2TBJXVGEC]
about: [M4BSARXSCC, S82TXJB05T]
sources:
  - url: https://en.wikipedia.org/wiki/Threshold_theorem
same_as:
  wikidata: Q7269106
  wikipedia: Threshold theorem
---

## Statement

Consider [[quantum circuits|S82TXJB05T]] built from four kinds of operations: one- and two-qubit gates, preparations of fresh qubits in $\lvert 0 \rangle$, measurements and idle steps.
Any number of operations may act in parallel, and fast classical computation is free.
Assume local stochastic noise of strength $p$: each operation fails independently with probability at most $p$.
A failed operation is replaced by an arbitrary quantum operation on the same qubits.
Then there is a constant $p_{\mathrm{th}} > 0$, the threshold, with the following property.
If $p < p_{\mathrm{th}}$, then for every ideal circuit $C$ with $N$ operations and every $\varepsilon > 0$ there is a circuit $C'$ with $O(N \operatorname{polylog}(N/\varepsilon))$ operations.
Under the noise, the output distribution of $C'$ is within total variation distance $\varepsilon$ of the output distribution of $C$ without noise.

## Remarks

Proof idea: encode each qubit in a [[quantum error-correcting code|M4BSARXSCC]] and replace each operation by a fault-tolerant gadget that does not spread a single fault into an uncorrectable error.
Then a level-$1$ logical operation fails with probability at most $c p^2$ for a constant $c$.
Concatenating the code $k$ times gives logical failure probability at most $p_{\mathrm{th}} (p/p_{\mathrm{th}})^{2^k}$ with $p_{\mathrm{th}} = 1/c$.
So the error falls doubly exponentially in $k$ while the size grows only exponentially in $k$, which gives the polylogarithmic overhead.

The hypothesis of fresh qubits is needed: error correction removes entropy from the computer, and without a supply of fresh qubits the entropy builds up and long computations fail.
The parallelism is needed so that errors can be corrected on all qubits at every time step.

Example: with [[stabilizer codes|P2TBJXVGEC]] such as surface codes, numerical studies estimate thresholds of the order of $1\%$ for some noise models.

## Explanations

### L1 human

Real quantum hardware is noisy, and one might fear that errors always pile up in a long computation.
The threshold theorem says that this is not so: if each component is better than some fixed quality level, arbitrarily long quantum computations can be made reliable.
The cost is only a modest, polylogarithmic factor in the number of operations.

### L2 human

The theorem was proved independently in the late 1990s by Aharonov and Ben-Or, by Kitaev, and by Knill, Laflamme and Zurek.
It is the quantum analogue of von Neumann's theorem on reliable computation with unreliable components.
The value of $p_{\mathrm{th}}$ depends on the noise model, the code and the gadgets, and the rigorous lower bounds are far below the numerical estimates.
The theorem also holds for some correlated noise models with suitably decaying correlations.
