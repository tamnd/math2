---
tag: 8QBWWC354F
kind: definition
name: Principal curvature
msc: [53A05]
defines: FA8QE1SGP4
uses: [DQCD11X1VM, 6080X3FAD4, 9KHQR16P1B, 0ZND7NQ970, 0MB8HQW495]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_curvature
---

## Definition

Let $S \subseteq \R^3$ be a [[regular surface|6080X3FAD4]] with a smooth unit normal field $N$ near a point $p \in S$.
Let $S_p$ be the [[shape operator|DQCD11X1VM]] at $p$.
Since $S_p$ is [[self-adjoint|0MB8HQW495]], it has two real [[eigenvalues|0ZND7NQ970]] $k_1 \ge k_2$, counted with multiplicity.
These are the *principal curvatures* of $S$ at $p$.
A unit eigenvector of $S_p$ is a *principal direction* at $p$.

## Remarks

The principal directions can be chosen orthonormal, by the spectral theorem.
Equivalently, $k_1$ and $k_2$ are the maximum and the minimum of the [[second fundamental form|9KHQR16P1B]] $I\!I_p(w)$ over unit vectors $w \in T_p S$.
Replacing $N$ by $-N$ changes $k_1, k_2$ into $-k_2, -k_1$.
Example: for the saddle $z = xy$ at the origin, with $N = (0, 0, 1)$, one has $I\!I_0(a, b) = 2ab$ on $T_0 S = \R^2 \times \set{0}$.
So $k_1 = 1$ and $k_2 = -1$, with principal directions $(1, 1, 0)/\sqrt{2}$ and $(1, -1, 0)/\sqrt{2}$.
Non-example: on the same saddle, the normal curvature in the direction $(1, 0, 0)$ is $I\!I_0(1, 0) = 0$, which is neither $k_1$ nor $k_2$, so $(1, 0, 0)$ is not a principal direction.
