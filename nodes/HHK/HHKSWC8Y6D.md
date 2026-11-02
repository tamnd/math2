---
tag: HHKSWC8Y6D
kind: definition
name: Principal symbol of an operator on a manifold
msc: [58J40, 35S05, 47F05]
defines: S8GC34D5ZG
uses: [CGBX1N9V8H, F31T650DKY, P4DZM975BV, F45VQ47GPV, 0ZHSTAG8ZY, F4NWZNTRMD]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_operator
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] with cotangent bundle $\pi \colon T^*M \to M$, and let $E$ and $F$ be smooth [[vector bundles|P4DZM975BV]] over $M$.
Let $P \colon \Gamma(E) \to \Gamma(F)$ be a [[differential operator|CGBX1N9V8H]] of order at most $m$.
Let $x \in M$, $\xi \in T^*_x M$ and $e \in E_x$.
Choose a smooth function $f$ on $M$ with $f(x) = 0$ and $df(x) = \xi$, and a section $u \in \Gamma(E)$ with $u(x) = e$.
The *principal symbol* of order $m$ of $P$ is the bundle map $\sigma_m(P) \colon \pi^* E \to \pi^* F$ over $T^*M$ given by
$$\sigma_m(P)(x, \xi) \, e = \frac{1}{m!} \, P(f^m u)(x).$$

## Remarks

The right side does not depend on the choices of $f$ and $u$.
Take a chart and trivialisations in which $P = \sum_{\abs{\alpha} \le m} A_\alpha(x) \partial^\alpha$.
Then, with $\xi = \sum_j \xi_j \, dx_j$,
$$\sigma_m(P)(x, \xi) = \sum_{\abs{\alpha} = m} A_\alpha(x) \, \xi^\alpha.$$
Indeed, at $x$ only the terms in which all $m$ derivatives fall on distinct factors $f$ survive, and they give $m! \, \xi^\alpha$.
So $\sigma_m(P)$ agrees with the [[principal symbol|F31T650DKY]] on open subsets of $\R^n$, and it is homogeneous of degree $m$ in $\xi$.
Many texts include a factor $i^m$, defining the symbol through $D_j = -i \partial_j$; this does not change where the symbol is invertible.
The symbol is multiplicative: $\sigma_{m + l}(P Q) = \sigma_m(P) \, \sigma_l(Q)$.

Example: for the [[exterior derivative|0ZHSTAG8ZY]] $d$ on $k$-forms, $d(f \omega)(x) = df(x) \wedge \omega(x) + f(x) \, d\omega(x) = \xi \wedge \omega(x)$.
So $\sigma_1(d)(x, \xi) \omega = \xi \wedge \omega$.
For the [[Laplace–Beltrami operator|F4NWZNTRMD]] on functions of a Riemannian manifold, with the sign convention $\Delta = -\operatorname{div} \operatorname{grad} = -\sum_{j,k} g^{jk} \partial_j \partial_k + (\text{lower order})$, one gets $\sigma_2(\Delta)(x, \xi) = -\abs{\xi}_g^2$, or $\abs{\xi}^2_g$ with the factor $i^2$.

Non-example: the full expression $\sum_{\abs{\alpha} \le m} A_\alpha(x) \xi^\alpha$, with the lower-order terms kept, is not the principal symbol.
It depends on the chart: for $P = \partial_x^2$ on $\R$ and the new coordinate $y = e^x$, one has $P = y^2 \partial_y^2 + y \partial_y$, whose first-order term is not there in the old coordinate.

## Explanations

### L1 human

The principal symbol keeps the top-order derivatives of an operator, with each derivative replaced by a component of a covector.
