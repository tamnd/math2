---
tag: RHSAMRWG3H
kind: definition
name: GENERIC formalism
msc: [82C35, 80A17]
defines: W67G4PYPGH
uses: [2S0MXDT4YH, 0PBY4E9GQF, 01MMVW8CKC, 0ABK9V9Y64, F6JVQ12X43, SPY89W0RJ7]
sources:
  - url: https://en.wikipedia.org/wiki/GENERIC_formalism
---

## Definition

Let the state $x$ of a closed system lie in a state space, here an open subset of $\R^n$.
Let $E(x)$ be its total energy and $S(x)$ its [[entropy|SPY89W0RJ7]], smooth functions with [[gradients|0ABK9V9Y64]] $\nabla E$ and $\nabla S$.
An evolution equation is in *GENERIC form* if it reads
$$\frac{dx}{dt} = L(x)\,\nabla E(x) + M(x)\,\nabla S(x),$$
where $L(x)$ and $M(x)$ are $n \times n$ matrices with these properties.

1. $L(x)$ is [[skew-symmetric|0PBY4E9GQF]], and $\set{A, B} = \nabla A^T L \nabla B$ satisfies the Jacobi identity, so it is a [[Poisson bracket|2S0MXDT4YH]].
2. $M(x)$ is symmetric and [[positive semidefinite|01MMVW8CKC]].
3. $L(x)\,\nabla S(x) = 0$ for all $x$.
4. $M(x)\,\nabla E(x) = 0$ for all $x$.

## Remarks

These conditions give $dE/dt = \nabla E^T L \nabla E + \nabla E^T M \nabla S = 0$ and $dS/dt = \nabla S^T L \nabla E + \nabla S^T M \nabla S \ge 0$.
Example: a particle of mass $m$ in a potential $V$ with friction coefficient $\gamma > 0$, whose lost energy becomes [[internal energy|F6JVQ12X43]] $e$ of a medium with entropy $S(e)$ and temperature $T(e) = 1/S'(e) > 0$.
Take $x = (q, p, e)$, $E = p^2/(2m) + V(q) + e$, $L$ the canonical skew matrix on $(q, p)$ and zero on $e$, and $M = \gamma T\, w w^T$ with $w = (0, 1, -p/m)$.
Then $L \nabla S = 0$ and $w^T \nabla E = p/m - p/m = 0$, so clauses 1 to 4 hold, and the equations are $\dot q = p/m$, $\dot p = -V'(q) - \gamma p/m$, $\dot e = \gamma p^2/m^2$.
Non-example: the same system with $M = \gamma T \operatorname{diag}(0, 1, 0)$ fails clause 4, since $M \nabla E = (0, \gamma T p/m, 0) \ne 0$ when $p \ne 0$.
In infinite dimensions, as for fluids, the gradients become functional derivatives and $L$, $M$ become operators.
