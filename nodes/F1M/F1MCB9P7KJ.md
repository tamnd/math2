---
tag: F1MCB9P7KJ
kind: definition
name: Integrable system
msc: [37J35, 70H06]
defines: N0N7CMRCMH
uses: [CAN490EPRT, 0EDKGA2FAK, 2S0MXDT4YH, 0262JP0NV9]
sources:
  - url: https://en.wikipedia.org/wiki/Integrable_system
---

## Definition

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]] of dimension $2n$, and let $H \colon M \to \R$ be a smooth function.
Let $\{F, G\}$ denote the [[Poisson bracket|2S0MXDT4YH]] of smooth functions $F, G$ on $M$.
The [[Hamiltonian system|0EDKGA2FAK]] with Hamiltonian $H$ is *integrable*, or *Liouville integrable*, if there are smooth functions $F_1 = H, F_2, \ldots, F_n \colon M \to \R$ such that:

1. $\{F_i, F_j\} = 0$ for all $i, j \in \set{1, \ldots, n}$;
2. the differentials $dF_1, \ldots, dF_n$ are linearly independent at each point of an open dense subset of $M$.

## Remarks

Clause 1 with $i = 1$ says that each $F_j$ is a [[first integral|0262JP0NV9]] of the system, since $\frac{d}{dt} F_j = \{F_j, H\}$ along solutions.
Functions that satisfy clause 1 are said to be in involution.

Example: on $\R^4$ with coordinates $(q_1, q_2, p_1, p_2)$, let $H = \frac{1}{2}(p_1^2 + q_1^2) + \frac{1}{2}(p_2^2 + q_2^2)$ and $F_2 = \frac{1}{2}(p_2^2 + q_2^2)$.
Then $\{H, F_2\} = \{\frac{1}{2}(p_2^2 + q_2^2), \frac{1}{2}(p_2^2 + q_2^2)\} = 0$, since the first summand of $H$ does not depend on $q_2, p_2$.
The differentials $dH$ and $dF_2$ are independent wherever $(q_1, p_1) \ne (0, 0)$ and $(q_2, p_2) \ne (0, 0)$, an open dense set.

Non-example: the same $H$ with $F_2 = H$ satisfies clause 1 but not clause 2, since $dF_1 = dF_2$ everywhere.

Every Hamiltonian system with one degree of freedom ($n = 1$) is integrable as soon as $dH \ne 0$ on an open dense set.
The [[Liouville–Arnold theorem|PNQCW85HTJ]] describes the motion of an integrable system near a compact regular level set.
