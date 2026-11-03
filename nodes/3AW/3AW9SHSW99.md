---
tag: 3AW9SHSW99
kind: definition
name: Bogoliubov transformation
msc: [81S05, 81T20]
defines: WR197X48YC
uses: [7N0J4DF8N5, 6TW5A09KCB, 0AR68JTMDT]
sources:
  - url: https://en.wikipedia.org/wiki/Bogoliubov_transformation
---

## Definition

Let $a_1, \dots, a_n$ be bosonic [[annihilation operators|7N0J4DF8N5]] with adjoints $a_1^*, \dots, a_n^*$, so that $[a_j, a_k^*] = \delta_{jk}$ and $[a_j, a_k] = 0$ for all $j, k$.
Let $U$ and $V$ be complex $n \times n$ matrices, and set
$$b_i = \sum_{j=1}^n \big( U_{ij}\, a_j + V_{ij}\, a_j^* \big), \qquad i = 1, \dots, n.$$
This is a *Bogoliubov transformation* if the $b_i$ satisfy the same relations, $[b_i, b_k^*] = \delta_{ik}$ and $[b_i, b_k] = 0$.
This holds if and only if
$$U U^* - V V^* = I \quad\text{and}\quad U V^T - V U^T = 0,$$
where $U^*$ is the conjugate transpose and $U^T$ the transpose of $U$.
For fermionic operators, which satisfy the [[canonical anticommutation relations|6TW5A09KCB]], the definition uses anticommutators instead.
Then the condition becomes $U U^* + V V^* = I$ and $U V^T + V U^T = 0$.

## Remarks

The conditions come from the computation $[b_i, b_k^*] = (UU^* - VV^*)_{ik}$ and $[b_i, b_k] = (UV^T - VU^T)_{ik}$.
Example: for $n = 1$, $b = \cosh(r)\, a + \sinh(r)\, a^*$ with $r \in \R$ is a bosonic Bogoliubov transformation, since $\cosh^2 r - \sinh^2 r = 1$; it is the single-mode squeezing transformation.
Non-example: $b = a + a^*$ has $U = V = 1$, so $UU^* - VV^* = 0 \ne 1$; indeed $b$ is self-adjoint and $[b, b^*] = 0$.
For fermions with $n = 1$, $b = u\, a + v\, a^*$ gives $\set{b, b^*} = \abs{u}^2 + \abs{v}^2$ and $\set{b, b} = 2uv$, so it is a Bogoliubov transformation only if one of $u, v$ is $0$, as for the particle-hole exchange $b = a^*$.
A genuine fermionic mixing needs two modes: $b_1 = u\, a_1 + v\, a_2^*$ and $b_2 = u\, a_2 - v\, a_1^*$ with $\abs{u}^2 + \abs{v}^2 = 1$ satisfy the conditions, since here $U = uI$ and $V$ is antisymmetric.
If $V = 0$, the condition says that $U$ is a [[unitary matrix|0AR68JTMDT]], and the transformation is an ordinary change of one-particle basis.
