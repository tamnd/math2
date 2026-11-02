---
tag: SCCP5E254A
kind: definition
name: Elliptic operator
msc: [47F10, 35J99]
defines: XY8GEQSWPR
uses: [09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set and let $m \ge 1$ be an integer.
For a multi-index $\alpha = (\alpha_1, \ldots, \alpha_n)$ of nonnegative integers, write $\abs{\alpha} = \alpha_1 + \cdots + \alpha_n$, $\partial^\alpha = \partial_1^{\alpha_1} \cdots \partial_n^{\alpha_n}$ for the [[partial derivatives|09EGC6F8PT]], and $\xi^\alpha = \xi_1^{\alpha_1} \cdots \xi_n^{\alpha_n}$ for $\xi \in \R^n$.
Let
$$L = \sum_{\abs{\alpha} \le m} a_\alpha(x) \partial^\alpha$$
be a linear differential operator of order $m$ on $\Omega$ with complex-valued continuous coefficients $a_\alpha$.
Its principal symbol is $\sigma_L(x, \xi) = \sum_{\abs{\alpha} = m} a_\alpha(x) \xi^\alpha$.
The operator $L$ is *elliptic* if
$$\sigma_L(x, \xi) \ne 0 \quad \text{for all } x \in \Omega \text{ and all } \xi \in \R^n \setminus \set{0}.$$

## Remarks

Many authors put a factor $i^m$ in the principal symbol; this does not change the condition.
For a second-order operator $L = \sum_{j,k} a_{jk}(x)\partial_j\partial_k + \sum_j b_j(x)\partial_j + c(x)$ with real symmetric $(a_{jk})$, ellipticity means that the matrix $(a_{jk}(x))$ is positive definite or negative definite at each $x$.
The operator is *uniformly elliptic* if there is $\theta > 0$ with $\sum_{j,k} a_{jk}(x)\xi_j\xi_k \ge \theta \abs{\xi}^2$ for all $x$ and $\xi$.
The definition extends to systems, where the symbol is a matrix that must be invertible, and to operators between vector bundles on manifolds.

Example: the [[Laplacian|0E0B6RA8K0]] $\Delta = \partial_1^2 + \cdots + \partial_n^2$ has symbol $\abs{\xi}^2$, which is nonzero for $\xi \ne 0$, so it is elliptic.
The Cauchy–Riemann operator $\partial_x + i\partial_y$ on $\R^2$ has symbol $\xi_1 + i\xi_2$, also nonzero for $\xi \ne 0$.

Non-example: the wave operator $\partial_1^2 - \partial_2^2$ on $\R^2$ has symbol $\xi_1^2 - \xi_2^2$, which vanishes at $\xi = (1, 1)$.
