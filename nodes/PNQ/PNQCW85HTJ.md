---
tag: PNQCW85HTJ
kind: statement
role: theorem
name: Liouville–Arnold theorem
msc: [37J35, 70H06, 53D12]
uses: [CAN490EPRT, 2S0MXDT4YH, C5EH3B4BEP, H8ACPTMX08, 03NM7DZXXC, N0N7CMRCMH, M3T81YNSKC]
about: [N0N7CMRCMH, M3T81YNSKC]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville–Arnold_theorem
same_as:
  wikidata: Q14943261
  wikipedia: Liouville–Arnold theorem
---

## Statement

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]] of dimension $2n$.
Let $F_1, \ldots, F_n \colon M \to \R$ be smooth functions with [[Poisson brackets|2S0MXDT4YH]] $\{F_i, F_j\} = 0$ for all $i, j$, and let $H = F_1$.
Let $F = (F_1, \ldots, F_n) \colon M \to \R^n$, let $c \in \R^n$ be a regular value of $F$, and let $M_c = F^{-1}(c)$.
Then:

1. $M_c$ is a smooth [[Lagrangian submanifold|H8ACPTMX08]] of dimension $n$. It is invariant under the flows of the [[Hamiltonian vector fields|C5EH3B4BEP]] $X_{F_1}, \ldots, X_{F_n}$.
2. Each compact connected component of $M_c$ is diffeomorphic to the [[torus|03NM7DZXXC]] $\mathbb{T}^n = \R^n / 2\pi \Z^n$.
3. On such a component there are angle coordinates $\theta \in \mathbb{T}^n$ in which the flow of $X_H$ is linear: $\theta(t) = \theta(0) + t \, \nu(c)$ for a vector $\nu(c) \in \R^n$.
4. A neighbourhood of such a component has [[action-angle coordinates|M3T81YNSKC]] $(I, \theta)$ in which $H$ is a function of $I$ only.

## Remarks

Since the $F_i$ Poisson-commute, the flows of $X_{F_1}, \ldots, X_{F_n}$ commute and preserve $M_c$.
They give an action of $\R^n$ on each component of $M_c$, which is locally free because the $dF_i$ are independent there.
A compact connected manifold with a transitive locally free $\R^n$-action is $\R^n / \Lambda$ for a lattice $\Lambda$, that is, a torus.
The actions are built from the integrals $\oint p \, dq$ over the basic cycles of the tori.

Example: for two uncoupled harmonic oscillators on $\R^4$, with $F_1 = \frac{1}{2}(p_1^2 + q_1^2) + \frac{1}{2}(p_2^2 + q_2^2)$ and $F_2 = \frac{1}{2}(p_2^2 + q_2^2)$, the level sets with $c_1 > c_2 > 0$ are products of two circles, that is, $2$-tori.

Compactness is necessary for the torus conclusion.
For a free particle on $\R$ with $H = p^2/2$, the level set $H = c > 0$ is two lines, not circles, and the motion is not periodic.

## Explanations

### L1 human

If a mechanical system with $n$ degrees of freedom has $n$ independent conserved quantities that are compatible with each other, then its motion is very simple.
Each bounded motion lives on a doughnut-shaped surface, an $n$-dimensional torus.
On the torus, the motion is a straight line wound around at constant speeds.
This is one precise meaning of "the system can be solved".

### L2 human

The theorem is the structure theorem for [[integrable systems|N0N7CMRCMH]].
It turns the algebraic condition of commuting integrals into a geometric picture: a fibration of phase space by invariant Lagrangian tori, with linear flow on each torus.
The frequency vector $\nu$ decides the type of motion.
When its entries are rationally independent, each orbit is dense in its torus.
When they satisfy an integer relation, the torus is filled by invariant tori of lower dimension, and no orbit is dense in it.
This picture is the starting point of [[KAM theory|3ZZSXKM16Z]], which asks which tori survive a small perturbation of $H$.
