---
tag: 3218XHTDPK
kind: definition
name: LOCC
msc: [81P48, 81P40]
defines: F5EB23T03M
uses: [EY0X2NKA3S, CGY299QMC3, 10VZYJ4552, F1K9J81GCT, 7F386TSFRW]
sources:
  - url: https://en.wikipedia.org/wiki/LOCC
---

## Definition

Let $H_A$ and $H_B$ be finite-dimensional complex Hilbert spaces, and write $B(H)$ for the operators on a space $H$.
A *local instrument* of party $A$ is a finite family $(\mathcal{E}_j)_j$ of [[completely positive maps|CGY299QMC3]] on $B(H_A)$ whose sum $\sum_j \mathcal{E}_j$ preserves the trace.
Local instruments of party $B$ are defined in the same way on $B(H_B)$.
The set of *LOCC channels* on $B(H_A \otimes H_B)$ is the smallest set of maps with these properties:

1. For all [[quantum channels|10VZYJ4552]] $\mathcal{E}$ on $B(H_A)$ and $\mathcal{F}$ on $B(H_B)$, the map $\mathcal{E} \otimes \mathcal{F}$ is an LOCC channel.
2. If $(\mathcal{E}_j)_j$ is a local instrument of $A$ and each $\Lambda_j$ is an LOCC channel, then $\sum_j \Lambda_j \circ (\mathcal{E}_j \otimes \id)$ is an LOCC channel.
3. If $(\mathcal{F}_j)_j$ is a local instrument of $B$ and each $\Lambda_j$ is an LOCC channel, then $\sum_j \Lambda_j \circ (\id \otimes \mathcal{F}_j)$ is an LOCC channel.

In clauses 2 and 3, one party measures, announces the outcome $j$, and the protocol continues with $\Lambda_j$.

## Remarks

Example: Alice measures her qubit in the basis $|0\rangle, |1\rangle$ and Bob applies the flip $X$ when the outcome is $1$.
With $\mathcal{E}_j(\rho) = |j\rangle\langle j| \rho |j\rangle\langle j|$ and $\Lambda_j = \id \otimes \mathcal{X}^j$, where $\mathcal{X}(\tau) = X \tau X$, the map is $\sum_j \Lambda_j \circ (\mathcal{E}_j \otimes \id)$.
Each $\Lambda_j$ is LOCC by clause 1, so the map is LOCC by clause 2.

Non-example: the controlled-NOT gate on $\C^2 \otimes \C^2$ maps the product state $\tfrac{1}{\sqrt 2}(|0\rangle + |1\rangle) \otimes |0\rangle$ to the entangled state $\tfrac{1}{\sqrt 2}(|00\rangle + |11\rangle)$.
Every LOCC channel maps [[separable states|7F386TSFRW]] to separable states, so this gate is not LOCC.

Every LOCC channel is a separable operation: it has Kraus operators of product form $A_k \otimes B_k$.
The converse fails: there are separable operations that are not LOCC.
Some authors also allow countably many rounds, or take the closure of the set of LOCC channels.
