---
tag: TYX54W4X6R
kind: definition
name: Topological insulator
msc: [82D20, 81V70, 19L64]
defines: X66S7EJ1R7
uses: [QP0TK2M29V, EKTERAYFJ2, CX8GDHENTT]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_insulator
---

## Definition

Let $d \ge 1$ and let $T^d = \R^d / \Lambda^*$ be the [[Brillouin zone|EKTERAYFJ2]] torus of a crystal.
A *band insulator* is a continuous family $k \mapsto H(k)$ of Hermitian $N \times N$ matrices on $T^d$, the Bloch Hamiltonians (see [[band structure|QP0TK2M29V]]).
It comes with a Fermi energy $E_F$ that is not an eigenvalue of any $H(k)$.
Fix a symmetry class, that is, a set of symmetry conditions on $H$ such as time-reversal symmetry $\Theta H(k) \Theta^{-1} = H(-k)$ with an antiunitary $\Theta$.
The insulator is *topologically trivial* if it can be deformed to a $k$-independent Hamiltonian, after possibly adding extra $k$-independent bands.
The deformation must pass through band insulators of the same symmetry class, so $E_F$ never becomes an eigenvalue.
A *topological insulator* is a band insulator that is not topologically trivial.

In the narrow sense, a topological insulator is one of class AII in dimension $d = 2$ or $3$ whose strong $\Z_2$ invariant is nonzero.
Class AII means spin-$1/2$ electrons with time-reversal symmetry, $\Theta^2 = -1$.

## Remarks

Topological invariants, such as the [[TKNN invariant|CX8GDHENTT]] in dimension $2$ without symmetry, or the $\Z_2$ invariant of Kane and Mele with time reversal, detect non-triviality.
At an interface between a topological and a trivial insulator, the gap must close, which produces gapless boundary states.

Example: in dimension $2$ with no symmetry, a band insulator whose filled bands have total Chern number $C \ne 0$ is a topological (Chern) insulator.
Indeed $C$ is unchanged along a gapped deformation, and it is $0$ for a $k$-independent Hamiltonian.

Non-example: a $k$-independent $H(k) = H_0$ with $E_F$ not an eigenvalue of $H_0$, an atomic insulator, is trivial by definition.
