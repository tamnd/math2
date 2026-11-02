---
tag: MX6D07DDAZ
kind: definition
name: Principal symbol
msc: [35A99, 47F05, 35S05]
defines: F31T650DKY
uses: [6DZETZ5T9G, 0PJXBR6QA3, 2C3PAQ7H50]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_operator
---

## Definition

Let $\Omega$ be an open set in $\R^n$.
Let $P = \sum_{\abs{\alpha} \le m} a_\alpha(x) \, \partial^\alpha$ be a [[linear differential operator|6DZETZ5T9G]] of order $m$ on $\Omega$, with [[multi-indices|0PJXBR6QA3]] $\alpha$.
The *principal symbol* of $P$ is the following function of $x \in \Omega$ and $\xi \in \R^n$.
$$\sigma_m(P)(x, \xi) = \sum_{\abs{\alpha} = m} a_\alpha(x) \, \xi^\alpha.$$
Here $\xi^\alpha = \xi_1^{\alpha_1} \cdots \xi_n^{\alpha_n}$.
For each fixed $x$, it is a [[homogeneous polynomial|2C3PAQ7H50]] of degree $m$ in $\xi$.

## Remarks

Example: for $P = \partial_x^2 - \partial_y^2 + 5 \partial_x + 1$ on $\R^2$, the order is $2$ and $\sigma_2(P)(x, \xi) = \xi_1^2 - \xi_2^2$; the terms $5 \partial_x$ and $1$ do not contribute.
Non-example: the full polynomial $\xi_1^2 - \xi_2^2 + 5 \xi_1 + 1$ is not the principal symbol, because it keeps the lower-order terms.
Many texts write $P = \sum a_\alpha(x) D^\alpha$ with $D_j = -i \partial_j$ and define the principal symbol as $\sum_{\abs{\alpha} = m} a_\alpha(x) \xi^\alpha$ in those coefficients; this differs from the definition above by the factor $i^m$.
The vanishing of the principal symbol, and so the [[characteristic variety|CQJ2E2ARRF]], is the same in all conventions.
On a manifold, the principal symbol is a well-defined function on the cotangent bundle.

## Explanations

### L1 human

The principal symbol is what remains of a differential operator when only its top-order terms are kept and each derivative is replaced by a variable.
