---
tag: PJVSCHMM6Z
kind: statement
role: theorem
name: Prigogine's minimum entropy production principle
msc: [82C35, 80A17]
uses: [STR73R5MX4, 9YACB2RQ80, 0KX66CZMBB]
about: [STR73R5MX4]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_production
---

## Statement

Let a system in the linear regime have thermodynamic forces $X = (X_1, \dots, X_n)$ and fluxes
$$J_i = \sum_{k=1}^{n} L_{ik} X_k,$$
where $L = (L_{ik})$ is a constant, symmetric, [[positive definite matrix|0KX66CZMBB]].
Let its [[entropy production|STR73R5MX4]] be $\sigma(X) = \sum_{i} J_i X_i = X^T L X$.
Fix $m$ of the forces, $X_1 = a_1, \dots, X_m = a_m$, with $1 \le m < n$, and let the other forces vary.
Then $\sigma$, restricted to these forces, has exactly one minimum point.
A point $X$ with $X_i = a_i$ for $i \le m$ is this minimum if and only if
$$J_{m+1} = \cdots = J_n = 0.$$
So the stationary state, in which the unconstrained fluxes vanish, is the state of least entropy production compatible with the constraints.

## Remarks

The proof is a direct computation.
For $j > m$, symmetry of $L$ gives $\partial \sigma / \partial X_j = 2 \sum_k L_{jk} X_k = 2 J_j$.
The restriction of $\sigma$ is a quadratic function whose Hessian is twice a principal submatrix of $L$, which is positive definite, so it has one minimum, where the gradient vanishes.
The symmetry $L_{ik} = L_{ki}$ comes from the [[Onsager reciprocal relations|9YACB2RQ80]]; without it the gradient is not $2J$ and the stationary state need not minimise $\sigma$.
Example: in thermal diffusion with a fixed temperature difference, the steady state with zero mass flux is the minimum of $\sigma$ at that temperature difference.

## Explanations

### L1 human

Keep a system under a fixed outside stress, such as a fixed temperature difference, and let it settle.
Close to equilibrium, it settles into the steady state that creates entropy at the smallest rate allowed by the stress.
This gives a variational principle for steady states, like the energy minimum for equilibrium states.

### L2 human

The principle holds only in the linear regime with constant coefficients and symmetric $L$.
Since $\sigma$ decreases along the approach to the steady state in this regime, it also acts as a Lyapunov function and gives stability of the steady state.
Far from equilibrium, or when the coefficients depend on the state, the principle fails in general.
