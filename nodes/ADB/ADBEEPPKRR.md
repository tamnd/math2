---
tag: ADBEEPPKRR
kind: example
name: Toda lattice
msc: [37J35, 37K60, 70H06]
instance_of: [N0N7CMRCMH]
uses: [0EDKGA2FAK, G3A4S7CSB3, 2S0MXDT4YH]
sources:
  - url: https://en.wikipedia.org/wiki/Toda_lattice
same_as:
  wikidata: Q572090
  wikipedia: Toda lattice
---

## Example

Let $n \ge 2$.
The open *Toda lattice* is the [[Hamiltonian system|0EDKGA2FAK]] on $\R^{2n}$ with positions $q_1, \ldots, q_n$, momenta $p_1, \ldots, p_n$ and Hamiltonian
$$H(q, p) = \sum_{k=1}^{n} \frac{p_k^2}{2} + \sum_{k=1}^{n-1} e^{-(q_{k+1} - q_k)}.$$
It describes $n$ particles on a line with exponential forces between neighbours.

It is an [[integrable system|N0N7CMRCMH]].
Flaschka's variables are $a_k = \frac{1}{2} e^{-(q_{k+1} - q_k)/2}$ for $1 \le k \le n - 1$ and $b_k = -\frac{1}{2} p_k$ for $1 \le k \le n$.
Let $L$ be the symmetric tridiagonal $n \times n$ matrix with diagonal entries $b_1, \ldots, b_n$ and off-diagonal entries $a_1, \ldots, a_{n-1}$.
The equations of motion can be written as a [[Lax pair|G3A4S7CSB3]] equation $L' = [B, L]$, where $B$ is an antisymmetric tridiagonal matrix whose off-diagonal entries are $\pm a_k$.
So $L(t)$ is conjugate to $L(0)$ for all $t$, and the $n$ eigenvalues of $L$, or the traces $\tr L^m$ for $m = 1, \ldots, n$, are first integrals.
These integrals are independent and Poisson-commute, which gives Liouville integrability.

A check of the scaling: $\tr L^2 = \sum_k b_k^2 + 2 \sum_k a_k^2 = \frac{1}{4} \sum_k p_k^2 + \frac{1}{2} \sum_k e^{-(q_{k+1} - q_k)} = \frac{1}{2} H$.
Also $\tr L = -\frac{1}{2} \sum_k p_k$ is a multiple of the total momentum.

## Remarks

Morikazu Toda introduced the lattice in 1967.
Its integrability was shown by Hénon and by Flaschka in 1974.
There is also a periodic Toda lattice, with $q_{n+1} = q_1$, which is integrable as well.

## Explanations

### L1 human

The Toda lattice is a row of particles pushed apart by forces that grow exponentially as neighbours come close.
Although the forces are nonlinear, the system has as many conserved quantities as particles, so its motion is completely regular.
The conserved quantities are hidden in a matrix built from positions and momenta: as time goes on the matrix changes, but its eigenvalues do not.
