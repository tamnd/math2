---
tag: CP0JWNNWXG
kind: definition
name: Quantum circuit
msc: [81P68, 68Q12, 81P65]
defines: S82TXJB05T
uses: [71CFM8DEM8, E9QTT3XBXS, EY0X2NKA3S, SQXNFGVADX]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_circuit
---

## Definition

Let $n \ge 1$ and let $\mathcal{G}$ be a set of [[quantum logic gates|71CFM8DEM8]], called the gate set.
A *quantum circuit* on $n$ [[qubits|E9QTT3XBXS]] over $\mathcal{G}$ is a finite sequence $((G_1, t_1), \dots, (G_m, t_m))$ with the following properties.

1. Each $G_j$ is a $k_j$-qubit gate in $\mathcal{G}$, with $k_j \le n$.
2. Each $t_j$ is a $k_j$-tuple of distinct indices in $\set{1, \dots, n}$.

Let $\widetilde{G}_j$ be the operator on $(\C^2)^{\otimes n}$ obtained by applying $G_j$ to the qubits $t_j$.
The circuit *implements* the unitary operator $U = \widetilde{G}_m \cdots \widetilde{G}_2 \widetilde{G}_1$.
The number $m$ is the *size* of the circuit.

## Remarks

Example: let $n = 2$ and the circuit be $((H, (1)), (\mathrm{CNOT}, (1, 2)))$, with $H$ the Hadamard gate.
Then $\lvert 00 \rangle \mapsto \frac{1}{\sqrt2}(\lvert 00 \rangle + \lvert 10 \rangle) \mapsto \frac{1}{\sqrt2}(\lvert 00 \rangle + \lvert 11 \rangle)$, a Bell state.

Non-example: the sequence $((\mathrm{CNOT}, (1, 1)))$ is not a circuit, because the indices in $t_1$ are not distinct; a gate cannot act twice on the same qubit at once.

The *depth* is the least number of layers into which the sequence can be cut, in order, such that the gates in one layer act on disjoint qubits.
Many authors also allow measurements and classical control inside a circuit; by the principle of deferred measurement, these can be moved to the end at small cost.
