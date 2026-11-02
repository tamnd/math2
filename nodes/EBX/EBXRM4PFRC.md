---
tag: EBXRM4PFRC
kind: problem
name: Fermi–Pasta–Ulam–Tsingou problem
msc: [37K60, 37N20, 70K75]
uses: [0EDKGA2FAK, N0N7CMRCMH]
about: [N0N7CMRCMH]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi–Pasta–Ulam–Tsingou_problem
same_as:
  wikidata: Q462254
  wikipedia: Fermi–Pasta–Ulam–Tsingou problem
history:
  posed_by: "Enrico Fermi, John Pasta, Stanislaw Ulam and Mary Tsingou"
  first_stated: "1955"
---

## Problem

Let $N \ge 2$ and $\alpha \in \R$.
Consider $N$ particles on a line with displacements $q_1, \ldots, q_N$ and momenta $p_1, \ldots, p_N$, with fixed ends $q_0 = q_{N+1} = 0$, and the [[Hamiltonian system|0EDKGA2FAK]] with Hamiltonian
$$H = \sum_{k=1}^{N} \frac{p_k^2}{2} + \sum_{k=0}^{N} \left( \frac{1}{2} (q_{k+1} - q_k)^2 + \frac{\alpha}{3} (q_{k+1} - q_k)^3 \right).$$
For $\alpha = 0$ the chain is a set of $N$ independent normal modes, each with a conserved energy.
Start with all energy in the lowest normal mode and $\alpha \ne 0$ small.
Explain the long-time behaviour of the energies of the normal modes.
In particular, explain why the energy does not spread evenly over all modes.
Instead it stays in a few low modes and returns almost completely to the initial mode after some time.

## Remarks

Fermi, Pasta, Ulam and Tsingou expected the nonlinear term to share the energy evenly between the modes, as statistical mechanics predicts for an ergodic system.
Their computer simulation on the MANIAC computer at Los Alamos showed the opposite: near recurrences to the initial state.
In 1965 Zabusky and Kruskal studied a continuum limit of the chain, which is the [[Korteweg–De Vries equation|KTT75QC72Z]], and discovered [[solitons|63D4AXYCT4]] in it.
Other explanations use the closeness of the chain to an [[integrable system|N0N7CMRCMH]], namely the [[Toda lattice|ADBEEPPKRR]], and KAM-type and Nekhoroshev-type stability.
It is now understood that for small energies the approach to equipartition, if any, happens only on very long time scales.
A full quantitative description is still a subject of research.

## Explanations

### L1 human

Take a chain of masses joined by springs that are slightly nonlinear, and pluck it in its simplest way of vibrating.
Physicists expected the energy to spread to all the ways of vibrating, like heat spreading out.
One of the first computer experiments showed that it does not: the energy moves to a few nearby ways of vibrating and then comes back almost entirely.
Explaining this surprise led to the discovery of solitons and to a large part of modern nonlinear science.
