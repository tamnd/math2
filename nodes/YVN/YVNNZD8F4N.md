---
tag: YVNNZD8F4N
kind: example
name: Lieb–Liniger model
msc: [82B23, 81Q80, 81V73]
instance_of: [DVQ0PVHKY1]
uses: [S92G5M6X41]
sources:
  - url: https://en.wikipedia.org/wiki/Lieb%E2%80%93Liniger_model
same_as:
  wikidata: Q6543926
  wikipedia: Lieb–Liniger model
---

## Example

The *Lieb–Liniger model* describes $N$ identical bosons on a circle of length $L$ with a repulsive contact interaction of strength $c > 0$.
In units with $\hbar = 2m = 1$, its Hamiltonian acts on symmetric wave functions $\psi(x_1, \ldots, x_N)$ with $x_j \in [0, L)$ periodic:
$$H = -\sum_{j=1}^N \frac{\partial^2}{\partial x_j^2} + 2c \sum_{1 \le i < j \le N} \delta(x_i - x_j).$$
Elliott Lieb and Werner Liniger solved it in 1963 with the [[Bethe ansatz|S92G5M6X41]].
In the region $x_1 < x_2 < \cdots < x_N$ the eigenfunctions are finite sums of plane waves $e^{i(k_{P1} x_1 + \cdots + k_{PN} x_N)}$ over permutations $P$, with real quasi-momenta $k_1, \ldots, k_N$.
Periodicity forces the Bethe equations
$$e^{i k_j L} = \prod_{l \ne j} \frac{k_j - k_l + i c}{k_j - k_l - i c}, \qquad j = 1, \ldots, N,$$
and the energy is $E = k_1^2 + \cdots + k_N^2$.

Check in two limits.
For $c = 0$ every factor is $1$, so $e^{i k_j L} = 1$ and $k_j \in (2\pi/L)\Z$: these are free bosons on the circle.
As $c \to \infty$ every factor tends to $-1$, so $e^{i k_j L} = (-1)^{N-1}$: the spectrum is that of free fermions, the Tonks–Girardeau gas.

## Remarks

In the thermodynamic limit at fixed density, the ground state is described by a density of quasi-momenta that solves the [[Lieb–Liniger integral equation|Z219Y8PJHD]].
The model is one of the basic exactly solvable models of one-dimensional quantum gases, and it has been realized with cold atoms in narrow traps.

## Explanations

### L1 human

Put bosons on a ring and let them repel only when they touch.
Each particle's wave picks up a fixed phase whenever it passes another, and the requirement to come back to itself around the ring gives a short list of equations.
Solving these equations gives every energy level exactly, which is rare for interacting particles.
With no interaction the bosons are free; with infinitely strong repulsion they act like fermions that cannot pass each other.
