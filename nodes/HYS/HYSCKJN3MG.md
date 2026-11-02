---
tag: HYSCKJN3MG
kind: definition
name: Poisson bracket
msc: [53D05, 37J39]
defines: 2S0MXDT4YH
uses: [CAN490EPRT, C5EH3B4BEP]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_bracket
---

## Definition

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]].
For a smooth function $f \colon M \to \R$, let $X_f$ be its [[Hamiltonian vector field|C5EH3B4BEP]], so $\iota_{X_f} \omega = df$.
The *Poisson bracket* of smooth functions $f, g \colon M \to \R$ is the smooth function
$$\{f, g\} = \omega(X_f, X_g).$$

## Remarks

Equivalently $\{f, g\} = df(X_g) = X_g(f) = -X_f(g)$.
The bracket is bilinear and antisymmetric, satisfies the Leibniz rule $\{f, gh\} = \{f, g\} h + g \{f, h\}$, and satisfies the Jacobi identity because $d\omega = 0$.
With these conventions $X_{\{f, g\}} = -[X_f, X_g]$.

Example: on $\R^{2n}$ with $\omega = \sum_i dq_i \wedge dp_i$,
$$\{f, g\} = \sum_{i=1}^n \left( \frac{\partial f}{\partial q_i} \frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i} \frac{\partial g}{\partial q_i} \right).$$
For instance $X_{p_j} = \partial / \partial q_j$, so $\{q_i, p_j\} = X_{p_j}(q_i) = \delta_{ij}$, while $\{q_i, q_j\} = \{p_i, p_j\} = 0$.

Non-example: on $\R^4$ the closed $2$-form $dq_1 \wedge dp_1$ is degenerate, so it does not define a bracket in this way: the function $q_2$ has no Hamiltonian vector field for it.

Along an integral curve $\gamma$ of $X_H$, a function $g$ satisfies $\frac{d}{dt} g(\gamma(t)) = \{g, H\}(\gamma(t))$.
Some authors use the opposite sign convention for $\{f, g\}$.
